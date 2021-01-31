<template>
  <v-container>
    <v-row>
      <v-col cols="12" class="text-center">
        <h1>Grocery List</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-dialog v-model="addDialog" max-width="700">
          <template v-slot:activator="{ on, attrs }">
            <v-btn text color="primary" v-bind="attrs" v-on="on">
              <v-icon>mdi-plus-circle-outline</v-icon>
            </v-btn>
          </template>

          <v-card>
            <v-card-title primary-title> Add Item To List </v-card-title>
            <v-card-text>
              <AddIngredientForm
                @ingredientAdded="
                  addDialog = false
                  getGroceryList()
                "
              />
            </v-card-text>
          </v-card>
        </v-dialog>
      </v-col>
    </v-row>
    <v-divider />
    <v-row>
      <v-col v-for="item in groceryList" :key="item.id" cols="12">
        <v-checkbox
          v-model="selected"
          :label="item.description"
          :value="item.id"
        ></v-checkbox>
      </v-col>
    </v-row>
    <v-row>
      <v-col class="text-left">
        <v-btn class="my-2" color="success" @click="checkAll()"
          >Check All Items</v-btn
        >
      </v-col>
      <v-spacer></v-spacer>
      <v-col class="text-right">
        <v-btn class="my-2" color="error" @click="clearChecked()"
          >Clear Checked Items</v-btn
        >
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'Grocery',
  data() {
    return {
      addDialog: false,
      validIngredientForm: false,
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
