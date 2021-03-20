<template>
  <v-container>
    <v-card>
      <v-card-title>Ingredients:</v-card-title>
      <v-card-text>
        <ul>
          <IngredientEdit
            v-for="ingredient in ingredients"
            :key="ingredient.ingredient_id"
            :ingredient="ingredient"
            @ingredientUpdated="$emit('ingredientUpdated')"
          ></IngredientEdit>
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
    <v-dialog v-model="dialog" max-width="800" :opacity="opacity" scrollable>
      <v-card>
        <v-card-title primary-title>Add Ingredients:</v-card-title>
        <v-card-text>
          <v-form @submit.prevent="addIngredients()">
            <v-checkbox
              v-for="(ingredient, index) in ingredients"
              :key="ingredient.ingredient_id"
              v-model="ingredientsSelected[index]"
              :label="ingredient.name"
              :value="ingredient"
            ></v-checkbox>
            <v-row>
              <v-btn type="submit" color="success"> Add Selected </v-btn>
              <v-spacer></v-spacer>
              <v-btn color="error" @click="dialog = false"> Cancel </v-btn>
            </v-row>
          </v-form>
        </v-card-text>
      </v-card>
    </v-dialog>
    <v-alert :value="alert" dismissible dark type="success">
      Your items were successfully added to your
      <v-btn color="secondary" text to="/Grocery/">
        <v-icon>mdi-cart-variant</v-icon>Grocery List</v-btn
      >.
    </v-alert>
  </v-container>
</template>

<script>
export default {
  props: {
    ingredients: {
      type: Array,
      default: Array,
    },
  },
  data() {
    return {
      ingredientsSelected: [],
      dialog: false,
      opacity: 0.5,
      alert: false,
    }
  },
  methods: {
    addIngredients() {
      this.ingredientsSelected.forEach((ingredient) => {
        const payload = {
          ingredient_id: ingredient.ingredient_id,
          amount: ingredient.amount,
          unit: ingredient.unit,
          description: ingredient.name,
          user: this.$auth.user.id,
        }
        this.$axios.post('/pantry/grocery/', payload).then((resp) => {
          if (resp.status === 201) {
            this.dialog = false
            this.alert = true
          }
        })
      })
    },
  },
}
</script>

<style lang="scss" scoped></style>
