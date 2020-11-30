<template>
  <div class="jumbotron col-4">
    <h2>회원가입</h2>
    <div class="form-group">
      <label for="username">사용자 ID</label>
      <input type="text" class="form-control" id="username" v-model="credentials.username" @keypress.enter="signup">
    </div>
    <div class="form-group">
      <label for="password">비밀번호</label>
      <input type="password" class="form-control" id="password" v-model="credentials.password" @keypress.enter="signup">
    </div>
    <div class="form-group">
      <label for="passwordConfirmation">비밀번호 확인</label>
      <input type="password" class="form-control" id="passwordConfirmation" v-model="credentials.passwordConfirmation" @keypress.enter="signup">
    </div>
    <div v-if="errorMessage !== ''" class="alert alert-danger" role="alert">
      {{ errorMessage }}
    </div>
    <div class="text-right">
      <button @click="signup" type="submit" class="btn btn-secondary">가입 완료</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Singup',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
      },
      errorMessage: '',
    }
  },
  methods: {
    signup: function () {
      axios.post(`${SERVER_URL}/accounts/signup/`, this.credentials)
        .then((res) => {
          console.log(res)
          if (res.status === 201) {
            this.login()
          }
        })
        .catch((error) => {
          this.errorMessage = error.response.data
          console.log(error.response.data)
        })
    },
    login: function () {
      axios.post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
        .then((res) => {
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$router.push({ name: 'ArticleList' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
  }
}
</script>
