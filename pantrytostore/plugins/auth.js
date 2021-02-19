export default function ({ $axios, app, error }, inject) {
  // axios default error handler - called first on every response
  $axios.onError((axiosError) => {
    // always log error
    console.error(axiosError)

    // no connection
    if (!axiosError.response) {
      error({})
      return
    }

    // for authorization errors, check if secret key rotated
    const authErr = [401, 403].includes(parseInt(axiosError.response.status))
    if (app.$auth.loggedIn && authErr) {
      app.$auth.refreshTokens().catch(() => {
        // eslint-disable-next-line no-console
        app.$auth.logout()
      })
    }
  })
}
