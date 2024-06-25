<template>
  <div>
    <div id="graphFive"></div>
    <div id="popup">
      <p id="popupContent"></p>
      <button @click="closePopup">Close</button>
    </div>
  </div>
</template>

<script>
import * as d3 from "d3";
import { mapActions } from "vuex";

export default {
  name: "Coast",
  mounted() {
    this.createGraphFive();
  },
  methods: {
    ...mapActions("missing", ["testMe"]),
    createGraphFive() {
      // Set the dimensions and margins of the graph
      let margin = { top: 50, right: 30, bottom: 50, left: 70 };
      let width = 460 - margin.left - margin.right;
      let height = 400 - margin.top - margin.bottom;

      // Append the svg object to the div with id "graphFive"
      let svg = d3
        .select("#graphFive")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      let data = [
        ["Eastern", 53],
        ["Western", 4],
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
        .attr("fill", "#0B90CA")
        .on("click", (event, d) => this.showPopup(d)); // Add click event

      // Add X axis label
      svg
        .append("text")
        .attr("text-anchor", "middle")
        .attr("x", width / 2)
        .attr("y", height + margin.bottom - 10)
        .attr("font-size", "12px")
        .attr("font-weight", "bold")
        .text("Coast");

      // Add Y axis label
      svg
        .append("text")
        .attr("text-anchor", "middle")
        .attr("transform", "rotate(-90)")
        .attr("x", -height / 2)
        .attr("y", -margin.left + 20)
        .attr("font-size", "12px")
        .attr("font-weight", "bold")
        .text("Count");

      // Add title
      svg
        .append("text")
        .attr("text-anchor", "middle")
        .attr("x", width / 2)
        .attr("y", -margin.top / 2 + 10)
        .attr("font-size", "16px")
        .attr("font-weight", "bold")
        .text("Missing by Coast");
    },

    showPopup(data) {
      // Display the popup with the count
      const popup = document.getElementById("popup");
      const content = document.getElementById("popupContent");
      let selectedCoast = data[0];
      console.log(data[0]);
      const payload = {
        coast: selectedCoast,
      };
      this.testMe({ payload });
      content.innerHTML = `Count: ${data[1]}`;
      popup.style.display = "block";
    },

    closePopup() {
      const popup = document.getElementById("popup");
      popup.style.display = "none";
    },
  },
};
</script>

<style>
#popup {
  z-index: 1000;
  display: none;
  position: fixed;
  top: 20%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: white;
  border: 1px solid #ccc;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
</style>
