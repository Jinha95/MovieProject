<template>
  <li class="d-flex justify-content-between align-items-center">
    <span>{{ comment.content }}</span><button @click="axiosDelete(url)" class="btn"><i class="far fa-trash-alt"></i></button>
  </li>
</template>

<script>

import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Comment',
  props: {
    comment: Object,
  },
  computed: {
    url: function () {
      return `community/comments/${this.comment.id}/`
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
    axiosDelete: function (url) {
      axios.delete(`${SERVER_URL}/${url}`, this.setToken())
        .then(response => {
          console.log(response)
          this.$emit('delete-comment', this.comment)
        })
        .catch(error => console.log(error))
    },
  }
}
</script>
<style>

</style>