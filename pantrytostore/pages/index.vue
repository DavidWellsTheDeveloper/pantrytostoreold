<template>
  <v-container>
    <v-parallax
      dark
      src="/massimiliano-martini-copy-IeEFsajuORc-unsplash.jpg"
      width="100%"
    ></v-parallax>
    <v-row justify="center" align="center">
      <v-col cols="12" sm="8" md="6">
        <v-card color="info">
          <v-card-title class="headline text-center">
            <h3>Pantry To Store</h3>
          </v-card-title>
          <v-card-text>
            <p>
              <b>Pantry To Store</b> is an all-in-one food management solution.
              The goal is to make Pantry To Store the only application you need
              to find recipes and manage dietary plans and build a shopping
              list.
            </p>
            <p class="text-xs-right">
              <em><small>&mdash; Dave Wells</small></em>
            </p>
            <hr class="my-3" />
          </v-card-text>
          <v-card-title v-if="$auth.loggedIn" class="headline text-center">
            Welcome {{ $auth.user.first_name }}
          </v-card-title>
          <v-card-title v-else></v-card-title>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  auth: false,
  name: 'Home',
  head() {
    return {
      title: 'Home',
      meta: [
        {
          hid: 'description',
          name: 'description',
          content:
            'Pantry To Store is an all-in-one food management solution. ' +
            'The goal is to make Pantry To Store the only application you need to ' +
            'go from finding recipes and managing dietary plans to building your grocery list.',
        },
      ],
    }
  },
}
</script>
