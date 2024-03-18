<template>
	<div class="result">
		<template v-if="error">
			{{ error }}
		</template>
		<template v-else-if="loading">
			<!-- loader -->
			<div class="loader"></div>
		</template>

		<div v-else-if="getResult.count == 0">
			<h1 class="blue">
					Результатов нет
				</h1>
		</div>

		<div v-else class="flex-container">
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
	/* HTML: <div class="loader"></div> */
	.loader {
	width: 15px;
	color: rgb(18, 91, 201);
	aspect-ratio: 1;
	border-radius: 50%;
	clip-path: inset(-45px);
	box-shadow: -60px 15px,-60px 15px,-60px 15px;
	transform: translateY(-15px);
	animation: l19 1s infinite linear;
	}
	@keyframes l19{ 
	16.67% {box-shadow:-60px 15px,-60px 15px,19px 15px}
	33.33% {box-shadow:-60px 15px,  0px 15px,19px 15px}
	40%,60%{box-shadow:-19px 15px,  0px 15px,19px 15px}
	66.67% {box-shadow:-19px 15px,  0px 15px,60px 15px}
	83.33% {box-shadow:-19px 15px, 60px 15px,60px 15px}
	100%   {box-shadow: 60px 15px, 60px 15px,60px 15px}
	}
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
