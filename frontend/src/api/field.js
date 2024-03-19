import http from './http'

const field = {
	async getFields() {
		const body = {
			first_user: 'user1',
			second_user: 'user2',
		}
		return await http.post('field', body)
	},
}

export { field }
export default field
