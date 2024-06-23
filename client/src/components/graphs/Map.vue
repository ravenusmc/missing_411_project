<template>
  <div>
    <Mapform />
    <Mapgraph />
  </div>
</template>

<script>
import Mapform from "@/components/forms/Mapform.vue";
import Mapgraph from "@/components/graphs/Mapgraph.vue";

export default {
  name: "Map",
  components: {
    Mapform,
    Mapgraph,
  },
};
</script>

