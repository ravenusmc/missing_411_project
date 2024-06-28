<template>
  <div>
    <div id="graphFive"></div>
    <div id="popup" style="display: none">
      <div id="content"></div>
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

    // Add event listener to close popup when clicking outside of it
    document.addEventListener('click', this.handleOutsideClick);
  },
  beforeDestroy() {
    // Remove event listener when the component is destroyed
    document.removeEventListener('click', this.handleOutsideClick);
  },
  methods: {
    ...mapActions("missing", ["getCoastDrillDown"]),
    async handleBarClick(d) {
      // Prepare the payload
      const payload = { coast: d[0] };
      
      // Await the response from the testMe action
      const response = await this.getCoastDrillDown({ payload });
      console.log(response);
      
      // Function to create a table from JSON data
      function createTableFromJson(data) {
          let table = '<table border="1"><tr><th>First Name</th><th>Last Name</th><th>Age</th><th>Year Missing</th><th>State</th></tr>';
          data.forEach(row => {
              table += `<tr>
                          <td>${row.firstName}</td>
                          <td>${row.lastName}</td>
                          <td>${row.age}</td>
                          <td>${row.yearMissing}</td>
                          <td>${row["state/province"]}</td>
                        </tr>`;
          });
          table += '</table>';
          return table;
      }

      // Display the popup with the count and response
      const popup = document.getElementById("popup");
      const content = document.getElementById("content");
      content.innerHTML = `Count: ${d[1]}<br>${createTableFromJson(response)}`;
      popup.style.display = "block";
      popup.style.top = `${event.clientY + 10}px`;
      popup.style.left = `${event.clientX + 10}px`;
    },
    createGraphFive() {
      // set the dimensions and margins of the graph
      let margin = { top: 50, right: 30, bottom: 50, left: 70 };
      let width = 460 - margin.left - margin.right;
      let height = 400 - margin.top - margin.bottom;

      // append the svg object to the div with id "graphFive"
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
        .on("click", async (event, d) => {
          await this.handleBarClick(d);
        });

      // Add X axis label
      svg
        .append("text")
        .attr("text-anchor", "middle")
        .attr("x", width / 2)
        .attr("y", height + margin.bottom - 10) // Adjusted y position to be within the SVG
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
        .attr("y", -margin.top / 2 + 10) // Adjusted y position to be within the SVG
        .attr("font-size", "16px")
        .attr("font-weight", "bold")
        .text("Missing by Coast");
    },
    handleOutsideClick(event) {
      const popup = document.getElementById("popup");
      if (popup.style.display === "block" && !popup.contains(event.target)) {
        popup.style.display = "none";
      }
    }
  },
};
</script>

<style>
#popup {
    display: none;
    position: fixed;
    background-color: white;
    border: 1px solid black;
    padding: 10px;
    z-index: 1000;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
}

#content {
  font-size: 14px;
}
</style>
