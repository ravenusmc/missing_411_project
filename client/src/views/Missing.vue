<template>
<div>
	<h1>Data</h1>

	<div class='graph-area'>
		<TopFiveGraphs />
		<MissingByDecade />
		<CommonAgeMissing />
		<Sex />
	</div>
</div>
</template>

<script>
import TopFiveGraphs from '@/components/graphs/TopFiveGraphs.vue'
import MissingByDecade	from '@/components/graphs/MissingByDecade.vue'
import CommonAgeMissing	from '@/components/graphs/CommonAgeMissing.vue'
import Sex from '@/components/graphs/Sex.vue'

export default {
	name: "Missing",
	components: {
		TopFiveGraphs,
		MissingByDecade,
		CommonAgeMissing,
		Sex
  },
};

</script>

<style scope>
.graph-area {
	display: grid;
	grid-template-columns: 1fr 1fr;
}

</style>