<template>
  <v-container grid-list-xs>
    <h1>Create Recipe</h1>
    <v-form v-model="valid" @submit.prevent="SubmitRecipe()">
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
      <v-btn color="success" type="submit" :disabled="!valid">
        {{ recipe.recipe_id ? 'Update' : 'Create' }}
      </v-btn>
    </v-form>
  </v-container>
</template>

<script>
export default {
  props: {
    recipe: {
      type: Object,
      required: true,
    },
  },
  async fetch() {
    this.ingredients = await this.$axios.$get(
      `/pantry/ingredients/?recipe=${this.$route.params.id}`
    )
    this.instructions = await this.$axios.$get(
      `/pantry/instructions/?recipe=${this.$route.params.id}`
    )
  },
  data() {
    return {
      valid: false,
      titleRules: [(value) => !!value || 'Title Required'],
      summaryRules: [(value) => !!value || 'Summary Required'],
      ingredients: [],
      instructions: [],
    }
  },

  methods: {
    async SubmitRecipe() {
      if (this.recipe.recipe_id === null) {
        const recipePayload = {
          title: this.recipe.title,
          summary: this.recipe.summary,
          user: this.recipe.user,
        }
        const response = await this.$axios.post(
          '/pantry/myrecipes/',
          recipePayload
        )
        this.recipe = response.data
      } else {
        const recipePayload = {
          recipe_id: this.recipe.recipe_id,
          title: this.recipe.title,
          summary: this.recipe.summary,
          user: this.recipe.user,
        }
        await this.$axios.$put(
          `/pantry/myrecipes/${this.recipe.recipe_id}`,
          recipePayload
        )
      }
    },
  },
}
</script>

<style lang="scss" scoped></style>
