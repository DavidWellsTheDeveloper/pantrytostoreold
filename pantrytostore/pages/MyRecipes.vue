<template>
  <v-container>
    <h1>My Recipes</h1>
    <v-row v-if="recipes.length >= 1">
      <v-col v-for="recipe in recipes" :key="recipe.id" cols="12" lg="6">
        <nuxt-link :to="'/results/' + recipe.recipe_id">
          <v-card>
            <v-card-title primary-title>
              <h2>{{ recipe.title }}</h2>
            </v-card-title>
            <v-card-text>
              {{ recipe.summary }}
            </v-card-text>
          </v-card>
        </nuxt-link>
      </v-col>
    </v-row>
    <v-row v-else>
      <v-col>
        <v-card class="mx-auto px-4 py-4" max-width="600">
          <h1>Let's Get Started!</h1>
          <p>It looks like you don't have any recipes yet...</p>
          <v-btn type="link" color="info" to="/search">
            Search for Recipes
          </v-btn>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'MyRecipes',
  async asyncData({ $axios }) {
    const recipes = await $axios.$get('/pantry/myrecipes/')
    return { recipes }
  },

  head() {
    return {
      title: 'My Recipes',
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: 'View your recipes',
        },
      ],
    }
  },
}
</script>

<style lang="scss" scoped>
a {
  text-decoration: none;
}
</style>
