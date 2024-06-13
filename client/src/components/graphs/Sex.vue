<template>
  <div>
    <div id="graphFour"></div>
  </div>
</template>

<script>
import * as d3 from "d3";

export default {
  name: "CommonAge",
  mounted() {
    this.createGraphThree();
  },
  methods: {
    createGraphThree() {
      // set the dimensions and margins of the graph
      let margin = { top: 40, right: 30, bottom: 50, left: 70 };
      let width = 460 - margin.left - margin.right;
			let height = 400 - margin.top - margin.bottom;
			

      // append the svg object to the div with id "graphTwo"
      let svg = d3
        .select("#graphThree")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
				.attr("transform", "translate(" + margin.left + "," + margin.top + ")");
			
			let data = [
				['M', 44], 
				['F', 14]
			]
			

    },
  },
};
</script>

<style>
</style>