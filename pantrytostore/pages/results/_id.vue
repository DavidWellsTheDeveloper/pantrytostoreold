<template>
  <v-container v-if="!!recipe">
    <v-row class="text-center">
      <v-col cols="12">
        <h1>{{ recipe.title }}</h1>
      </v-col>
    </v-row>
    <RecipeEdit
      v-if="recipe && instructions && ingredients"
      :editing="editing"
      :recipe="recipe"
      :ingredients="ingredients"
      :instructions="instructions"
      @ToggleEditing="editing = !editing"
    ></RecipeEdit>
    <v-row>
      <v-col cols="12">
        <v-tabs v-model="tab">
          <v-tab v-for="item in tabs" :key="item">
            {{ item }}
          </v-tab>
          <v-tab-item>
            <ViewIngredients
              :ingredients="ingredients"
              @ingredientUpdated="$fetch()"
            ></ViewIngredients>
          </v-tab-item>
          <v-tab-item>
            <v-card>
              <v-card-title> Instructions: </v-card-title>
              <v-card-text>
                <ol>
                  <li
                    v-for="instruction in instructions"
                    :key="instruction.instruction_id"
                  >
                    {{ instruction.instruction }}
                  </li>
                </ol>
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
  async fetch() {
    this.ingredients = await this.$axios.$get(
      `/pantry/ingredients/?recipe=${this.$route.params.id}`
    )
    this.instructions = await this.$axios.$get(
      `/pantry/instructions/?recipe=${this.$route.params.id}`
    )
  },
  async asyncData({ params, $axios }) {
    const recipe = await $axios.$get(`/pantry/myrecipes/${params.id}/`)
    return { recipe }
  },
  data() {
    return {
      // recipe (via asyncData)
      ingredients: null,
      instructions: null,
      editing: false,
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
  methods: {
    addIngredients() {
      this.ingredientsSelected.forEach((ingredient) => {
        const data = {
          ingredient_id: ingredient.ingredient_id,
          amount: ingredient.amount,
          unit: ingredient.unit,
          description: ingredient.originalString,
          completed: false,
          user: this.$auth.user.id,
        }
        if (ingredient != null) {
          this.$axios.post('/pantry/grocery/', data).then((response) => {
            this.dialog = false
          })
        }
      })
    },
  },
  head() {
    return {
      title: this.recipe.title,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content:
            'Pantry To Store is an all-in-one food management solution. ' +
            'The goal is to make Pantry To Store the only application you need to ' +
            'go from finding recipes and managing dietary plans to building your grocery list.',
        },
      ],
    }
  },
}
</script>

<style lang="scss" scoped></style>
