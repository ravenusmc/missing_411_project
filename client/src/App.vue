<template>
  <div id="app">
    <router-view/>
    <Footer/>
  </div>
</template>

<script>
// import Navbar from "@/components/common/Navbar.vue";
import Footer from "@/components/common/Footer.vue";

export default {
    components: {
    // Navbar,
    Footer,
  },
}
</script>

<style>

.center {
  text-align: center;
}

.arrange-data {
  display: grid;
  grid-template-columns: 1fr 1fr;
}
</style>
