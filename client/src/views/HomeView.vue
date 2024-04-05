<template>
  <div>

    <router-view />

    <!-- decide on navbar --> 

    <section>


      <div>
        
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

section {
  display: grid; 
  grid-template-columns: 10% 90%;
  border: 2px solid red;
}

</style>
