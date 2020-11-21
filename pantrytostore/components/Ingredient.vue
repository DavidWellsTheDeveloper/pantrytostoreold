<template>
  <v-checkbox
    v-model="value"
    :label="groceryIngredient.description"
    :value="groceryIngredient.completed"
    @change="checkboxUpdated"
  ></v-checkbox>
</template>

<script>
export default {
  props: {
    groceryIngredient: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      ingredientInfo: null,
      value: this.groceryIngredient.completed,
    }
  },
  mounted() {
    // this.getIngredientInfo()
  },
  methods: {
    getIngredientInfo() {
      const urlPath = new URL(
        'https://api.spoonacular.com/food/ingredients/' +
          this.groceryIngredient.ingredient_id +
          '/information'
      )
      urlPath.searchParams.append('apiKey', '5e819bee625f4a3b8572dde36611f257')

      this.$axios.get(urlPath.href).then((response) => {
        this.ingredientInfo = response.data
      })
    },
    checkboxUpdated(newValue) {
      if (newValue == null) {
        newValue = false
      }
      const urlPath = new URL(
        'http://localhost:8000/pantry/grocery/' +
          this.groceryIngredient.id +
          '/'
      )
      const data = {
        completed: newValue,
      }
      this.$axios.patch(urlPath.href, data).then((response) => {})
    },
  },
}
</script>

<style lang="scss" scoped></style>
