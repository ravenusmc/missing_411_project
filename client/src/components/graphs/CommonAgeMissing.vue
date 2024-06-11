<template>
  <div>
    <div id="graphThree"></div>
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
        [3.0, 7],
        [2.0, 6],
        [4.0, 6],
        [1.75, 3],
        [7.0, 3],
      ];

      // Add X axis
      let x = d3
        .scaleBand()
        .range([0, width])
        .domain(data.map((d) => d[0]))
        .padding(0.2);
      svg
        .append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

      // Add Y axis
      let y = d3
        .scaleLinear()
        .domain([0, d3.max(data, (d) => d[1])])
        .range([height, 0]);
			svg.append("g").call(d3.axisLeft(y));
			
			// Add X axis label
      svg
        .append("text")
        .attr("text-anchor", "middle")
        .attr("x", width / 2)
        .attr("y", height + margin.bottom - 10)
        .text("Top Five Most Common Ages of Missing");
    },
  },
};
</script>

<style>
</style>
