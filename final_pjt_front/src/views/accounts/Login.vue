<template>
  <div class="jumbotron col-4">
    <h2>로그인</h2>
    <div class="form-group">
      <label for="username">사용자 ID</label>
      <input type="text" class="form-control" id="username" v-model="credentials.username" @keypress.enter="login">
    </div>
    <div class="form-group">
      <label for="password">비밀번호</label>
      <input type="password" class="form-control" id="password" v-model="credentials.password" @keypress.enter="login">
    </div>
    <div v-if="!errorCheckLogin" class="alert alert-danger" role="alert">
      ID 또는 비밀번호를 다시 확인해주세요.
    </div>
    <div class="text-right">
      <button @click="login" type="submit" class="btn btn-secondary">로그인</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      },
      errorCheckLogin: true,
    }
  },
  methods: {
    login: function () {
      axios.post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
        .then((res) => {
          // console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$router.push({ name: 'MovieList' })
        })
        .catch(() => {
          this.errorCheckLogin = false
        })
    }
  }
}
</script>