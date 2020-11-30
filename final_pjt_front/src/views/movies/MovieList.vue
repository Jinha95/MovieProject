<template>
  <div>
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 row-cols-xl-5">
      <MovieCard
        type="button"
        data-toggle="modal"
        data-target="#movieModal"
        v-for="(movie, idx) in movies"
        :key="idx"
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
            <button type="button" class="btn btn-dark" data-toggle="modal" data-target="#reviewModal" @click="readMovieReview">리뷰 보기</button>
            <button type="button" class="btn btn-dark" @click="videoPlay">예고편 보기</button>
          </div>
        </div>
      </div>
    </div>
    <div class="modal fade modal-custom-style" id="reviewModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content bg-secondary text-white">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">{{ movie.title }} (평균 평점: {{ movie.vote_average }})</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <p>「{{ movie.title }}」의 평점과 리뷰를 남겨주세요.</p>
            <ul>
              <MovieReview
                v-for="(review, idx) in movieReviews"
                :key="idx"
                :review="review"
              />
            </ul>
            <div class="d-flex">
              <input type="text" class="form-control" placeholder="리뷰 쓰기" @keypress.enter="wirteMovieReview" v-model.trim="review">
              <select name="rank" id="rank" class="form-control col-2" v-model="rank">
                <option value=0>평점</option>
                <option value=1>1점</option>
                <option value=2>2점</option>
                <option value=3>3점</option>
                <option value=4>4점</option>
                <option value=5>5점</option>
                <option value=6>6점</option>
                <option value=7>7점</option>
                <option value=8>8점</option>
                <option value=9>9점</option>
                <option value=10>10점</option>
              </select>
              <button @click="wirteMovieReview" class="btn btn-dark col-2">제출</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieCard from '@/components/movies/MovieCard'
import MovieReview from '@/components/movies/MovieReview'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieList',
  components: {
    MovieCard,
    MovieReview,
  },
  data: function () {
    return {
      movie: [],
      movies: [],
      movieReviews: [],
      review: '',
      rank: 0,
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
    readMovies: function () {
      axios.get(`${SERVER_URL}/movies/`, this.setToken())
        .then(response => this.movies = response.data)
        .catch(error => console.log(error))
    },
    selectMovie: function (movie) {
      this.movie = movie
      console.log(movie)
    },
    readMovieReview: function () {
      axios.get(`${SERVER_URL}/movies/${this.movie.id}/reviews_read/`, this.setToken())
        .then(response => {
          this.movieReviews = response.data
          console.log(this.movieReviews)
        })
        .catch(error => console.log(error))
    },
    wirteMovieReview: function () {
      if (this.rank && this.review) {
        const reviewItem = {
          rank: this.rank,
          content: this.review,
        }
        axios.post(`${SERVER_URL}/movies/${this.movie.id}/reviews/`, reviewItem, this.setToken())
          .then(response => {
            this.movieReviews.push(response.data)
            console.log(this.movieReviews)
          })
          .catch(error => console.log(error))
        this.rank = 0
        this.review = ''
      }
    },
    videoPlay: function () {
      alert('힝! 속았지?')
    }
  },
  created: function () {
    this.readMovies()
  }
}
</script>

<style>
.modal-custom-style {
  top: 30%;
}
</style>