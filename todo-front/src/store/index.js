import Vue from 'vue'
import Vuex from 'vuex'
import jwtDecode from 'jwt-decode'

Vue.use(Vuex)

export default new Vuex.Store({
  // 상태 (데이터)
  state: {
    token: null,
  },
  // computed
  getters: {
    isLoggedIn(state) {
      return state.token ? true : false
    },
    options(state) {
      return {
        headers: {
          Authorization: 'JWT ' + state.token
        }
      }
    },
    userId(state) {
      return state.token ? jwtDecode(state.token).user_id : null
    }
  },
  // 상태만 변경하는 함수
  mutations: {
    // 첫 인자 무조건 state
    setToken(state, token) {
      // 로그인하면 토큰 변경
      state.token = token
    }
  },
  // method 와 같음
  actions: {
    login(context, token) {
      context.commit('setToken', token) 
    },

    logout(context) {
      context.commit('setToken', null)
    }
  },
})
