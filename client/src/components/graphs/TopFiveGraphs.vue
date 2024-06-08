<template>
  <div>
    <div id="graphOne"></div>
  </div>
</template>

<script>
import * as d3 from "d3";

export default {
  name: "TopFiveGraphs",
  mounted() {
    this.createGraphOne();
  },
  methods: {
    createGraphOne() {
      // set the dimensions and margins of the graph
      let margin = { top: 10, right: 30, bottom: 50, left: 70 };
      let width = 460 - margin.left - margin.right;
      let height = 400 - margin.top - margin.bottom;

      // append the svg object to the div with id "graphOne"
      let svg = d3
        .select("#graphOne")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      // data
      let data = [
        ["State", "Count"],
        ["PA", 11],
        ["MT", 5],
        ["ID", 4],
        ["WI", 3],
        ["OH", 3],
      ];

      // Remove the header row
      data = data.slice(1);

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

      // Add bars
      svg
        .selectAll("rect")
        .data(data)
        .enter()
        .append("rect")
        .attr("x", (d) => x(d[0]))
        .attr("y", (d) => y(d[1]))
        .attr("width", x.bandwidth())
        .attr("height", (d) => height - y(d[1]))
        .attr("fill", "#69b3a2");

      // Add X axis label
      svg
        .append("text")
        .attr("text-anchor", "middle")
        .attr("x", width / 2)
        .attr("y", height + margin.bottom - 10)
        .text("State");

      // Add Y axis label
      svg
        .append("text")
        .attr("text-anchor", "middle")
        .attr("transform", "rotate(-90)")
        .attr("x", -height / 2)
        .attr("y", -margin.left + 20)
        .text("Count of Missing People");
    },
  },
};
</script>

<style scoped>
#graphOne {
  margin: 20px;
}
</style>
