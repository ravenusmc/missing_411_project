import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import store from '@/store/index';

Vue.use(Vuex);

const data = {
	dataReceived: false,
	mapData: {MI: 1},
};

const getters = {
	dataReceived: (state) => state.dataReceived,
	mapData: (state) => state.mapData
};

const actions = {

	submitSelectedYearToServer: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/buildMap';
		axios.post(path, payload)
			.then((res) => {
				commit('setMapData', res.data)
			})
			.catch((error) => {
				console.log(error);
			});
	},

	// testMe: ({ commit }, { payload }) => {
	// 	console.log("Action")
	// 	const path = 'http://localhost:5000/getCoastData';
	// 	axios.post(path, payload)
	// 		.then((res) => {
	// 			return res.data
	// 			// commit('setMapData', res.data)
	// 		})
	// 		.catch((error) => {
	// 			console.log(error);
	// 		});
	// },

	async getCoastDrillDown({ commit }, payload) {
		try {
			// Perform an asynchronous operation, for example, an API call
			const res = await axios.post('http://localhost:5000/getCoastData', payload);
			// Return the data from the response
			return res.data;
		} catch (error) {
			console.error('Error in testMe action:', error);
			throw error;
		}
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