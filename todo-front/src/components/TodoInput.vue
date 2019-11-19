<template>
  <div class="todo-input">
    <form class="input-group mb-3" @submit.prevent="onSubmit">
      <input v-model="title" type="text" class="form-control">
      <button type="submit" class="btn btn-success">add</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'TodoInput',
  data() {
    return {
      title: ''
    }
  },
  methods: {
    onSubmit() {
      // emit 은 component 가 이벤트를 발생시키게 하는 함수
      this.$emit('createTodo', this.title)
      this.title = ''
    }
  }

}
</script>

<style>

</style>