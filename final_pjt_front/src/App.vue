<template>
  <div id="app">
    <div class="d-flex justify-content-between align-items-center m-2 mx-3">
      <h2>Episode 0</h2>
      <div class="text-right" v-if="login">
        <router-link class="text-decoration-none text-dark" @click.native="logout" to="#"><strong>로그아웃</strong></router-link>
      </div>
      <div class="text-right" v-else>
        <router-link class="text-decoration-none text-dark" :to="{ name: 'Signup' }"><strong>회원가입</strong></router-link> |
        <router-link class="text-decoration-none text-dark" :to="{ name: 'Login' }"><strong>로그인</strong></router-link> 
      </div>
    </div>
    <Navbar class="mb-3" />
    <router-view class="container" @login="login = true" :login="login"/>
  </div>
</template>

<script>
import Navbar from '@/components/app/Navbar'
export default {
  name: 'App',
  data: function () {
    return {
      login: false,
    }
  },
  components: {
    Navbar,
  },
  methods: {
    logout: function () {
      localStorage.removeItem('jwt')
      this.login = false
      this.$router.push({ name: 'Login' })
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      if (!this.login) {
        this.login = true
        // this.$router.push({ name: 'MovieList' })
      }
    } else {
      // this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<style>
#app {
  user-select: none;
}
</style>