<template>
  <div>
    <div id="graphTwo"></div>
  </div>
</template>

<script>
import * as d3 from "d3";
import { mapActions } from "vuex";

export default {
  name: "MissingByDecade",
  mounted() {
    this.createGraphTwo();
  },
  methods: {
    ...mapActions("missing", ["getDecadeDrillDown"]),
    async handleBarClick(d) {

      //Prepare the payload
      const payload = { decade: d[0] };

      // // Await the response from the testMe action
      const response = await this.getDecadeDrillDown({ payload });

      // // Function to create a table from JSON data
      // function createTableFromJson(data) {
      //   let table =
      //     '<table border="1"><tr><th>First Name</th><th>Last Name</th><th>Age</th><th>Year Missing</th><th>State</th></tr>';
      //   data.forEach((row) => {
      //     table += `<tr>
      //                     <td>${row.firstName}</td>
      //                     <td>${row.lastName}</td>
      //                     <td>${row.age}</td>
      //                     <td>${row.yearMissing}</td>
      //                     <td>${row["state/province"]}</td>
      //                   </tr>`;
      //   });
      //   table += "</table>";
      //   return table;
      // }
      // // Display the popup with the count and response
      // const popup = document.getElementById("popup");
      // const content = document.getElementById("content");
      // content.innerHTML = `${'Missing people in ' + d[0]}<br>${createTableFromJson(response)}`;

      // popup.style.display = "block";
      // popup.style.top = `${event.clientY + 10}px`;
      // popup.style.left = `${event.clientX + 10}px`;
    },
    createGraphTwo() {
      // set the dimensions and margins of the graph
      let margin = { top: 40, right: 30, bottom: 50, left: 70 };
      let width = 460 - margin.left - margin.right;
      let height = 400 - margin.top - margin.bottom;

      // append the svg object to the div with id "graphTwo"
      let svg = d3
        .select("#graphTwo")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      // data
      let data = [
        ["1860s", 1],
        ["1870s", 1],
        ["1880s", 5],
        ["1890s", 5],
        ["1900s", 6],
        ["1910s", 9],
        ["1920s", 8],
        ["1930s", 18],
        ["1950s", 2],
        ["1990s", 1],
        ["2010s", 1],
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

      // Create a tooltip div
      let tooltip = d3
        .select("#graphOne")
        .append("div")
        .style("opacity", 0)
        .attr("class", "tooltip")
        .style("background-color", "white")
        .style("border", "solid")
        .style("border-width", "1px")
        .style("border-radius", "5px")
        .style("padding", "10px")
        .style("position", "absolute");

      // Tooltip functions
      let showTooltip = function (event, d) {
        tooltip
          .style("opacity", 1)
          .html("Decade: " + d[0] + "<br>Count: " + d[1])
          .style("left", event.pageX + 10 + "px")
          .style("top", event.pageY - 10 + "px");
      };

      let moveTooltip = function (event, d) {
        tooltip
          .style("left", event.pageX + 10 + "px")
          .style("top", event.pageY - 10 + "px");
      };

      let hideTooltip = function (event, d) {
        tooltip.style("opacity", 0);
      };

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
        })
        .on("mouseover", showTooltip)
        .on("mousemove", moveTooltip)
        .on("mouseleave", hideTooltip);

      // Add X axis label
      svg
        .append("text")
        .attr("text-anchor", "middle")
        .attr("x", width / 2)
        .attr("y", height + margin.bottom - 10)
        .text("Decade");

      // Add Y axis label
      svg
        .append("text")
        .attr("text-anchor", "middle")
        .attr("transform", "rotate(-90)")
        .attr("x", -height / 2)
        .attr("y", -margin.left + 20)
        .text("Count of Missing People");

      // Add title
      svg
        .append("text")
        .attr("text-anchor", "middle")
        .attr("x", width / 2)
        .attr("y", -margin.top / 2)
        .attr("font-size", "16px")
        .attr("font-weight", "bold")
        .text("Missing People by Decade");
    },
  },
};
</script>
