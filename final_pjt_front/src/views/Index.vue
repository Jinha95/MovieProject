<template>
  <div>

  </div>
</template>

<script>
export default {
  name: 'Index',
  props: {
    login: Boolean,
  },
  created: function () {
    if (this.login) {
      this.$router.push({ name: 'MovieList' })
    } else {
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<style>

</style>