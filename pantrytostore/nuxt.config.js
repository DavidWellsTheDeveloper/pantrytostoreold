import colors from 'vuetify/es5/util/colors'

const development = process.env.NODE_ENV !== 'production'

export default {
  // Target (https://go.nuxtjs.dev/config-target)
  target: 'static',

  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    titleTemplate: '%s - pantrytostore',
    title: 'pantrytostore',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: ['@/assets/css/style.scss'],

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: ['~/plugins/auth.js'],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: true,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
    // https://go.nuxtjs.dev/vuetify
    '@nuxtjs/vuetify',
  ],

  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: ['@nuxtjs/auth', '@nuxtjs/axios', '@nuxt/http'],

  axios: {
    baseURL: development
      ? 'http://localhost:8000'
      : 'https://pantrytostore.com/api',
  },

  // Vuetify module configuration (https://go.nuxtjs.dev/config-vuetify)
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: false,
      themes: {
        dark: {
          primary: colors.cyan.darken4,
          secondary: colors.lightBlue.lighten3,
          accent: colors.teal.darken4,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.red.base,
          success: colors.green.accent3,
        },
        light: {
          primary: colors.teal.lighten2,
          secondary: colors.blue.darken4,
          accent: colors.teal.accent4,
          info: colors.cyan.accent4,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3,
        },
      },
    },
  },

  middleware: 'auth',

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {},

  auth: {
    strategies: {
      // JWT token auth
      local: {
        scheme: 'refresh',
        endpoints: {
          login: {
            url: '/api/token/',
            method: 'post',
            propertyName: 'access',
          },
          refreshToken: {
            url: 'api/token/refresh/',
            method: 'post',
            property: 'refresh',
          },
          logout: false,
          user: {
            url: '/user/users/',
            method: 'get',
            propertyName: false,
          },
        },
      },
    },
  },
  router: {
    // By default, views will require login.
    middleware: ['auth'],
  },
}
