<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
    <a class="navbar-brand" href="/">Home</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'MovieList' }">영화</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'ArticleList' }">게시판</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'MovieRecommend' }">영화 추천</router-link>
        </li>
      </ul>
      <input class="search-movie mr-sm-2 bg-dark" type="search" placeholder="영화 검색" aria-label="Search" @keypress.enter="searchMovie">
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
  methods: {
    searchMovie: function () {
      alert('현재 영화 검색 기능을 복구 중에 있습니다. 다음에 이용해주세요.')
    }
  }
}
</script>

<style scoped>
.search-movie {
  border: none;
  color: lightgray;
  border-bottom: 2px solid gray;
  
}
</style>
