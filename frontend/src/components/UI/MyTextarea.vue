<template>
  <textarea
        :value="value"
        @input="updateTextarea"
        class="textarea"
    ></textarea>
</template>

<script>
export default {
    name: 'MyTextarea',
    props: {
        value: [String, Number]
    },
    methods: {
        updateTextarea(event) {
            this.$emit('update:value', event.target.value)
        }
    }
}
</script>

<style lang="scss" scoped>
.textarea {
    resize: none;
    padding: 5px 10px;
    width: 500px;
    height: 200px;

  &:focus {
    outline-color: #8e4adf;
  }
}
</style>
