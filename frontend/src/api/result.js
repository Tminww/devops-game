import http from './http'

const result = {
	async getResults(limit = 10) {
		const parameters = { limit: limit }
		return await http.get('result? ', parameters)
	},
}

export { result }
export default result
