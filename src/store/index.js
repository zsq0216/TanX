import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      count: 0,
      token: null,
      currentUsername: null,
      currentYear: null,
      currentMonth: null,
      // 其他状态数据...
    };
  },
  mutations: {
    increment(state) {
      state.count++;
      // 其他 mutations...
    },
    SET_TOKEN(state, token) {
      state.token = token;
    },
    setCurrentUsername(state, username) {
      state.currentUsername = username;
    },
    setCurrentYear(state, year) {
      state.currentYear = year;
    },
    setCurrentMonth(state, month) {
      state.currentMonth = month;
    }
  },
  actions: {
    incrementAsync({ commit }) {
      setTimeout(() => {
        commit('increment');
      }, 1000);
      // 其他 actions...
    },
    saveToken({ commit }, token) {
      commit('SET_TOKEN', token);
    },

  },
  getters: {
    doubleCount(state) {
      return state.count * 2;
      // 其他 getters...
    },
    token: state => state.token,
  }
});

export default store;
