import { createStore } from 'vuex'
import { api } from '@/api/api.js'

// Create a new store instance.
const store = createStore({
	state() {
		return {
			result: [],
		}
	},

	getters: {
		getResult(state) {
			return state.result
		},
	},

	mutations: {
		setResult(state, newValue) {
			state.result = newValue
		},
	},

	actions: {
		dropResult(context) {
			context.commit('setResult', [])
		},

		async loadResultAPI(context) {
			const result = await api.result.getResults()
			context.commit('setResult', result)
		},
	},
})

export default store
