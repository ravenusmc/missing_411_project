<template>
  <div>
    <nav class="navbar">
      <a href="" class="navlink">Home</a>
      <a href="" class="navlink">About</a>
      <a href="" class="navlink">The Data</a>
      <a href="" class="navlink right">Sign Up</a>
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

.navlink {
	color: white;
	font-size: 2rem;
	margin: 0 30px;
}

.right {
	margin-left: auto;
}
</style>