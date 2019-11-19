<template>
  <div>
    
  </div>
</template>

<script>
import router from '@/router' // src 로부터 router import

export default {
  name: 'Home',

  // 함수
  methods: {
    // 로그인 되어있는지 확인하는 함수
    // 사용자 로그인 유무를 확인하여 로그인되어있지 않을 시 로그인 페이지로 보내겠다.
    checkLoggedIn() {
      // 1. 세션을 시작해서
      this.$session.start()

      // 2. jwt 가 있는지 확인
      // 확인하는 함수 has()
      if(!this.$session.has('jwt')) {
        // 없다면 로그인 페이지로 보내겠다.
        router.push('/login')
      }
    }
  },

  // Vue 가 화면에 그려지면 실행하는 함수
  mounted() {

  }

}
</script>

<style>

</style>