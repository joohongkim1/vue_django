<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">Loading..</span>
    </div>

    <div v-else class="login-form">
      
      <div class="alert alert-danger" v-if="errors.length">
        <h4>다음의 오류를 해결해주세요.</h4>
        <hr>
        <div v-for="(error, idx) in errors" v-bind:key="idx">{{ error }}</div>
      </div>
      
      <div class="form-group">
        <label for="id">ID</label>
        <input
          type="text"
          id="id"
          class="form-control"
          placeholder="아이디를 입력해주세요"
          v-model="credentials.username"
        />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input
          type="password"
          id="password"
          class="form-control"
          placeholder="비밀번호를 입력해주세요"
          v-model="credentials.password"
        />
      </div>
      <button class="btn btn-success" @click="login">로그인</button>
      <!-- v-on => @: 줄이기 가능, 어떤 행동을 했을 때  -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'

export default {
  name: "LoginForm",
  data() {
    return {
      credentials: {
        username: "",
        password: ""
      },
      loading: false, // 로딩 원 표시
      errors: []
    };
  },
  methods: {
    login() {
      if(this.checkForm()) { // 함수가 유효한지 아닌지를 확인해서 true or false 반환
        this.loading = true

        // http://127.0.0.1:8000
        const SERVER_IP = process.env.VUE_APP_SERVER_IP
        // axios.get('http://127.0.0.1:8000/', this.credentials)
        // SERVER IP 를 한 번만 바꿔주면 다른 곳에서도 적용


        axios.post(SERVER_IP + '/api-token-auth/', this.credentials) 
        // this.credentials 를 담아서 해당 서버로 보낸다.
        .then(response => {
          // 세션을 초기화, 사용하겠다.
          this.$session.start()
          // 응답결과를 세션에 저장하겠다.
          // this.$session.set(key, value)
          this.$session.set('jwt', response.data.token)

          // vuex store 를 등록해서 this.$store 로 접근 가능
          // dispatch('login) => login 이라는 action 을 실행
          this.$store.dispatch('login', response.data.token)
          // console.log(response)
          this.loading = false
          // vue router 를 통해 특정 페이지로 이동
          router.push('/')
        })
        .catch(error => {
          console.error(error)
          this.loading = false
        })
      }
    },
    checkForm() {
      this.errors = [] // 체크할 때 항상 초기화를 해줘야 뜨지 않음.
      if (!this.credentials.username) {
        this.errors.push("아이디를 입력해주세요.");
      }
      if (this.credentials.password.length < 8) {
        // 비밀번호가 8글자보다 작으면
        this.errors.push("비밀번호는 8글자 이상 입력해주세요.");
      }
      if (this.errors.length === 0) { // 위의 둘을 통과한다면
        return true // true 반환
      }       
    },
  },
};
</script>

<style>
</style>