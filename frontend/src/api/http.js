import axios from 'axios'
// axios.defaults.withCredentials = true;
// axios.defaults.baseURL = 'http://localhost:8080/'
// axios.defaults.headers.common["Access-Control-Allow-Origin"] = "*";
axios.defaults.baseURL = 'http://localhost:8000/'

const http = {
	async get(path, parameters) {
		const params = new URLSearchParams(parameters)
		console.log(params)
		console.log(this.baseUrl, path, params)
		return (await axios.get(`/${path}/${params}`)).data
	},
	async post(path, body) {
		return
	},
	setUrl(url) {
		axios.defaults.baseURL = url
	},
}

export { http }
export default http
