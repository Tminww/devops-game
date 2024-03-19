<template>
	<div class="result">
		<div v-for="row in "
		<icon-hexagon :color="'blue'"> </icon-hexagon>
	</div>
</template>

<script lang="js">
	import IconHexagon from '../components/icons/IconHexagon.vue';

	export default {
		name: "field-view",
		components: {
			IconHexagon
		},
		data(){
			return{
				"first_user": "string",
  "second_user": "string",
  "id": 1,
  "field": [

			}
		}
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
