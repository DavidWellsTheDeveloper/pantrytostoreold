<template>
  <v-container>
    <v-row>
      <v-btn
        :color="editing ? 'error' : 'warning'"
        text
        small
        @click="editing = !editing"
      >
        <v-icon>
          {{ editIcon }}
        </v-icon>
      </v-btn>
      <v-col v-if="editing">
        <v-text-field v-model="editAmount" label="Amount"></v-text-field>
        <v-text-field v-model="editUnit" label="Unit"></v-text-field>
        <v-text-field v-model="editName" label="Ingredient"></v-text-field>
        <v-btn color="success" text @click="updateIngredient()">
          <v-icon>mdi-content-save-outline</v-icon>
        </v-btn>
      </v-col>
      <v-col v-else>
        {{ fullIngredient }}
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: {
    ingredient: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      editing: false,
      editAmount: this.ingredient.amount,
      editUnit: this.ingredient.unit,
      editName: this.ingredient.name,
    }
  },
  computed: {
    editIcon() {
      return this.editing ? 'mdi-cancel' : 'mdi-pencil'
    },
    fullIngredient() {
      let ingredientStr = ''
      if (this.ingredient.amount) {
        ingredientStr += `${this.ingredient.amount} `
      }
      if (this.ingredient.unit) {
        ingredientStr += `${this.ingredient.unit} `
      }
      if (this.ingredient.name) {
        ingredientStr += `${this.ingredient.name}`
      }
      return ingredientStr
    },
  },
  methods: {
    updateIngredient() {
      const payload = {
        ingredient_id: this.ingredient.ingredient_id,
        name: this.editName,
        amount: this.editAmount,
        unit: this.editUnit,
        recipe: this.$route.params.id,
      }
      this.$axios
        .put(`/pantry/ingredients/${this.ingredient.ingredient_id}/`, payload)
        .then((response) => {
          if (response.status === 200) {
            this.editing = false
            this.$emit('ingredientUpdated')
          }
        })
    },
  },
}
</script>

<style lang="scss" scoped></style>
