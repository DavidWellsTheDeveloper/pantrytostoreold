<template>
  <v-container>
    <v-row>
      <v-col cols="12" class="text-center">
        <h1>Find Recipes</h1>

        <v-form
          id="searchForm"
          v-model="valid"
          @submit.prevent="searchRecipes(0)"
        >
          <v-row>
            <h3>Search:</h3>
            <v-col cols="12" xl="4">
              <v-text-field
                v-model="query"
                label="Search Recipes"
                :rules="queryRules"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <h3>Options:</h3>
            <v-col>
              <v-checkbox
                v-model="recipeInfo"
                label="Include Recipe Information"
                color="orange darken-2"
              >
              </v-checkbox>
              <v-checkbox
                v-model="recipeNutrition"
                label="Include Recipe Nutrition"
                color="orange darken-2"
              >
              </v-checkbox>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-btn color="success" type="submit" :disabled="!valid">
                Search
              </v-btn>
            </v-col>
          </v-row>
        </v-form>

        <v-row v-if="!!searchResults">
          <v-col
            v-for="result in searchResults.results"
            :key="result.id"
            cols="12"
            xl="3"
            lg="4"
            md="6"
          >
            <recipe-summary :result="result" />
          </v-col>
        </v-row>

        <v-row>
          <v-col v-if="currentPage > 1">
            <v-btn @click="previousPage" @:click="$vuetify.goTo('#searchForm')">
              Previous Page
            </v-btn>
          </v-col>
          <v-col v-if="totalPages > currentPage">
            <v-btn @click="nextPage" @:click="$vuetify.goTo('#searchForm')">
              Next Page
            </v-btn>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import RecipeSummary from '../components/RecipeSummary.vue'
export default {
  auth: false,
  name: 'Search',
  components: { RecipeSummary },
  data() {
    return {
      valid: false,
      searchResults: null,
      query: null,
      recipeInfo: true,
      recipeNutrition: false,
      queryRules: [(value) => !!value || 'Required'],
    }
  },
  computed: {
    totalPages() {
      if (this.searchResults) {
        return Math.ceil(this.searchResults.totalResults / 10.0)
      } else {
        return 0
      }
    },
    currentPage() {
      if (this.searchResults) {
        return Math.ceil(this.searchResults.offset / 10.0) + 1
      } else {
        return 0
      }
    },
  },
  methods: {
    async searchRecipes(offset) {
      const params = {
        apiKey: '5e819bee625f4a3b8572dde36611f257',
        query: this.query,
        addRecipeInformation: this.recipeInfo,
        addRecipeNutrition: this.recipeNutrition,
        offset: String(offset),
      }

      this.searchResults = await this.$axios.$get('/pantry/search/', {
        params,
      })
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.searchRecipes(this.searchResults.offset + 10)
        this.top()
      }
    },
    previousPage() {
      if (this.currentPage > 1) {
        this.searchRecipes(this.searchResults.offset - 10)
        this.top()
      }
    },
    top() {
      window.scrollTo({
        top: 0,
        left: 0,
        behavior: 'smooth',
      })
    },
  },
  head() {
    return {
      title: 'Search For Recipes',
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
