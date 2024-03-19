import { createStore } from 'vuex'
import { api } from '@/api/api.js'

// Create a new store instance.
const store = createStore({
	state() {
		return {
			result: [],
			field: {},
		}
	},

	getters: {
		getResult(state) {
			return state.result
		},
		getField(state) {
			return state.field.field
		},
		getFieldId(state) {
			return state.field.id
		},
		getFirstUser(state) {
			return state.field.first_user
		},
		getSecondUser(state) {
			return state.field.second_user
		},
	},

	mutations: {
		setResult(state, newValue) {
			state.result = newValue
		},
		setField(state, newValue) {
			state.field = newValue
		},
	},

	actions: {
		dropResult(context) {
			context.commit('setResult', [])
		},
		dropField(context) {
			context.commit('setField', {})
		},

		async loadResultAPI(context) {
			const result = await api.result.getResults()
			context.commit('setResult', result)
		},
		async loadFieldAPI(context) {
			const field = await api.field.getFields()
			context.commit('setField', field)
		},
	},
})

export default store
