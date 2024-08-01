import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import store from '@/store/index';


Vue.use(Vuex);

const data = {
	dataReceived: false,
	mapData: {MI: 1},
	year: 1868,
};

const getters = {
	dataReceived: (state) => state.dataReceived,
	mapData: (state) => state.mapData,
	year: (state) => state.year,
};

const actions = {

	submitSelectedYearToServer: ({ commit }, { payload }) => {
		commit('setYear', payload['year'])
		const path = 'http://localhost:5000/buildMap';
		axios.post(path, payload)
			.then((res) => {
				commit('setMapData', res.data)
			})
			.catch((error) => {
				console.log(error);
			});
	},

	async getCoastDrillDown({ commit }, payload) {
		try {
			// Perform an asynchronous operation, for example, an API call
			const res = await axios.post('http://localhost:5000/getCoastData', payload);
			// Return the data from the response
			return res.data;
		} catch (error) {
			console.error('Error in getCoastDrillDown action:', error);
			throw error;
		}
	},

	async getTopFiveDrillDown({ commit }, payload) {
		try {
			const res = await axios.post('http://localhost:5000/getTopFiveData', payload);
			return res.data;
		}catch (error) {
			console.error('Error in getTopFiveDrillDown action:', error);
			throw error;
		}
	},

	async getDecadeDrillDown({ commit }, payload) {
		try {
			const res = await axios.post('http://localhost:5000/getDecadeDrillDown', payload);
			return res.data;
		}catch (error) {
			console.error('Error in getDecadeDrillDown action:', error);
			throw error;
		}
	},

	async getAgeDrillDown({ commit }, payload) {
		try {
			const res = await axios.post('http://localhost:5000/getAgeDrillDown', payload);
			return res.data;
		}catch (error) {
			console.error('Error in getAgeDrillDown action:', error);
			throw error;
		}
	},

	async getSexDrillDown({ commit }, payload) {
		try {
			const res = await axios.post('http://localhost:5000/getSexDrillDown', payload);
			return res.data;
		}catch (error) {
			console.error('Error in getSexDrillDown action:', error);
		}
	},

	async getMapDrillDown({ commit }, payload) {
		try {
			const res = await axios.post('http://localhost:5000/getMapDrillDown', payload);
			return res.data;
		}catch (error) {
			console.error('Error in getMapDrillDown action:', error);
			throw error;
		}
	},

};

const mutations = {

	setMapData(state, value) {
		state.mapData = value;
	},

	setYear(state, value) {
		state.year = value;
	},

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};