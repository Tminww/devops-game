<template>
	<div class="result">
		<div v-for="(x, row) in getField">
			<div v-for="(y, column) in row">
				<icon-hexagon :color="column" :xCoord="x" :yCoord="y">
				</icon-hexagon>
			</div>
		</div>

		<div>{{ getField }}</div>
	</div>
</template>

<script lang="js">
	import IconHexagon from '../components/icons/IconHexagon.vue';
	import { mapGetters, mapActions } from 'vuex'

	export default {
		name: "field-view",
		components: {
			IconHexagon
		},
		data(){
			return{
				loading: false,
				error: null,


			}
		},
		computed: {
			...mapGetters([
				'getField',
				'getFieldId',
				'getFirstUser',
				'getSecondUser',
			]),

		},

		methods: {
			...mapActions([
				'loadFieldAPI',
				"dropField",
			]),
			async loadField() {
				try {
					this.loading = true
					this.error = null

					await this.loadFieldAPI()
				} catch (e) {
					this.error = e.message
					this.dropField()
				} finally {
					this.loading = false
				}
			},
		},



		async mounted() {
			console.log("Mounted")
			await this.loadField()

		},

	};
</script>

<style scoped>
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
	.field {
		min-height: 100%;
		display: flex;
		flex-direction: row;
		justify-content: center;
		padding-top: 40px;
	}
</style>
