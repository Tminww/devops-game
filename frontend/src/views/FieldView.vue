<template>
	<div class="result">
		<svg
			width="1280.000000pt"
			height="989.000000pt"
			viewBox="0 0 1280.000000 989.000000"
			class="hex"
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
	</div>
</template>

<style>
	.hex {
		position: absolute;
		width: 50px;
		height: 50px;
		transform: rotate(30deg);
		fill: #1323b1;
	}
	.hex:hover {
		fill: #797fb1;
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
	.field {
		min-height: 100%;
		display: flex;
		flex-direction: row;
		justify-content: center;
		padding-top: 40px;
	}
</style>
