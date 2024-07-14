<template>
  <div>
    <nav class="navbar">
      <a href="" class="navlink"><router-link class='link-style'  to="/">Home</router-link></a>
      <a href="" class="navlink"><router-link class='link-style' to="/about">About</router-link></a>
      <a href="" class="navlink"><router-link class='link-style' to="/data">The Data</router-link></a>
      <a href="" class="navlink right"><router-link class='link-style' to="/signup">Sign Up</router-link></a>
    </nav>
  </div>
</template>

<script>
</script>

<style scoped>

.navbar {
	background-color: #343a40;
	height: 50px;
	display: flex; 
	justify-content: flex-start;
}

a {
  text-decoration: none;
}

.link-style {
  color: white;
}

.navlink {
	color: white;
	font-size: 1.5rem;
	margin: 10px 15px;
}

.right {
	margin-left: auto;
}

/* Responsive aspects */
</style>