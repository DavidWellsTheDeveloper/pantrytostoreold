# Installing venv
if [ ! -d "./venv" ]
then
  echo "Directory does not exist, creating venv"
  python3 -m virtualenv -p python3 venv
else
  echo "venv directory exists."
fi

# Installing Requirements
source venv/bin/activate
pip install -r requirements.txt