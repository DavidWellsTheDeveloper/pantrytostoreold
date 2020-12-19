#!/usr/bin/env bash
################################################################################
# Deploy script for Pantry To Store App - backend api
#
# Dependencies:
# USER: Has root permission (script must be run as 'sudo')
# OTHER: Required arguments sourced from '.env'. If variables are empty, script exits.
#
# CMD arguments:
#	1: repo name			ex. pantrytostore
#	2: branch name			ex. master
#
# To execute:
#   $ sudo ./startup.sh "pantrytostore" "master"
#
# Author:
# Chris Keyes, chris.keyes@mountaindatagroup.com (GitHub: Chuy5685)
# And David Wells, dave1.t.wells@gmail.com (GitHub: DavidWellsTheDeveloper)
# Last Updated: 12/14/2020
################################################################################
cd "$(dirname "$0")" || exit 1

errmsg="For assistance with this error, please send terminal output to Operations team."
TOKEN="e3e45b60304b8dd36b65bcf76b6dd86fc09aa48f"

# Read in command line parameters.  Check for required and exit if Null.
repo="$1"
branch="$2"
if [ -z "$repo" ] || [ -z "$branch" ]; then
    echo "[error] Expecting cmd arguments 'repo' 'branch'."
    echo -e "Ex.\t$ ./startup.sh 'crime-dashboard' 'master'"
    exit 1
fi

# if [ ! -e "$(pwd)/.env" ]; then
#     echo "[error] Environment variable not found. Make sure '$(pwd)/.env' exists."
#     exit 1
# else
#     . "$(pwd)"/.env
# fi

npm_app="${npm_app:=pantrytostore}"
django="${django:=backend}"
app_domain="${app_domain:=pantry.focowebsites.com}"
appuser="${appuser:=nodejs}"		        # user for app to run as
appservice="${django}-gunicorn"			# systemd daemon service name


export repodir="${reporoot:=/var/www}/${repo}"

# directory of nuxt project
export npmdir="${repodir}/pantrytostore"

# Echo deploy variables
echo "Deploying:"
echo "  Github project:         $repo"
echo "  Branch name:            $branch"
echo
echo "  Django project:         $django"
echo "  Django project path:    ${repodir}/${django}"
echo
echo "  App user account:       $appuser"
echo "  App domain:             $app_domain"
echo "  Project path:           $repodir"
echo
sleep 3

set -v
set -eo pipefail
# -v: Verbose print command
# -e: Exit for non-zero commands
# -o pipefail: Pass non-zero status through pipes


# Make directories for repo and source files if
# not already created.
echo "Updating $django sources ..."
mkdir -p "$reporoot"


# [PACKAGE DEPENDENCIES]

echo "Installing system dependencies ..."

# Get NodeJS PPA
curl -sL https://deb.nodesource.com/setup_10.x | bash -

apt update
apt-get upgrade -yq || exit 1

if [ $? -ne 0 ]; then
	echo "[error] Failed to install system dependencies."
    echo "$errmsg"
	exit 1
fi


# [BUILD APP]

echo "Building app $django from source code ..."

export HOME=/root
if [ ! -d "$repodir" ]; then
	echo "Cloning $repo from $branch branch ..."
	(
	cd "$reporoot"
	git clone https://"${TOKEN}"@github.com/DavidWellsTheDeveloper/"${repo}".git
	)
else
    echo "Existing $repo found, stoping app service ..."
    # stop backend now
    if ! systemctl stop "$appservice"; then
        echo "[warning] Failed to stop $appservice with systemctl."
    fi
    sleep 1

    # archive existing logs
    # TODO: archive access.log and err.log files to directory

    echo "Merging updates from $branch ..."
    # stash before merge
    # on error, dump changes in a branch, commiit then continue
    git -C "${repodir}" stash || \
        (cd "${repodir}"; git checkout stash -- .; git commit)
fi

git -C "${repodir}" pull
git -C "${repodir}" checkout "$branch"

echo "Verify git status..."
git -C "${repodir}" status


# create new app key using uuid4 and output into file
# if [ -e "${srcdir}"/key.txt ]; then
#     echo "Existing security key found..."
#     echo "Continuing."
# else
#     echo "Creating new app security key ..."
#     $(which python3) -c "from uuid import uuid4; print(uuid4())" > "${srcdir}"/key.txt
# fi


echo "Creating python environment ..."
virtualenv -p python3 "${repodir}"/"${django}"/venv

if ! "${repodir}"/"${django}"/venv/bin/pip install -r "${repodir}"/"${django}"/"${pipfile:-requirements.txt}"; then
	echo "[error] Failed to create venv and install python packages."
    echo "$errmsg"
	exit 1
fi

echo "Collecting Django static files ..."
if ! "${repodir}"/"${django}"/venv/bin/python "${repodir}"/"${django}"/manage.py \
    collectstatic --no-input --clear ; then
    echo "[warning] Failed to collect static files"
    echo "You will need to copy static files for Django"
    echo
fi

# [APP CONFIG SETTINGS]

