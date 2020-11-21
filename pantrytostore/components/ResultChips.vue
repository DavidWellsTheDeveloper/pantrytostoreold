<template>
  <v-chip-group column>
    <v-chip v-if="result.readyInMinutes">
      <v-icon>mdi-timer-sand</v-icon>
      {{ result.readyInMinutes }}
    </v-chip>
    <v-chip v-if="result.vegitarian"> Vegitarian </v-chip>
    <v-chip v-if="result.healthScore">
      Health Score: {{ result.healthScore }}
    </v-chip>
    <v-chip v-if="result.weightWatcherSmartPoints">
      Weight Watcher Pts: {{ result.weightWatcherSmartPoints }}
    </v-chip>
  </v-chip-group>
</template>

<script>
export default {
  name: 'ResultChips',
  props: {
    result: {
      type: Object,
      required: true,
    },
  },
}
</script>

<style lang="scss" scoped></style>
