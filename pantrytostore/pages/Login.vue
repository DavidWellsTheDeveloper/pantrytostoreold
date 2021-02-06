<template>
  <div>
    <v-card width="400" class="mx-auto mt-5">
      <v-card-title>
        <h1 class="display-1 mx-auto">Login</h1>
      </v-card-title>
      <v-card-text>
        <v-form id="login-form" v-model="valid" @submit.prevent="loginUser">
          <v-text-field
            id="username-field"
            v-model="login.username"
            label="username"
            :rules="rules_username"
            prepend-icon="mdi-account-circle"
          ></v-text-field>
          <v-text-field
            id="password-field"
            v-model="login.password"
            label="password"
            :rules="rules_password"
            prepend-icon="mdi-lock"
            :type="showPassword ? 'text' : 'password'"
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="showPassword = !showPassword"
          ></v-text-field>
          <v-row justify="space-between">
            <v-col>
              <v-btn color="info" :disabled="!valid" type="submit">
                Login
              </v-btn>
            </v-col>
            <v-col class="text-right">
              <v-btn type="link" to="/Register" color="success">Register</v-btn>
            </v-col>
          </v-row>
        </v-form>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  auth: false,
  name: 'Login',
  data() {
    return {
      valid: false,
      rules_username: [(value) => !!value || 'Required'],
      rules_password: [(value) => !!value || 'Required'],
      showPassword: false,
      login: {
        username: '',
        password: '',
      },
    }
  },
  methods: {
    loginUser() {
      this.$auth
        .loginWith('local', {
          data: this.login,
        })
        .then((resp) => {
          this.$auth.setToken('local', 'Bearer ' + resp.data.access)
          this.$auth.setRefreshToken('local', resp.data.refresh)
          this.$axios.setHeader('Authorization', 'Bearer ' + resp.data.access)
          this.$auth.ctx.app.$axios.setHeader(
            'Authorization',
            'Bearer ' + resp.data.access
          )
          if (resp.status === 200) this.$router.push({ name: 'index' })
        })
    },
  },
  head() {
    return {
      title: 'Login',
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: 'Login to manage your own recipes, food, and ingredients',
        },
      ],
    }
  },
}
</script>

<style lang="scss" scoped></style>
