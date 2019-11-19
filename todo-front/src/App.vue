<template>
  <div id="app">
    <div id="nav">
      
      <!-- 조건부 렌더링 -->
      <div v-if="isLoggedIn">
        <router-link to="/">Home</router-link> |
        <a @click.prevent="logout" href="/logout">Logout</a>
      </div>

      <div v-else>
        <router-link to="/login">Login</router-link> 
      </div>
      <!-- a태그로 만드는 이유 -->
      <!-- prevent : href 로 redirect 를 방지하기 위함 -->

    </div>
    <div class="container col-6">
      <router-view/>
    </div>
  </div>
</template>

<script>
import router from '@/router'

export default {
  name: 'App',
  data() {
    return {
      // 사용자의 로그인 상태 jwt 가 있으면 true
      isLoggedIn: this.$session.has('jwt')
    }
  },
  methods: {
    logout() {
      // 세션을 통째로 날려주는 기능
      this.$session.destroy()
      router.push('/login')
    }
  },
  // data 에 변화가 일어나는 시점에 실행하는 함수
  updated() {
    this.isLoggedIn = this.$session.has('jwt')
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
