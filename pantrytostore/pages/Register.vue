<template>
  <v-container grid-list-xs>
    <v-card class="mx-auto mt-5" max-width="600">
      <v-card-title>
        <h1 class="display-1 mx-auto">Register</h1>
      </v-card-title>
      <v-card-text>
        <v-form id="login-form" v-model="valid" @submit.prevent="onSubmit">
          <v-row>
            <v-col cols="12" lg="6">
              <v-text-field
                id="first-name-field"
                v-model="user.first_name"
                label="First Name"
                :rules="firstNameRules"
                prepend-icon="mdi-card-account-details"
              ></v-text-field>
            </v-col>
            <v-col cols="12" lg="6">
              <v-text-field
                id="last-name-field"
                v-model="user.last_name"
                label="Last Name"
                :rules="lastNameRules"
                prepend-icon="mdi-card-account-details"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-text-field
                id="username-field"
                v-model="user.username"
                label="username"
                :rules="usernameRules"
                prepend-icon="mdi-account-box"
              ></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field
                id="email-field"
                v-model="user.email"
                label="email"
                :rules="emailRules"
                prepend-icon="mdi-email"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <!-- <v-col cols="1">
              <v-tooltip bottom>
                <template v-slot:activator="{ on, attrs }">
                  <v-icon color="primary" dark v-bind="attrs" v-on="on">
                    mdi-information
                  </v-icon>
                </template>
                <span>
                  Password Rules:
                  <ul>
                    <li>Must be 8 characters</li>
                    <li>Must contain a special character</li>
                    <li>Must contain a number</li>
                  </ul>
                </span>
              </v-tooltip>
            </v-col> -->
            <v-col cols="12">
              <v-text-field
                id="password-field"
                v-model="user.password"
                label="password"
                hint="At least 8 characters, including at least 1 number and at least 1 special character."
                :rules="[
                  passwordRules.required,
                  passwordRules.min,
                  passwordRules.special,
                  passwordRules.number,
                ]"
                prepend-icon="mdi-lock"
                :type="showPassword ? 'text' : 'password'"
                :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append="showPassword = !showPassword"
              >
              </v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field
                id="password-confirm-field"
                v-model="passwordConfirm"
                label="confirm password"
                :rules="confirmPasswordRules"
                prepend-icon="mdi-lock-check"
                :type="showConfirmPassword ? 'text' : 'password'"
                :append-icon="showConfirmPassword ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append="showConfirmPassword = !showConfirmPassword"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row justify="space-between">
            <v-col>
              <v-btn color="error" type="link" to="/login">Cancel</v-btn>
            </v-col>
            <v-col class="text-right">
              <v-btn color="info" :disabled="!valid" type="submit">
                Register
              </v-btn>
            </v-col>
          </v-row>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
export default {
  auth: false,
  data() {
    return {
      valid: false,
      user: {
        username: null,
        password: null,
        email: null,
        first_name: null,
        last_name: null,
      },
      usernameRules: [
        (v) => !!v || 'Username is required',
        (v) =>
          /^([a-zA-Z0-9_-]){5,40}$/.test(v) ||
          'Username must be 5-40 characters, and may contain letters, numbers and the following symbols -_',
      ],
      firstNameRules: [(v) => !!v || 'First Name is required'],
      lastNameRules: [(v) => !!v || 'Last Name is required'],
      emailRules: [
        (v) => !!v || 'E-mail is required',
        (v) =>
          /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) ||
          'E-mail must be valid',
      ],
      passwordRules: {
        required: (v) => !!v || 'Password is required',
        min: (v) => (!!v && v.length >= 8) || 'Minimum 8 characters',
        special: (v) =>
          (!!v && /([!@#$%^&*)(+=._-])/.test(v)) ||
          'At least 1 special character is required. Available: !@#$%^&*)(+=._-',
        number: (v) =>
          (!!v && /([0-9])/.test(v)) || 'At least 1 number is required',
      },
      showPassword: false,
      passwordConfirm: null,
      showConfirmPassword: false,
      confirmPasswordRules: [
        (v) => !!v || 'Password confirmation is required',
        (v) => v === this.user.password || 'Passwords must match',
      ],
    }
  },
  methods: {
    onSubmit() {
      this.$axios.post('/user/create/', this.user).then((resp) => {
        // TODO confirm success before redirecting to login.
        this.$router.push({ name: 'Login' })
      })
    },
  },
  head() {
    return {
      title: 'Register',
      meta: [
        {
          hid: 'description',
          name: 'description',
          content:
            'Register for Pantry To Store. Search for and save recipes, manage grocery lists and more.',
        },
      ],
    }
  },
}
</script>

<style lang="scss" scoped></style>
