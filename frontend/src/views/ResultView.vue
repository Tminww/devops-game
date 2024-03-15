<template>
	<div class="result">
		<div>Результаты последних {{ getResult.count }} игр</div>
		<div v-if="error">{{ error }}</div>
		<div class="flex-container">
			<div v-for="result of getResult.response"></div>
		</div>
	</div>
</template>

<script lang="js">
	import { mapGetters, mapActions } from 'vuex'

	export default {
		name: 'results',
		components: {  },

		data() {
			return {
				loading: false,
				error: null,
			}
		},
		computed: {
			...mapGetters([
				'getResult',
			]),
		},

		methods: {
			...mapActions([
				'loadResultAPI',
				"dropResult"
			]),

			async loadResult() {
				try {
					this.loading = true
					this.error = null

					await this.loadResultAPI()
				} catch (e) {
					this.error = e.message
					this.dropResult()
				} finally {
					this.loading = false
				}
			},
		},

		async mounted() {
			await this.loadResult()

		},
	}
</script>

<style>
	/* @media (min-width: 1024px) { */
	.result {
		min-height: 100vh;
		display: flex;
		align-items: center;
	}

	/* } */
</style>
