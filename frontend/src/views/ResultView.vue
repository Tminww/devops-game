<template>
	<div class="result">
		<template v-if="error">
			{{ error }}
		</template>
		<template v-else-if="loading">
			<!-- loader -->
			<progress></progress>
		</template>

		<div class="flex-container" v-else>
			<div>
				<h1 class="blue">
					Результаты последних {{ getResult.count }} игр
				</h1>
			</div>
			<div class="flex-row" v-for="result in getResult.response">
				<div>
					{{ result.first_user.username }}
					{{ result.first_user.score }} очков
				</div>
				<div>
					{{ result.second_user.username }}
					{{ result.second_user.score }} очков
				</div>
				<div>
					{{ new Date(result.created).toLocaleDateString() }}
					{{ new Date(result.created).toLocaleTimeString() }}
				</div>
			</div>
		</div>
		<div class="flex-container"></div>
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
	.flex-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		text-align: center;
	}

	.flex-row {
		display: flex;
		flex-direction: row;
	}

	.flex-row:hover {
		background-color: hsla(224, 48%, 47%, 0.301);
		border-radius: 10px;
	}

	.flex-row > div {
		margin: 10px;
	}
	/* @media (min-width: 1024px) { */
	.result {
		min-height: 100%;
		display: flex;
		flex-direction: row;
		justify-content: center;
		padding-top: 40px;
	}

	/* } */
</style>
