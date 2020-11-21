<template>
  <v-switch @change="toggleDarkTheme()">
    <template v-slot:label>
      <v-icon>mdi-theme-light-dark</v-icon>
    </template>
  </v-switch>
</template>

<script>
export default {
  methods: {
    toggleDarkTheme() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark
    },
  },
}
</script>

<style lang="scss" scoped></style>
