<script setup>
	import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
	<header>
		<div class="wrapper">
			<div class="greetings">
				<h1 class="blue">Заливка</h1>
				<h3>Игра полуфинала для номинации DevOps</h3>
			</div>
			<!-- <img
        alt="logo"
        class="logo"
        src="@/assets/logo.jpg"
        width="125"
        height="125"
      /> -->
			<nav>
				<router-link :to="{ name: 'result' }"
					>Смотреть результаты</router-link
				>
				<router-link :to="{ name: 'field' }">Играть</router-link>
			</nav>
		</div>
	</header>

	<router-view />
</template>

<style scoped>
	h1 {
		font-weight: 500;
		font-size: 2.6rem;
		position: relative;
		top: -10px;
	}

	h3 {
		font-size: 1.2rem;
	}

	.greetings h1,
	.greetings h3 {
		text-align: center;
	}

	/* @media (min-width: 1024px) { */
	/* .greetings h1,
  .greetings h3 {
    text-align: left;
  } */
	/* } */

	header {
		line-height: 1.5;
		max-height: 100vh;
	}

	.logo {
		display: block;
		margin: 0 auto 2rem;
	}

	nav {
		width: 100%;
		font-size: 12px;
		text-align: center;
		margin-top: 2rem;
	}

	nav a.router-link-exact-active {
		color: var(--color-text);
	}

	nav a.router-link-exact-active:hover {
		background-color: transparent;
	}

	nav a {
		display: inline-block;
		padding: 0 1rem;
		border-left: 1px solid var(--color-border);
	}

	nav a:first-of-type {
		border: 0;
	}
	/* 
@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
} */
</style>
