<template>
<div>
	<h1>Data</h1>

	<div class='graph-area'>
		<TopFiveGraphs />
	</div>
</div>
</template>

<script>
import TopFiveGraphs from '@/components/graphs/TopFiveGraphs.vue'

export default {
	name: "Missing",
	components: {
		TopFiveGraphs,
  },
};

</script>

<style scope>
.graph-area {
	display: grid;
	grid-template-columns: 1fr 1fr;
}

</style>