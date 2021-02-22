<template>
  <v-container>
    <v-row class="justify-space-around">
      <v-col cols="12" md="8" lg="6">
        <v-card shaped color="primary">
          <v-card-title primary-title class="justify-center">
            Would you rather add your own recipe?
          </v-card-title>
          <v-card-actions>
            <v-btn
              text
              class="mx-auto"
              color="success"
              :to="{ name: 'CreateRecipe' }"
            >
              Add Your Own Recipe
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-divider class="my-5"></v-divider>
        <h1>Import a recipe from another website</h1>
        <p>
          We will do our best to extract recipes from popular recipe websites.
          Just copy and paste the URL of a specific recipe from any popular
          recipe website. Recipe websites that seem to have success are:
        </p>
        <ul>
          <li>All Recipes</li>
          <li>etc...</li>
        </ul>
      </v-col>
    </v-row>

    <h2 class="text-center">Copy recipe URL</h2>
    <v-form id="searchForm" v-model="valid" @submit.prevent="extractRecipe()">
      <v-row>
        <v-col cols="12" lg="7">
          <v-text-field
            v-model="extractUrl"
            :rules="urlRules"
            label="Paste URL"
          ></v-text-field>
        </v-col>
        <v-col cols="12" lg="5">
          <v-btn color="success" :disabled="!valid" type="submit">
            Extract Recipe
          </v-btn>
        </v-col>
      </v-row>
    </v-form>
  </v-container>
</template>

<script>
// import RecipeSummary from '../components/RecipeSummary.vue'
export default {
  auth: false,
  name: 'AddRecipes',
  // components: { RecipeSummary },
  data() {
    return {
      valid: false,
      extractUrl: null,
      urlRules: [
        (value) => !!value || 'Required.',
        (value) => this.isValidHttpUrl(value) || 'URL is not valid',
      ],
    }
  },
  methods: {
    isURL(str) {
      let url

      try {
        url = new URL(str)
      } catch (_) {
        return false
      }

      return url.protocol === 'http:' || url.protocol === 'https:'
    },

    extractRecipe() {
      console.log('asdf')
    },

    isValidHttpUrl(string) {
      let url

      try {
        url = new URL(string)
      } catch (_) {
        return false
      }

      return url.protocol === 'http:' || url.protocol === 'https:'
    },
  },
  head() {
    return {
      title: 'Search Recipes',
      meta: [
        {
          hid: 'description',
          name: 'description',
          content:
            'Search for recipes to view. Filter recipies based on diet, ingredients, or nutrition. Save your favorite recipes for later.',
        },
      ],
    }
  },
}
</script>

<style lang="scss" scoped>
.v-card__text,
.v-card__title {
  word-break: normal; /* maybe !important  */
}
</style>
