<template>
  <v-app dark>
    <v-navigation-drawer v-model="drawer" clipped app>
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar clipped-left app>
      <v-app-bar-nav-icon @click="drawer = !drawer" />
      <v-toolbar-title v-text="title" />
    </v-app-bar>
    <v-main>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>
    <v-footer absolute app>
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
      items: [
        {
          icon: 'mdi-apps',
          title: 'Welcome',
          to: '/',
        },
        {
          icon: 'mdi-cart-variant',
          title: 'Grocery List',
          to: '/Grocery',
        },
        {
          icon: 'mdi-text-box-search',
          title: 'Find Recipes',
          to: '/search',
        },
        {
          icon: 'mdi-text-box-multiple',
          title: 'My Recipes',
          to: '/MyRecipes',
        },
      ],
    }
  },
  head() {
    return {
      titleTemplate: '%s - Pantry To Store',
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
