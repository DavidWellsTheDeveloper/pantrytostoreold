<template>
  <v-form v-model="valid" @submit.prevent="addIngredient()">
    <v-text-field
      v-model="ingredient.description"
      label="Item"
      :rules="descriptionRules"
    ></v-text-field>
    <!-- <v-text-field
      v-model="ingredient.amount"
      label="Amount"
      type="number"
    ></v-text-field>
    <v-text-field v-model="ingredient.unit" label="Unit"></v-text-field> -->
    <v-btn color="success" type="submit" :disabled="!valid"> Submit </v-btn>
  </v-form>
</template>

<script>
export default {
  data() {
    return {
      valid: false,
      ingredient: {
        ingredient_id: null,
        amount: null,
        unit: null,
        description: null,
        user: this.$auth.user.id,
      },
      descriptionRules: [(value) => !!value || 'Required'],
    }
  },
  methods: {
    addIngredient() {
      this.$axios.post('/pantry/grocery/', this.ingredient).then((resp) => {
        if (resp.status === 201) {
          this.$emit('ingredientAdded')
        }
      })
    },
  },
}
</script>

<style lang="scss" scoped></style>
