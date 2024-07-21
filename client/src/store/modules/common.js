import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import router from '../../router';

Vue.use(Vuex);

const data = {
	userNotFound: false,
	passwordNoMatch: false,
	loginFlag: false,
};

const getters = {
	userNotFound: (state) => state.userNotFound,
	passwordNoMatch: (state) => state.passwordNoMatch,
	loginFlag: (state) => state.loginFlag,
};

const actions = {

	setUpUser: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/setUpUser';
		axios.post(path, payload)
			.then((res) => {
				router.push({ name: 'login'})
			})
			.catch((error) => {
				console.log(error);
			});
	},


};

const mutations = {

	setMapData(state, value) {
		state.mapData = value;
	},


};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};