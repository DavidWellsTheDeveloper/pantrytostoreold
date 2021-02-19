<template>
  <v-container grid-list-xs>
    <h1>New Recipe</h1>
    <v-row>
      <v-col>
        <v-text-field
          v-model="recipe.title"
          :rules="titleRules"
          label="Recipe Title"
        ></v-text-field>
        <v-textarea
          v-model="recipe.summary"
          outlined
          :rules="summaryRules"
          label="Recipe Summary"
        ></v-textarea>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-btn text color="success" @click="AddIngredient()">
          <v-icon>mdi-shaker-outline</v-icon> Add Ingredients
        </v-btn>
      </v-col>
    </v-row>
    <v-row
      v-for="(ingredient, index) in ingredients"
      :key="'ingredient' + index"
    >
      <v-col cols="12" sm="3" md="2">
        <v-text-field v-model="ingredient.amount" label="amount"></v-text-field>
      </v-col>
      <v-col cols="12" sm="4" md="3">
        <v-text-field v-model="ingredient.unit" label="unit"></v-text-field>
      </v-col>
      <v-col cols="12" sm="5" md="7">
        <v-text-field v-model="ingredient.name" label="name"></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-btn text color="success" @click="AddInstruction()">
          <v-icon>mdi-pot-mix-outline</v-icon> Add Instructions
        </v-btn>
      </v-col>
    </v-row>
    <v-row
      v-for="(instruction, index) in instructions"
      :key="'instruction' + index"
    >
      <v-col>
        <v-text-field
          v-model="instruction.instruction"
          label="Instruction"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-btn color="success" @click="CreateRecipe()">Create</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// import RecipeEdit from '../components/RecipeEdit.vue'
export default {
  name: 'CreateRecipe',
  // components: { RecipeEdit },
  data() {
    return {
      recipe: {
        title: null,
        summary: null,
        user: this.$auth.user.id,
        recipe_id: null,
      },
      ingredients: [],
      instructions: [],

      titleRules: [(value) => !!value || 'Title Required'],
      summaryRules: [(value) => !!value || 'Summary Required'],
    }
  },
  methods: {
    AddIngredient() {
      const ingredient = {
        name: 'New Ingredient',
        amount: null,
        unit: null,
      }
      this.ingredients.push(ingredient)
    },
    AddInstruction() {
      const length = this.instructions.length
      const instruction = {
        step: length + 1,
        instruction: 'Instruction',
      }
      this.instructions.push(instruction)
    },

    async CreateRecipe() {
      const payload = {
        title: this.recipe.title,
        summary: this.recipe.summary,
        user: this.recipe.user,
      }
      const response = await this.$axios.post('/pantry/myrecipes/', payload)
      await this.createChildren(response.data.recipe_id)
      this.$router.push(`/results/${response.data.recipe_id}/`)
    },

    createChildren(recipeId) {
      this.instructions.forEach((item, index) => {
        const instruction = {
          step: index + 1,
          instruction: item.instruction,
          recipe: recipeId,
        }
        this.$axios.post('/pantry/instructions/', instruction)
      })

      this.ingredients.forEach((item, index) => {
        const ingredient = {
          amount: item.amount,
          unit: item.unit,
          name: item.name,
          recipe: recipeId,
        }
        this.$axios.post('/pantry/ingredients/', ingredient)
      })
    },
  },
}
</script>

<style lang="scss" scoped></style>
