<template>
  <div>
    <nav class="navbar">
      <div class="navlinks-left">
        <a href="" class="navlink"><router-link class="link-style" to="/">Home</router-link></a>
        <a href="" class="navlink"><router-link class="link-style" to="/about">About</router-link></a>
        <a href="" class="navlink"><router-link class="link-style" to="/data">The Data</router-link></a>
      </div>
      <div class="navlinks-right">
        <a href="" class="navlink"><router-link class="link-style" to="/login">Login</router-link></a>
        <a href="" class="navlink"><router-link class="link-style" to="/signup">Sign Up</router-link></a>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style scoped>
.navbar {
  background-color: #343a40;
  height: 50px;
  display: flex; 
  justify-content: space-between;
  align-items: center;
  padding: 0 15px;
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

.navlinks-left, .navlinks-right {
  display: flex;
  align-items: center;
}

/* Responsive aspects */
</style>
