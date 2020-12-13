<template>
  <v-container>
    <h1>My Recipes</h1>
    <v-row>
      <v-col v-for="recipe in myRecipes" :key="recipe.id" cols="12" lg="6">
        <nuxt-link :to="'/results/' + recipe.id">
          <v-card>
            <v-img
              :src="recipe.image"
              width="200"
              class="float-left mx-5"
            ></v-img>
            <v-card-title primary-title>
              <h2>{{ recipe.title }}</h2>
            </v-card-title>
            <v-card-text>
              <ResultChips :result="recipe" />
            </v-card-text>
          </v-card>
        </nuxt-link>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ResultChips from '@/components/ResultChips.vue'
export default {
  name: 'MyRecipes',
  components: {
    ResultChips,
  },
  data() {
    return {
      myRecipes: {},
    }
  },
  mounted() {
    this.getMyRecipes()
  },
  methods: {
    async getMyRecipes() {
      const response = await this.$axios.get('/pantry/myrecipes/')
      this.myRecipes = response.data
    },
  },
}
</script>

<style lang="scss" scoped>
a {
  text-decoration: none;
}
</style>
