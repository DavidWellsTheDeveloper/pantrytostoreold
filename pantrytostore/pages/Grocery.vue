<template>
  <v-container>
    <v-row>
      <v-col cols="12" class="text-center">
        <h1>Grocery List</h1>
      </v-col>
      <v-col v-for="item in groceryList" :key="item.id" cols="12">
        <v-checkbox
          v-model="selected"
          :label="item.description"
          :value="item.id"
        ></v-checkbox>
      </v-col>
    </v-row>
    <v-row>
      <v-btn class="my-2" color="success" @click="checkAll()"
        >Check All Items</v-btn
      >
    </v-row>
    <v-row>
      <v-btn class="my-2" color="error" @click="clearChecked()"
        >Clear Checked Items</v-btn
      >
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'Grocery',
  data() {
    return {
      groceryList: null,
      selected: [],
    }
  },
  mounted() {
    this.getGroceryList()
  },
  methods: {
    getGroceryList() {
      this.$axios.get('/pantry/grocery/').then((response) => {
        this.groceryList = response.data
      })
    },
    clearChecked() {
      this.selected.forEach((item) => {
        this.$axios
          .$delete('/pantry/grocery/' + item + '/')
          .then((response) => {
            this.getGroceryList()
          })
      })
    },
    checkItem(item) {
      if (!this.selected.includes(item.id)) {
        this.selected.push(item.id)
      }
    },
    checkAll() {
      this.groceryList.forEach((item) => {
        this.checkItem(item)
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
