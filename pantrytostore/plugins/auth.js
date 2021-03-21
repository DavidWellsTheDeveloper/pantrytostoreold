export default function ({ app }) {
  // axios default error handler - called first on every response
  const $axios = app.$axios
  $axios.onError((axiosError) => {
    // always log error
    console.error(axiosError)

    // no connection
    if (!axiosError.response) {
      return
    }

    // for authorization errors, check if secret key rotated
    const authErr = [401, 403].includes(parseInt(axiosError.response.status))
    if (app.$auth.$state.loggedIn && authErr) {
      app.$auth.logout()
    }
  })
}
