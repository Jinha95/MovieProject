<template>
  <div class="jumbotron">
    <div class="form-group">
      <label for="title">제목: </label>
      <input class="form-control" type="text" id="title" v-model.trim="title" @keypress.enter="writeArticle">
      <br>
      <label for="content">내용: </label>
      <textarea class="form-control mb-3" name="" id="content" rows="10" v-model.trim="content" @keypress.enter="writeArticle"></textarea>
      <div class="text-right">
        <button class="btn btn-secondary text-white" @click="writeArticle">등록</button>
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
      title: '',
      content: '',
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
    writeArticle: function () {
      const articleItem = {
        title: this.title,
        content: this.content,
      }
      axios.post(`${SERVER_URL}/community/articles/create/`, articleItem, this.setToken())
        .then(() => this.$router.push({ name: 'ArticleList' }))
        .catch(error => console.log(error))
    },
  }
}
</script>

<style>

</style>