<template>
  <div v-if="login">
    <div class="mb-3">
      <router-link :to="{ name: 'ArticleList' }">
        <button class="btn btn-dark text-secondary">글 목록</button>
      </router-link>
      <router-link :to="{ name: 'UpdateArticle', params: {article_id: $route.params.article_id} }">
        <button class="btn btn-dark text-secondary">수정하기</button>
      </router-link>
      <button @click="deleteArticle" class="btn btn-dark text-secondary">삭제하기</button>
    </div>
    <div class="jumbotron">
      <h2>{{ article.title }}</h2>
      <hr>
      <div class="text-right"><small>작성일: {{ article.created_at | moment('YYYY-MM-DD') }}</small></div>
      <div class="text-right"><small>작성자: {{ article.user_name }}</small></div>
      <br>
      <p>{{ article.content }}</p>
    </div>
    <ul v-if="comments" class="jumbotron">
      <Comment
        v-for="(comment, idx) in comments"
        :key="idx"
        :comment="comment"
        @delete-comment="deleteComment"
      />
    </ul>
    <ul v-else>
      아직 댓글이 없습니다.
    </ul>
    <CommentForm @write-comment="writeComment"/>
  </div>
  <div v-else>
    <h2 align="center">로그인이 필요한 서비스입니다</h2>
    <div class="mb-3">
      <router-link :to="{ name: 'ArticleList' }">
        <button class="btn btn-dark text-secondary">글 목록</button>
      </router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Vue from 'vue'
import vueMoment from 'vue-moment'
import Comment from '@/components/community/Comment.vue'
import CommentForm from '@/components/community/CommentForm.vue'

Vue.use(vueMoment)

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  components: {
    Comment,
    CommentForm,
  },
  name: 'ArticleDetail',
  data: function () {
    return {
      article: [],
      comments: [],
      login: false,
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
    readArticle: function () {
      const articleId = this.$route.params.article_id
      axios.get(`${SERVER_URL}/community/${articleId}`, this.setToken())
        .then(response => {
          console.log(response)
          this.article = response.data
        })
        .catch(error => console.log(error))
    },
    deleteArticle: function () {
      const articleId = this.$route.params.article_id
      axios.delete(`${SERVER_URL}/community/${articleId}`, this.setToken())
        .then(response => {
          console.log(response)
          this.article = response.data
          this.$router.push({ name: 'ArticleList' })
        })
        .catch(error => console.log(error))
    },
    readComments: function () {
      const articleId = this.$route.params.article_id
      axios.get(`${SERVER_URL}/community/${articleId}/comments`, this.setToken())
        .then(response => {
          console.log(response.data)
          this.comments = response.data
          console.log(this.comments)
        })
        .catch(error => console.log(error))      
    },
    writeComment: function () {
      this.readComments()
    },
    deleteComment: function (commentItem) {
      const index = this.comments.indexOf(commentItem)
      this.comments.splice(index, 1)
    }
  },
  created: function () {
    console.log('created')
    const token = localStorage.getItem('jwt')

    if (token) {
      if (!this.login) {
        this.login = true
        this.readComments()
        this.readArticle()
      }
    }
  },
}
</script>

<style scoped>
router-link a{
  text-decoration: none;
}
</style>