import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import store from '@/store/index';

Vue.use(Vuex);

const data = {
	dataReceived: false,
};

const getters = {
	dataReceived: (state) => state.dataReceived,

};

const actions = {

	submitSelectedYearToServer: ({ commit }, { payload }) => {
		console.log('Action')
		const path = 'http://localhost:5000/buildMap';
		axios.post(path, payload)
			.then((res) => {
				console.log(res.data)
				// commit('setDataReceived', true)
			})
			.catch((error) => {
				console.log(error);
			});
	},


};

const mutations = {

	setDataReceived(state, value) {
		state.dataReceived = value;
	},

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};