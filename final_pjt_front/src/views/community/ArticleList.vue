<template>
  <div>
    <div v-if="login" class="text-right mb-3">
      <router-link class="btn btn-light text-dark" :to="{ name: 'CreateArticle'}">리뷰 작성하기</router-link>
    </div>
    <div v-else class="text-right mb-3">
      <button type="button" class="btn btn-light" @click="videoPlay">리뷰 작성하기</button>
    </div>
    <Article
      v-for="(article, idx) in articles"
      :key="idx"
      :article="article"
    />
  </div>
</template>

<script>
import axios from 'axios'
import Article from '@/components/community/Article'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ArticleList',
  components: {
    Article,
  },
  data: function () {
    return {
      articles: [],
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    readArticles: function () {
      axios.get(`${SERVER_URL}/community/`, this.setToken())
        .then(response => this.articles = response.data)
        .catch(error => console.log(error))
    },
    videoPlay: function () {
      alert('로그인이 필요한 서비스입니다')
    },
  },
  created: function () {
    this.readArticles()
    const token = localStorage.getItem('jwt')
    if (token) {
      if (!this.login) {
        this.login = true
      }
    }
  }
}
</script>

<style>

</style>