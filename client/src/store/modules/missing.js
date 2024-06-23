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