<template>
  <v-container v-if="!!recipe">
    <v-row class="text-center">
      <v-spacer></v-spacer>
      <v-col>
        <v-img max-width="750" :src="recipe.image"></v-img>
      </v-col>
      <v-spacer></v-spacer>
      <v-col cols="12">
        <h1>{{ recipe.title }}</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-btn color="primary" @click="SaveRecipe">Save Recipe</v-btn>
      </v-col>
      <v-col v-if="already_saved">
        <h3>You've already saved this recipe!</h3>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-alert
          v-model="saved_alert"
          border="left"
          close-text="Close Alert"
          color="deep-purple accent-4"
          dark
          dismissible
        >
          Recipe Saved!
        </v-alert>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-tabs v-model="tab">
          <v-tab v-for="item in tabs" :key="item">
            {{ item }}
          </v-tab>
          <v-tab-item>
            <v-card>
              <v-card-title>Ingredients:</v-card-title>
              <v-card-text>
                <ul>
                  <li
                    v-for="ingredient in recipe.extendedIngredients"
                    :key="ingredient.id"
                  >
                    {{ ingredient.amount }} {{ ingredient.unit }}
                    {{ ingredient.name }}
                  </li>
                </ul>
              </v-card-text>
              <v-btn
                v-if="$auth.loggedIn"
                color="info"
                class="mx-3 my-3"
                @click="dialog = !dialog"
              >
                Add Ingredients to Grocery List
              </v-btn>
            </v-card>
            <v-dialog
              v-model="dialog"
              max-width="800"
              :opacity="opacity"
              scrollable
            >
              <v-card>
                <v-card-title primary-title>Add Ingredients:</v-card-title>
                <v-card-text>
                  <v-form @submit.prevent="addIngredients()">
                    <v-checkbox
                      v-for="(ingredient, index) in recipe.extendedIngredients"
                      :key="ingredient.id"
                      v-model="ingredientsSelected[index]"
                      :label="ingredient.originalString"
                      :value="ingredient"
                    ></v-checkbox>
                    <v-row>
                      <v-btn type="submit" color="success">
                        Add Selected
                      </v-btn>
                      <v-spacer></v-spacer>
                      <v-btn color="error" @click="dialog = false">
                        Cancel
                      </v-btn>
                    </v-row>
                  </v-form>
                </v-card-text>
              </v-card>
            </v-dialog>
          </v-tab-item>
          <v-tab-item>
            <v-card>
              <v-card-title> Instructions: </v-card-title>
              <v-card-text>
                <section
                  v-for="(instruction, index) in recipe.analyzedInstructions"
                  :key="index"
                >
                  <h4 v-if="instruction.name">{{ instruction.name }}</h4>
                  <ol>
                    <li v-for="step in instruction.steps" :key="step.number">
                      {{ step.step }}
                    </li>
                  </ol>
                </section>
              </v-card-text>
            </v-card>
          </v-tab-item>
        </v-tabs>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'RecipeDetails',
  data() {
    return {
      recipe: null,
      tab: null,
      tabs: ['ingredients', 'directions'],
      saved_alert: false,
      already_saved: false,
      // overlay data elements
      opacity: 0.5,
      dialog: false,
      ingredientsSelected: [],
    }
  },
  computed: {
    id() {
      return this.$route.params.id
    },
  },
  mounted() {
    this.getRecipe()
  },
  methods: {
    getRecipe() {
      const urlPath = new URL(
        'https://api.spoonacular.com/recipes/' + this.id + '/information'
      )
      urlPath.searchParams.append('apiKey', '5e819bee625f4a3b8572dde36611f257')
      urlPath.searchParams.append('includeNutrition', false)

      this.$axios.get(urlPath.href).then((response) => {
        this.recipe = response.data
      })
    },
    SaveRecipe() {
      const urlPath = new URL('http://localhost:8000/pantry/myrecipes/')
      const data = {
        recipe_id: this.id,
        user: this.$auth.user.id,
      }

      this.$axios
        .post(urlPath.href, data)
        .then((response) => {
          this.saved_alert = true
        })
        .catch((err) => {
          if (err.status === 500) {
            this.already_saved = true
          }
        })
    },
    addIngredients() {
      const urlPath = new URL('http://localhost:8000/pantry/grocery/')
      this.ingredientsSelected.forEach((ingredient) => {
        const data = {
          ingredient_id: ingredient.id,
          amount: ingredient.amount,
          unit: ingredient.unit,
          description: ingredient.originalString,
          completed: false,
          user: this.$auth.user.id,
        }
        if (ingredient != null) {
          this.$axios.post(urlPath.href, data).then((response) => {
            this.dialog = false
          })
        }
      })
    },
  },
}
</script>

<style lang="scss" scoped></style>
