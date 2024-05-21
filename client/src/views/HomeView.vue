<template>
  <div>
    <router-view />
    <Jumbo />
    <Midsection />
    <Purpose />
  </div>
</template>

<script>
// @ is an alias to /src
import Jumbo from '@/components/home/Jumbo.vue'
import Midsection from '@/components/home/Midsection.vue'
import Purpose from '@/components/home/Purpose.vue'

export default {
  name: 'HomeView',
  components: {
    Jumbo,
    Midsection,
    Purpose,
  },
}
</script>

<style scoped>


</style>
