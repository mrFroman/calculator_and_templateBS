<template>
  <violett-button
          @click="$emit('template', this.button)"
  >
      {{ button.name }}
  </violett-button>
</template>

<script>
export default {
    emits: ['template'],
    props: {
        button: {
            type: Object
        }
    }
}
</script>

<style>

</style>
