<template>
  <div>
    <router-view />
    <Jumbo />>
    <Midsection />
  </div>
</template>

<script>
// @ is an alias to /src
import Jumbo from '@/components/home/Jumbo.vue'
import Midsection from '@/components/home/Midsection.vue'

export default {
  name: 'HomeView',
  components: {
    Jumbo,
    Midsection,
  },
}
</script>

<style scoped>


</style>
