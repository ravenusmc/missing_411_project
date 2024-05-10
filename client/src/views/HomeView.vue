<template>
  <div>
    <router-view />
    <section>

      <div class='main-image'>

      </div>

    </section>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
  }
}
</script>

<style scoped>

.main-image {
  height: 75vh;
  background: url("../assets/images/home.jpg") center/cover no-repeat; /* Combine background properties */
  background-size: cover;
}


</style>
