<template>
  <nuxt-link :to="'/results/' + result.id">
    <v-card max-width="375" elevation="5">
      <v-img :src="result.image"></v-img>
      <v-card-title>{{ result.title }}</v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="12">
            <v-chip>Likes: {{ result.aggregateLikes }}</v-chip>
          </v-col>
          <v-col cols="12">
            <v-divider class="my-3"></v-divider>
            <p v-html="result.summary"></p>
            <v-divider class="my-3"></v-divider>
          </v-col>
        </v-row>
        <v-row>
          <ResultChips :result="result" />
        </v-row>
      </v-card-text>
    </v-card>
  </nuxt-link>
</template>

<script>
import ResultChips from '@/components/ResultChips.vue'
export default {
  components: {
    ResultChips,
  },
  props: {
    result: {
      type: Object,
      required: true,
    },
  },
}
</script>

<style lang="scss" scoped>
a {
  text-decoration: none;
}
</style>
