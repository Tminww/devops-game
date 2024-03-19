<template>
	<svg
		width="1280.000000pt"
		height="989.000000pt"
		viewBox="0 0 1280.000000 989.000000"
		class="hexagon"
		:style="{ fill: color }"
	>
		<g
			transform="translate(0.000000,989.000000) scale(0.100000,-0.100000)"
			stroke="none"
		>
			<path
				d="M2516 7269 c-1164 -2018 -1337 -2323 -1329 -2342 6 -12 303 -528 660
-1147 357 -619 955 -1655 1329 -2302 l679 -1178 2685 0 2686 0 619 1072 c1721
2982 2029 3515 2042 3544 l15 31 -434 754 c-238 415 -841 1459 -1338 2321
l-905 1568 -2685 0 -2685 0 -1339 -2321z"
			/>
		</g>
	</svg>
</template>

<script lang="js">

	export default {
		name: "icon-hexagon",
		props: {
		color: { type: String, required: true },
	},
		data(){
			return {
				xCoord: 0,
				yCoord: 0,

			}
		},
		computed:{
			getCurrentColor(){
				console.log(self.color)

				return self.color
			}
		}

	};
</script>

<style scoped>
	.hexagon {
		position: absolute;
		width: 50px;
		height: 50px;
		transform: rotate(30deg);
		transition: fill 1s;
	}
	.hexagon:hover {
		fill: #070a24;
	}
</style>
