<template>
  <v-container>
    <v-row>
      <v-col cols="12" class="text-center">
        <h1>Grocery List</h1>
      </v-col>
      <v-col v-for="item in groceryList" :key="item.id" cols="12">
        <Ingredient :grocery-ingredient="item" class="my-0 py-0" />
      </v-col>
    </v-row>
    <v-row>
      <v-btn color="success" @click="checkAll()">Check All Items</v-btn>
      <v-spacer></v-spacer>
      <v-btn color="error" @click="clearChecked()">Clear Checked Items</v-btn>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'Grocery',
  data() {
    return {
      groceryList: null,
    }
  },
  mounted() {
    this.getGroceryList()
  },
  methods: {
    getGroceryList() {
      const urlPath = new URL('http://localhost:8000/pantry/grocery/')

      this.$axios.get(urlPath.href).then((response) => {
        this.groceryList = response.data
      })
    },
    clearChecked() {
      this.groceryList.forEach((item) => {
        if (item.completed) {
          const urlPath = new URL(
            'http://localhost:8000/pantry/grocery/' + item.id + '/'
          )

          this.$axios.delete(urlPath.href).then((response) => {
            this.getGroceryList()
          })
        }
      })
    },
    checkAll() {
      this.groceryList.forEach((item) => {
        if (!item.completed) {
          const urlPath = new URL(
            'http://localhost:8000/pantry/grocery/' + item.id + '/'
          )
          const data = {
            completed: true,
          }
          this.$axios.patch(urlPath.href, data).then((response) => {
            this.getGroceryList()
          })
        }
      })
    },
  },
  head() {
    return {
      title: 'Grocery List',
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: 'Add items to grocery list.',
        },
      ],
    }
  },
}
</script>

<style lang="scss" scoped></style>
