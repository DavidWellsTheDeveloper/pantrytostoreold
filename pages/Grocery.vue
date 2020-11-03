<template>
  <v-container>
    <v-row>
      <v-col class="text-center">
        <h1>Grocery List</h1>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'Grocery',
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
