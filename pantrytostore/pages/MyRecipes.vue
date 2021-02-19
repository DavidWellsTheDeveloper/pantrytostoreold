<template>
  <v-container>
    <v-row class="mb-5">
      <v-col>
        <v-card class="mx-auto px-4 py-4" max-width="600">
          <h1>Add a new recipe</h1>
          <v-btn block color="info" to="/createrecipe"> Add a recipe </v-btn>
        </v-card>
      </v-col>
    </v-row>
    <h1>My Recipes</h1>
    <v-row v-if="!!recipes">
      <v-col v-for="recipe in recipes" :key="recipe.id" cols="12" md="6" lg="4">
        <v-card>
          <nuxt-link :to="'/results/' + recipe.recipe_id">
            <v-card-title primary-title>
              <h2>{{ recipe.title }}</h2>
            </v-card-title>
            <v-card-text>
              {{ recipe.summary }}
            </v-card-text>
          </nuxt-link>
          <v-card-actions>
            <v-btn text color="amber">
              <v-icon>mdi-star{{ true ? '-outline' : '' }}</v-icon>
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn text color="error" @click="dialog = true"
              >Delete Recipe</v-btn
            >
            <v-dialog
              v-model="dialog"
              dismissable
              persistent
              :overlay="false"
              max-width="500px"
              transition="dialog-transition"
            >
              <v-card>
                <v-card-title primary-title> Are you sure? </v-card-title>
                <v-card-actions>
                  <v-btn text color="error" @click="dialog = false">
                    Cancel
                  </v-btn>
                  <v-spacer></v-spacer>
                  <v-btn
                    text
                    color="success"
                    @click="
                      deleteRecipe(recipe.recipe_id)
                      dialog = false
                    "
                  >
                    Yes Remove Recipe
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-card-actions>
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
  data() {
    return {
      dialog: false,
    }
  },
  methods: {
    async deleteRecipe(id) {
      await this.$axios.delete(`/pantry/myrecipes/${id}/`)
      this.recipes = await this.$axios.$get('/pantry/myrecipes/')
    },
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
  color: inherit !important;
  // cursor: pointer;
}
</style>
