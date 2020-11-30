<template>
  <div v-if="login">
    <h2>관객수를 고려하여 사용자에게 영화를 추천드립니다</h2>
    <button type="button" class="btn btn-success" @click="getRecommend">추천 받기</button>
    <div v-if="getmovie" class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 row-cols-xl-5">
      <MovieCard
        type="button"
        data-toggle="modal"
        data-target="#movieModal"
        :movie="movie"
        @click.native="selectMovie(movie)"
      />
    </div>
    <div class="modal fade modal-custom-style" id="movieModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content bg-secondary text-white">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">{{ movie.title }} (평균 평점: {{ movie.vote_average }})</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <p>{{ movie.overview }}</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-dark" data-toggle="modal" data-target="#rateModal">평점 남기기</button>
            <button type="button" class="btn btn-dark" @click="videoPlay">예고편 보기</button>
          </div>
        </div>
      </div>
    </div>
    <div class="modal fade modal-custom-style" id="rateModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content bg-secondary text-white">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">{{ movie.title }} (평균 평점: {{ movie.vote_average }})</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <p>{{ movie.title }}의 평점을 남겨주세요.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else>
    <h2 align="center">로그인이 필요한 서비스입니다</h2>
  </div>
</template>

<script>
import axios from 'axios'
import MovieCard from '@/components/movies/MovieCard'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieRecommend',
  components: {
    MovieCard,
  },
  data: function () {
    return {
      movie: [],
      getmovie: false,
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
    selectMovie: function (movie) {
      this.movie = movie
      console.log(movie)
    },
    getRecommend: function () {
      this.getmovie = true
      axios.get(`${SERVER_URL}/movies/recommend/`, this.setToken())
        .then(res => this.movie = res.data)
        .catch(err => console.log(err))
    },
    videoPlay: function () {
      alert('힝! 속았지?')
    }
  },
  created: function () {
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
.modal-custom-style {
  top: 30%;
}
</style>