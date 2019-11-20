<template>
  <div class="todo-list">
    <div class="card mb-2" v-for="todo in todos" :key="todo.id">
      <div class="card-body d-flex justify-content-between">
        <span>{{ todo.title }}</span>
        <span @click="deleteTodo(todo)">삭제</span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TodoList',
  props: {
    todos: {
      type: Array,
      required: true,
    }
  },
  computed: {
    options() {
      return this.$store.getters.options
    }
  },
  methods: {
    deleteTodo(todo) {
      // 요청 보낼 시 헤더에 token 실어서 보내야 함.
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // const options = {
      //   headers: { // key 값 Authorization 으로 해야됨.
      //     Authorization: 'JWT ' + token
      //   }
      // }
      const SERVER_IP = process.env.VUE_APP_SERVER_IP

      axios.delete(`${SERVER_IP}/api/v1/todos/${todo.id}/`, this.options)
        // 응답 받는 경우
        .then(response => {
          console.log(response)
          const idx = this.todos.indexOf(todo)
          if (idx > -1) {
            // splice : 자르기
            this.todos.splice(idx, 1)
          }
          })
        .catch(error => {
          console.error(error)
        })
    },
  }
}
</script>

<style>

</style>



