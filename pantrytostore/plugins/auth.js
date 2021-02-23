export default function ({ app }) {
  // axios default error handler - called first on every response
  const { $axios, $auth } = app
  $axios.onError((axiosError) => {
    // always log error
    console.error(axiosError)

    // no connection
    if (!axiosError.response) {
      return
    }

    // for authorization errors, check if secret key rotated
    const authErr = [401, 403].includes(parseInt(axiosError.response.status))
    if ($auth.loggedIn && authErr) {
      // $auth.refreshTokens().catch(() => {
      // eslint-disable-next-line no-console
      $auth.logout()
      // })
    }
  })
}
