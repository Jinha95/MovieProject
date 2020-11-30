<template>
  <div class="jumbotron">
    <router-link class="media text-dark text-decoration-none" :to="{ name: 'ArticleDetail', params: { article_id: article.id } }">
      <img src="../../assets/logo.png" class="mr-3" height="64" alt="이미지">
      <div class="media-body">
        
        <div class="d-flex justify-content-between">
          <big class="d-block text-secondary">감상/논평</big>
          <div class="text-right">
            <small class="d-block">작성일: {{ article.created_at | moment('YYYY-MM-DD') }}</small>
            <small>작성자: {{ article.user_name }}</small>
          </div>
        </div>
        <h2 class="mt-0">{{ article.title }}</h2>
      </div>
    </router-link>
  </div>
</template>

<script>
import Vue from 'vue'
import vueMoment from 'vue-moment'

Vue.use(vueMoment)

export default {
  name: 'Article',
  props: {
    article: Object,
  }
}
</script>

<style scoped>
img {
  height: 5rem;
}
.jumbotron {
  padding: 1rem;
  margin-bottom: 1rem;
}
</style>
