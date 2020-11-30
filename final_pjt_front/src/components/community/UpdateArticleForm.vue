<template>
  <div class="jumbotron">
    <div class="form-group">
      <label for="title">제목: </label>
      <input class="form-control" type="text" id="title" v-model.trim="article.title" @keypress.enter="updateArticle">
      <br>
      <label for="content">내용: </label>
      <textarea class="form-control mb-3" name="" id="content" rows="10" v-model.trim="article.content" @keypress.enter="updateArticle"></textarea>
      <div class="text-right">
        <button class="btn btn-secondary text-white" @click="updateArticle">등록</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CreateArticleForm',
  data: function () {
    return {
      article: [],
    }
  },
  created: function () {
    this.readArticle()
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
    readArticle: function () {
      const articleId = this.$route.params.article_id
      axios.get(`${SERVER_URL}/community/${articleId}`, this.setToken())
        .then(response => {
          console.log(response)
          this.article = response.data
        })
        .catch(error => console.log(error))
    },
    updateArticle: function () {
      const articleItem = {
        title: this.article.title,
        content: this.article.content,
      }
      const articleId = this.$route.params.article_id
      axios.put(`${SERVER_URL}/community/${articleId}/`, articleItem, this.setToken())
        .then(() => this.$router.push({ name: 'ArticleDetail', params: {article_id: articleId} }))
        .catch(error => console.log(error))
    },
  }
}
</script>

<style>

</style>