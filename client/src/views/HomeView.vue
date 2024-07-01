<template>
  <div>
    <router-view />
    <Jumbo />
    <Midsection />
    <hr>
    <Purpose />
    <Bottom />
  </div>
</template>

<script>
// @ is an alias to /src
import Jumbo from '@/components/home/Jumbo.vue'
import Midsection from '@/components/home/Midsection.vue'
import Purpose from '@/components/home/Purpose.vue'
import Bottom from '@/components/home/Bottom.vue'

export default {
  name: 'HomeView',
  components: {
    Jumbo,
    Midsection,
    Purpose,
    Bottom
  },
}
</script>

<style scoped>

</style>

