import Vue from 'vue'
import Vuex from 'vuex'
import missing from './modules/missing';

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    missing,
  },
});
