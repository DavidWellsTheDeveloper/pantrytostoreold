<template>
  <v-container>
    <v-btn
      :color="editing ? 'error' : 'warning'"
      text
      @click="$emit('ToggleEditing')"
    >
      <v-icon>{{ editIcon }}</v-icon> {{ editText }}
    </v-btn>
    <v-form v-if="editing" v-model="valid">
      <v-row>
        <v-col cols="12" md="6">
          <v-text-field v-model="recipe.title" label="Title"></v-text-field>
        </v-col>
        <v-col cols="12">
          <v-textarea
            v-model="recipe.summary"
            outlined
            label="Summary"
          ></v-textarea>
        </v-col>
        <!-- <v-col
          v-for="ingredient in ingredients"
          :key="ingredient.ingredient_id"
          cols="12"
        >
          <IngredientEdit :ingredient="ingredient"></IngredientEdit>
        </v-col> -->
      </v-row>
      <v-row>
        <v-col>
          <v-btn color="success" @click="addIngredient()">Add Ingredient</v-btn>
        </v-col>
      </v-row>
      <v-btn color="success" :disabled="!valid" @click="updateRecipe()">
        Submit Changes
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
    ingredients: {
      type: Array,
      required: true,
    },
    instructions: {
      type: Array,
      required: true,
    },
    editing: Boolean,
  },
  data() {
    return {
      valid: false,
    }
  },
  computed: {
    editText() {
      return this.editing ? 'CANCEL' : 'EDIT TITLE & SUMMARY'
    },
    editIcon() {
      return this.editing ? 'mdi-cancel' : 'mdi-pencil'
    },
  },
  methods: {
    addIngredient() {
      const payload = {
        name: 'New Ingredient',
        amount: null,
        unit: null,
        recipe: this.recipe.recipe_id,
      }
      this.$axios.post('/pantry/ingredients/', payload)
    },
    updateRecipe() {
      const payload = {
        title: this.recipe.title,
        summary: this.recipe.summary,
        user: this.$auth.user.id,
      }
      this.$axios
        .put(`/pantry/myrecipes/${this.$route.params.id}/`, payload)
        .then((response) => {
          if (response.status === 200) {
            this.$emit('ToggleEditing')
          }
        })
    },
  },
}
</script>

<style lang="scss" scoped></style>
