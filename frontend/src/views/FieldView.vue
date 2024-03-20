<template>
	<div class="field">
		<div class="flex-container">
			<div class="flex-row" v-for="(rowItem, xIndex) in getField">
				<icon-hexagon
					v-for="(columnItem, yIndex) in rowItem"
					class="flex-item"
					:color="columnItem"
					:xCoord="xIndex"
					:yCoord="yIndex"
				>
				</icon-hexagon>
			</div>
		</div>
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
		margin: 15px;
		padding: 0px;
		flex-direction: row;
		justify-content: flex-start;
	}
	.flex-item {
		display: flex;
		margin-right: 8px;
		margin-bottom: -30px;
		padding: 0px;
		flex-direction: row;
		justify-content: flex-start;
	}

	.flex-row:nth-child(odd) {
		margin-right: 50px;
		padding: 0px;
	}

	.field {
		min-height: 100%;
		display: flex;
		flex-direction: row;
		justify-content: center;
		padding-top: 40px;
	}
</style>
