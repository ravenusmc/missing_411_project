<template>
<div>
	<h2 class='title center'>The Data</h2>

	<div class='graph-area'>
		<TopFiveGraphs />
		<MissingByDecade />
		<CommonAgeMissing />
		<Sex />
		<Coast />
	</div>
	<hr>
	<Map />
</div>
</template>

<script>
import TopFiveGraphs from '@/components/graphs/TopFiveGraphs.vue'
import MissingByDecade	from '@/components/graphs/MissingByDecade.vue'
import CommonAgeMissing	from '@/components/graphs/CommonAgeMissing.vue'
import Sex from '@/components/graphs/Sex.vue'
import Coast from '@/components/graphs/Coast.vue'
import Map from '@/components/graphs/Map.vue'

export default {
	name: "Missing",
	components: {
		TopFiveGraphs,
		MissingByDecade,
		CommonAgeMissing,
		Sex,
		Coast, 
		Map,
  },
};
</script>

<style scoped>
.title {
	text-transform: uppercase;
	font-size: 2em;
}

.graph-area {
	display: grid;
	grid-template-columns: 1fr 1fr;
}

@media only screen and (max-width: 850px) {

  .graph-area {
    grid-template-columns: 1fr;
  }

}

</style>