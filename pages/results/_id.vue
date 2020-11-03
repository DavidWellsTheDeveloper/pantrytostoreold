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
            </v-card>
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
import axios from 'axios'
export default {
  name: 'RecipeDetails',
  data() {
    return {
      recipe: null,
      tab: null,
      tabs: ['ingredients', 'directions'],
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

      axios.get(urlPath.href).then((response) => {
        this.recipe = response.data
      })
    },
  },
}
</script>

<style lang="scss" scoped></style>
