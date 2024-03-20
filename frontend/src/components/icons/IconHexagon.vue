<template>
	<svg
		width="1280.000000pt"
		height="989.000000pt"
		viewBox="0 0 1280.000000 989.000000"
		class="hexagon"
		:style="{
			fill: getCurrentColor,
			stroke: getUserColor,
			'stroke-width': getUserWidth + 'px',
		}"
	>
		<g transform="translate(0.000000,989.000000) scale(0.100000,-0.100000)">
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
			color: { type: Number, required: true },
			xCoord: { type: Number, required: true},
			yCoord: { type: Number, required: true},

	},
		data(){
			return {
				colors: {
					1: "gray",
					2: "red",
					3: "green",
					4: "lightgreen",
					5: "blue",
					6: "lightblue",
					7: "yellow",
					8: "pink",
					9: "orange",
					0: "black",
	   }


			}
		},
		computed:{
			getCurrentColor() {
				console.log("COLOR", this.color)
				// Получаем значение цвета из пропсов
				const colorValue = this.color %10;


				// Проверяем, есть ли такой цвет в массиве colors
				if (colorValue in this.colors) {
					// Если есть, возвращаем соответствующее значение
					return this.colors[colorValue];
				} else {
					// Если цвет не найден, возвращаем "Unknown" или что-то другое по вашему усмотрению
					return "transparent";
				}
			},
			getUserColor(){
				const userColor = Math.floor(this.color / 10);
				console.log(userColor)
				if (userColor ==  1) {
					// Если есть, возвращаем соответствующее значение
					return "darkred";
				} else if (userColor ==  2){
					// Если цвет не найден, возвращаем "Unknown" или что-то другое по вашему усмотрению
					return "darkblue";
				}else{
					return "none";
				}


			},
			getUserWidth(){
				const userColor =  Math.floor(this.color / 10);
				console.log("getUserWidth" + userColor)

				if (userColor !==  0) {
					console.log("!!!!!!!!!!!!!!!!! return 20")
					// Если есть, возвращаем соответствующее значение
					return 2000;

				}else{
					return 0;
				}


			},


		}

	};
</script>

<style scoped>
	.hexagon {
		/* position: absolute; */
		padding: 0px;
		margin: -15px;
		width: 35px;
		height: 35px;
		transform: rotate(30deg);
	}
	.hexagon:hover {
		fill: #070a24;
	}
</style>