echo "Congifuring system handlers ..."
cat > "${repodir}"/"${django}"/start-gunicorn.sh << EOF
#!/bin/bash
cd ${repodir}/${django} || exit 1
# Activate the virtualenv
source venv/bin/activate
# Additional environmental variables required
# export CONFIGPATH="${srcdir}"		# path used in deploy.sh
export APP_HOST="$app_domain"		# add canonical name to whitelist
# Run gunicorn with these options:
# hot reload changes to app files
# create access and error logs
exec venv/bin/gunicorn \
    -w ${workers:-5} \
    -b ${bindhost:-127.0.0.1:8888} \
    --reload \
    --access-logfile access.log \
    --error-logfile err.log \
    $django.wsgi
EOF

# # nuxt server for static site
# cat > "${appsubdir}"/frontend/start-nuxt.sh << EOF
# #!/bin/bash
# pwd
# cd ${appsubdir}/frontend || exit 1
# exec npm run start
# EOF



# Reset permissions to app dir, config files, and update executable script
# Set owner to app user, leave group as root
chmod ugo+rx "${repodir}"/"${django}"/start-gunicorn.sh
# chmod ugo+rx "${appsubdir}"/frontend/start-nuxt.sh
chown -R "$appuser" "${repodir}"        # change owner of repo



# Create systemd unit file. This will tell systemd how to start
# our service. Systemd will restart gunicorn if it dies, and start
# it on reboot.
cat > /etc/systemd/system/"$appservice".service << EOF
[Unit]
Description=$repo gunicorn daemon
After=network.target
[Service]
User=$appuser
Group=$appuser
WorkingDirectory=${repodir}/${django}
Environment=PATH=/sbin:/bin:/usr/sbin:/usr/bin
ExecStart=${repodir}/${django}/start-gunicorn.sh
Restart=always
[Install]
WantedBy=multi-user.target
EOF

# # nuxt systemd unit file
# cat > /etc/systemd/system/nuxt.service << EOF
# [Unit]
# Description=$repo nuxt daemon
# After=network.target
# 
# [Service]
# User=$appuser
# Group=$appuser
# WorkingDirectory=${repodir}/frontend
# Environment=PATH=/sbin:/bin:/usr/sbin:/usr/bin
# ExecStart=${repodir}/frontend/start-nuxt.sh
# Restart=always
# 
# [Install]
# WantedBy=multi-user.target
# EOF



#########################################################################
# Define NGINX http server configuration.

# If there is a pre-defined '*.conf' file in this directory with correct
# domain name (ie matching $app_domain) then use that conf file.
# Otherwise, write a simple server conf to default NGINX path.
if [ -f "$(pwd)"/"$app_domain".conf ];
then
echo "Found local NGINX app config file..."
echo "Will configure HTTP server using: '$(pwd)/$app_domain.conf'"
cp "$(pwd)"/"$app_domain".conf /etc/nginx/sites-available/"$app_domain".conf
else
echo "No local NGINX app config file found at $(pwd)"
echo "Creating HTTP server config for '$app_domain' ..."
echo
echo "[warning] Web app '$app_domain' will be on HTTP ONLY!!"
echo "Correct this when SSL is available."
cat > /etc/nginx/sites-available/"$app_domain".conf <<-EOF
server {
    listen 80;
    listen [::]:80;
    server_name smell-test.mdg-test.com;
    location = /favicon.ico { access_log off; log_not_found off; }
    location /api/ {                                                                                                                                      
        include proxy_params;
        proxy_pass http://127.0.0.1:8888;
    }
    location / {                                                                                                                                      
        include proxy_params;
        proxy_pass http://${bindhost:-127.0.0.1:3000};
    }
}
EOF
fi

# Remove NGINX default server conf and create sym links to this app's conf.
if ! rm /etc/nginx/sites-enabled/default; then
    echo "Default nginx conf already removed."
fi
ln -s --force \
    /etc/nginx/sites-available/"$app_domain".conf \
    /etc/nginx/sites-enabled/"$app_domain".conf


echo "Reloading systemd and app service ..."

# Tell systemd to reread the service files
systemctl daemon-reload

# Reload NGINX
service nginx configtest
service nginx reload
systemctl restart nginx


# start web app now
systemctl start "$appservice"

# start web app on restart
systemctl enable "$appservice"
# systemctl enable nuxt

echo
echo "Django app started."
echo "To check the status, run:"
echo -e "\t$ systemctl status $appservice"
echo "Check Django ALLOWED_HOST settings."
echo "The server has been configured to proxy external HTTP requests to:"
echo "http://$bindhost"


# # build/start nuxt app
# echo "Stopping nuxt service"
# if ! systemctl stop nuxt; then
#     echo "[warning] Failed to stop nuxt with systemctl."
# fi
# sleep 1

# echo "Building nuxt app."
# cd "${npmdir}" || exit 1
# npm install
# npm run generate --fail-on-error
# 
# # reload nuxt service
# echo "Reloading nuxt systemd ..."
# systemctl start nuxt
# systemctl enable nuxt

echo
echo "************************************************************************"
echo "Done."
echo "************************************************************************"

# Done.
