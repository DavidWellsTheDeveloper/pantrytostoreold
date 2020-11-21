<template>
  <v-container>
    <v-parallax
      dark
      src="/massimiliano-martini-copy-IeEFsajuORc-unsplash.jpg"
      width="100%"
    ></v-parallax>
    <v-row justify="center" align="center">
      <v-col cols="12" sm="8" md="6">
        <div class="text-center">
          <logo />
          <vuetify-logo />
        </div>
        <v-card color="info">
          <v-card-title class="headline text-center">
            Pantry To Store
          </v-card-title>
          <v-card-text>
            <no-ssr>
              <p>
                <b>Pantry To Store</b> is an all-in-one food management
                solution. The goal is to make <b>Pantry To Store</b> the only
                application you need to go from finding recipes and managing
                dietary plans to building your grocery list.
              </p>
              <div class="text-xs-right">
                <em><small>&mdash; Dave Wells</small></em>
              </div>
              <hr class="my-3" />
            </no-ssr>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Logo from '~/components/Logo.vue'
import VuetifyLogo from '~/components/VuetifyLogo.vue'

export default {
  components: {
    Logo,
    VuetifyLogo,
  },
  head() {
    return {
      title: 'Home',
    }
  },
}
</script>
