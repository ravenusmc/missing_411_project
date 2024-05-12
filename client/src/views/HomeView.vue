<template>
  <div>
    <router-view />

    <div class='main-image'>
      <div class='title-div'>
        <h1 class='center'>Missing 411 Study</h1>
        <hr>
        <h3 class='center'>A Project Examing Missing Person Data</h3>
      </div>
    </div>

    <Midsection />

  </div>
</template>

<script>
// @ is an alias to /src
import Midsection from '@/components/home/Midsection.vue'

export default {
  name: 'HomeView',
  components: {
    Midsection,
  },
}
</script>

<style scoped>

.main-image {
  height: 80vh;
  background: url("../assets/images/home.jpg") center/cover no-repeat; /* Combine background properties */
  background-size: cover;
  display: flex;
  justify-content: center;
  align-items: center;
}

.title-div {
  background-color: rgba(0, 0, 0, 0.6);
  border-radius: 15px;
  color: white;
  padding: 20px;
}


</style>
