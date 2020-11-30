<template>
  <li>
    <div class="d-flex justify-content-between">
      <span>
        {{ review.user_name }}:
        {{ review.content }}
      </span>
      <span>
        {{ review.rank }}점
      </span>
    </div>
  </li>
</template>

<script>
export default {
  name: 'MovieReview',
  props: {
    review: Object,
  }
}
</script>

<style>

</style>