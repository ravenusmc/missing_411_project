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


	loginUser: ({ commit }, { payload }) => {
		console.log(payload)
		const path = 'http://localhost:5000/login';
		axios.post(path, payload)
			.then((res) => {
				if (res.data.login_flag) {
					console.log(res.data)
					// commit('session/setUserObject', res.data.user, { root: true })
					commit('setLoginFlag', res.data.login_flag);
					// router.push({ name: 'GameData' });
				}
				commit('setNoPasswordMatch', res.data.Password_no_match);
				commit('setUserNotFound', res.data.Not_found);
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
