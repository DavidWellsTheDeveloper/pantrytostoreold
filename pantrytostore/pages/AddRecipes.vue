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
          <!-- <v-btn color="success" disabled type="submit">
            This feature is currently in development
          </v-btn> -->
        </v-col>
      </v-row>
    </v-form>
    <v-card v-if="recipe">
      <v-card-title primary-title>
        <v-img :src="recipe.image.url"></v-img>
        {{ recipe.headline }}
      </v-card-title>
      <v-card-text>
        {{ recipe.description }}
        <v-divider></v-divider>
        <v-list shaped>
          <v-subheader>Ingredients</v-subheader>
          <v-list-item-group>
            <v-list-item
              v-for="(ingredient, index) in ingredients"
              :key="index"
              v-html="ingredient"
            >
            </v-list-item>
          </v-list-item-group>
          <v-subheader>Instructions</v-subheader>
          <v-list-item-group>
            <v-list-item
              v-for="(instruction, index) in instructions"
              :key="index"
            >
              {{ instruction.text }}
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-card-text>
      <v-card-actions v-if="recipe">
        <v-btn color="success" :disabled="!validRecipe" @click="CreateRecipe()">
          Save Recipe
        </v-btn>
      </v-card-actions>
    </v-card>
    <v-alert
      v-else
      v-model="recipeNotFound"
      border="left"
      close-text="Close Alert"
      color="deep-purple accent-4"
      dark
      dismissible
    >
      Sorry, but we were unable to extract the website. Please try another.
    </v-alert>
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
      recipe: null,
      urlRules: [
        (value) => !!value || 'Required.',
        (value) => this.isValidHttpUrl(value) || 'URL is not valid',
      ],
      recipeNotFound: false,
    }
  },

  computed: {
    ingredients() {
      return this.recipe.recipeIngredient
    },
    instructions() {
      if (typeof this.recipe.recipeInstructions !== 'string') {
        return this.recipe.recipeInstructions
      } else {
        const instructionsObj = { text: this.recipe.recipeInstructions }
        const arrayOfOne = []
        arrayOfOne.push(instructionsObj)
        return arrayOfOne
      }
    },
    validRecipe() {
      console.log('Ingredients' + typeof this.ingredients)
      if (typeof this.ingredients !== 'object') {
        return false
      }
      console.log('Instructions' + typeof this.instructions)
      if (typeof this.instructions !== 'object') {
        return false
      }
      return true
    },
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

    async extractRecipe() {
      await this.$axios
        .get(`/pantry/extractrecipe/?url=${this.extractUrl}`)
        .then((response) => {
          console.log(response)
          if (response.data !== 'Recipe data not found') {
            this.recipeNotFound = false
            this.recipe = response.data
          } else {
            this.recipe = null
            this.recipeNotFound = true
          }
        })
        .catch((err) => {
          console.log(err)
        })
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

    async CreateRecipe() {
      const payload = {
        title: this.recipe.headline,
        summary: this.recipe.description,
        user: this.$auth.user.id,
      }
      const response = await this.$axios.post('/pantry/myrecipes/', payload)
      await this.createChildren(response.data.recipe_id)
      this.$router.push(`/results/${response.data.recipe_id}/`)
    },

    createChildren(recipeId) {
      this.instructions.forEach((item, index) => {
        const instruction = {
          step: index + 1,
          instruction: item.text,
          recipe: recipeId,
        }
        this.$axios.post('/pantry/instructions/', instruction)
      })

      this.ingredients.forEach((item, index) => {
        const ingredient = {
          name: item,
          recipe: recipeId,
        }
        this.$axios.post('/pantry/ingredients/', ingredient)
      })
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
