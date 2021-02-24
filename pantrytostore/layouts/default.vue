<template>
  <v-app dark>
    <v-navigation-drawer
      v-model="drawer"
      :expand-on-hover="$vuetify.breakpoint.mdAndUp"
      :permanent="$vuetify.breakpoint.mdAndUp"
      app
      dark
      color="primary"
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in itemsCommon"
          :key="i"
          :to="item.to"
          :color="activeLinkColor"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item @click="toggleDarkTheme()">
          <v-list-item-action>
            <v-icon>
              {{
                $vuetify.theme.dark ? 'mdi-brightness-5' : 'mdi-weather-night'
              }}
            </v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Change Theme</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
      </v-list>

      <v-list v-show="$auth.loggedIn">
        <v-list-item
          v-for="(item, i) in itemsLoggedIn"
          :key="i"
          :to="item.to"
          :color="activeLinkColor"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item @click="logout()">
          <v-list-item-action>
            <v-icon>mdi-account-circle</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-list v-show="!$auth.loggedIn">
        <v-list-item
          v-for="(item, i) in itemsNotLoggedIn"
          :key="i"
          :to="item.to"
          :color="activeLinkColor"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar v-if="$vuetify.breakpoint.smAndDown" clipped-left app>
      <v-app-bar-nav-icon @click="drawer = !drawer" />
      <v-toolbar-title>{{ title }}</v-toolbar-title>
    </v-app-bar>
    <v-main>
      <nuxt />
    </v-main>
    <v-footer app>
      <span>&copy; PantryToStore {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      title: 'Pantry To Store',
      drawer: false,
      fixed: false,
      itemsCommon: [
        {
          icon: 'mdi-apps',
          title: 'Welcome',
          to: '/',
        },
      ],
      itemsLoggedIn: [
        {
          icon: 'mdi-cart-variant',
          title: 'Grocery List',
          to: '/Grocery',
        },
        {
          icon: 'mdi-text-box-multiple',
          title: 'My Recipes',
          to: '/MyRecipes',
        },
        {
          icon: 'mdi-application-import',
          title: 'Import Recipes',
          to: '/AddRecipes',
        },
        {
          icon: 'mdi-plus-box',
          title: 'Create Recipe',
          to: '/CreateRecipe',
        },
      ],
      itemsNotLoggedIn: [
        {
          icon: 'mdi-account-circle',
          title: 'Login',
          to: '/Login',
        },
        {
          icon: 'mdi-account-check-outline',
          title: 'Register',
          to: '/Register',
        },
      ],
      activeLinkColor: 'secondary',
    }
  },

  methods: {
    logout() {
      this.$auth.logout()
      this.$router.push({ name: 'Login' })
    },
    toggleDarkTheme() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark
    },
  },

  head() {
    return {
      title: 'Food Management Solution',
      titleTemplate: 'Pantry To Store | %s',
      meta: [
        {
          hid: 'description',
          name: 'description',
          content:
            'Pantry To Store is an all-in-one food management solution. The goal is to make Pantry To Store the only application you need to go from finding recipes and managing dietary plans to building your grocery list.',
        },
      ],
    }
  },
}
</script>
