<template>
  <v-form v-model="valid" @submit.prevent="addIngredient()">
    <v-text-field
      ref="ingredient"
      v-model="ingredient.description"
      label="Item"
      :rules="descriptionRules"
    ></v-text-field>
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
  mounted() {
    this.focusInput()
  },
  methods: {
    addIngredient() {
      this.$axios.post('/pantry/grocery/', this.ingredient).then((resp) => {
        if (resp.status === 201) {
          this.ingredient.description = null
          this.$emit('ingredientAdded')
        }
      })
    },
    focusInput() {
      console.log('Focus Input')
      this.$nextTick(() => this.$refs.ingredient.focus())
    },
  },
}
</script>

<style lang="scss" scoped></style>
