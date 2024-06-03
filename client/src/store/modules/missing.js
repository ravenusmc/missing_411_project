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

	submitSelectionToServer: ({ commit }, { payload }) => {
		commit('setSelectedYear', payload['year'])
		commit('setSelectedGenre', payload['genre'])
		const path = 'http://localhost:5000/buildCSVCharts';
		axios.post(path, payload)
			.then((res) => {
				// console.log(res.data)
				commit('setDataReceived', true)
				commit('setBestSingleGameByYear', res.data['best_single_game'])
				commit('setBestSingleGameByYearScore', res.data['best_game_score'])
				commit('setBestGameByGenreAndYear', res.data['best_game_by_genre_and_year'])

				const topFiveGamesLength = res.data['top_five_games_and_scores_selected_year'].length;
				const topPublishersLength = res.data['top_publishers_by_selected_year'].length;
				const topPublishersGenreLength = res.data['top_publishers_by_selected_year_and_genre'].length;

				if (topFiveGamesLength === 2 && topPublishersLength === 2 && topPublishersGenreLength === 2) {
					commit('setHideAllGraphs', false);	
					// I made not need this else if statement...
				} else if (topFiveGamesLength === 2 && topPublishersLength > 2 && topPublishersGenreLength > 2) {
					console.log('Else if')
					commit('setGraphOptions', ["Top Publishers in Selected Year", "Top Publishers in Selected Year and Genre"])
				} else {
					commit('setHideAllGraphs', true);
					commit('setTopFiveGamesAndScoresSelectedYear', res.data['top_five_games_and_scores_selected_year'])
					commit('setTopPublishersBySelectedYear', res.data['top_publishers_by_selected_year'])
					commit('setTopPublishersBySelectedYearAndGenre', res.data['top_publishers_by_selected_year_and_genre'])
					commit('setGraphOptions', ["Top 5 Games for Selected Year", "Top Publishers in Selected Year", "Top Publishers in Selected Year and Genre"])
				}

				res.data['year_and_critic_ratings'] = res.data['year_and_critic_ratings'].map(([year, rating]) => [
					new Date(year, 0, 1),
					rating,
				]);
				commit('setYearAndCriticRatings', res.data['year_and_critic_ratings'])
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