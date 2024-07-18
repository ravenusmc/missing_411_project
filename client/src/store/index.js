import Vue from 'vue'
import Vuex from 'vuex'
import missing from './modules/missing';
import common from './modules/common';

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    missing,
    common,
  },
});
