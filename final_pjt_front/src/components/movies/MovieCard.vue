<template>
  <div class="col m-0 p-0">
    <img :src="posterURL" class="card-img-top" :class="{ 'on-cursor': focusImg }" alt="movie_poster" @mouseenter="mouseEnter" @mouseleave="mouseLeave">
    <div v-show="focusImg" class="text-white text-on-image">
      <small>{{ movieGenres }}</small>
      <h4>{{ movie.title }}</h4>
      <div class="text-warning">
        <i v-if="star >= 2" class="fas fa-star"></i>
        <i v-else-if="star === 1" class="fas fa-star-half-alt"></i>
        <i v-else class="far fa-star"></i>
        <i v-if="star >= 4" class="fas fa-star"></i>
        <i v-else-if="star === 3" class="fas fa-star-half-alt"></i>
        <i v-else class="far fa-star"></i>
        <i v-if="star >= 6" class="fas fa-star"></i>
        <i v-else-if="star === 5" class="fas fa-star-half-alt"></i>
        <i v-else class="far fa-star"></i>
        <i v-if="star >= 8" class="fas fa-star"></i>
        <i v-else-if="star === 7" class="fas fa-star-half-alt"></i>
        <i v-else class="far fa-star"></i>
        <i v-if="star >= 10" class="fas fa-star"></i>
        <i v-else-if="star === 9" class="fas fa-star-half-alt"></i>
        <i v-else class="far fa-star"></i>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import Vue from 'vue'
import vueMoment from 'vue-moment'
Vue.use(vueMoment)
export default {
  name: 'MovieCard',
  props: {
    movie: [Object, Array]
  },
  data: function () {
    return {
      focusImg: false,
    }
  },
  computed: {
    posterURL: function () {
      return this.movie.poster_path
    },
    star: function () {
      const rate = _.round(this.movie.vote_average)
      return rate
    },
    movieGenres: function () {
      const genres = this.movie.genre_ids.map(genre => genre.name).join('/')
      return genres
    }
  },
  methods: {
    mouseEnter: function () {
      if (!this.focusImg) {
        this.focusImg = true
      }
    },
    mouseLeave: function () {
      if (this.focusImg) {
        this.focusImg = false
      }
    },
  }
}
</script>

<style scoped>
.on-cursor {
  opacity: 30%;
}
.text-on-image {
  top: 0; left: 0; bottom: 0; right: 0;
  position: absolute;
  padding-top: 30%;
  text-align: center;
  z-index: -1;
}
</style>