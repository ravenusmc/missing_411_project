<template>
  <div ref="mapContainer"></div>
</template>

<script>
import * as d3 from "d3";
import usStates from "@/assets/us-states.json";
import { mapGetters } from "vuex";

export default {
  name: 'MapGraph',
  computed: {
    ...mapGetters("missing", [
      "mapData"
    ]),
  },
  watch: {
    mapData: {
      handler: "drawMap",
      deep: true,
    },
  },
  mounted() {
    this.drawMap();
  },
  methods: {
    drawMap() {
      // Clear previous SVG elements
      d3.select(this.$refs.mapContainer).select("svg").remove();

      const width = 1000;
      const height = 730;

      const svg = d3
        .select(this.$refs.mapContainer)
        .append("svg")
        .attr("viewBox", `0 0 ${width} ${height}`);

      const projection = d3.geoAlbersUsa().scale(1300).translate([487.5, 305]);
      const path = d3.geoPath().projection(projection);

      // Create a color scale
      const colorScale = d3
        .scaleQuantize()
        .domain([0, d3.max(Object.values(this.mapData))])
        .range(d3.schemeBlues[9]);

      // Draw states
      svg
        .selectAll("path")
        .data(usStates.features)
        .enter()
        .append("path")
        .attr("fill", (d) => {
          const stateAbbr = d.properties.postal;
          const value = this.mapData[stateAbbr];
          return value ? colorScale(value) : "#ccc";
        })
        .attr("d", path)
        .on("mouseover", (event, d) => {
          const stateAbbr = d.properties.postal;
          const value = this.mapData[stateAbbr] || 0;
          tooltip
            .html(`<strong>${d.properties.name}</strong><br/>Missing: ${value}`)
            .style("visibility", "visible");
        })
        .on("mousemove", (event) => {
          tooltip
            .style("top", event.pageY + 10 + "px")
            .style("left", event.pageX + 10 + "px");
        })
        .on("mouseout", () => {
          tooltip.style("visibility", "hidden");
        });

      // Create a tooltip
      const tooltip = d3
        .select(this.$refs.mapContainer)
        .append("div")
        .attr("class", "tooltip")
        .style("position", "absolute")
        .style("visibility", "hidden")
        .style("background", "white")
        .style("border", "1px solid #ccc")
        .style("padding", "10px")
        .style("border-radius", "4px")
        .style("box-shadow", "0 0 10px rgba(0,0,0,0.1)");

      // Legend
      const legend = svg
        .append("g")
        .attr("class", "legend")
        .attr("transform", `translate(20, ${height - 100})`);

      const legendRectSize = 18;
      const legendSpacing = 10; // Increase the spacing between legend items

      legend
        .selectAll("rect")
        .data(colorScale.range())
        .enter()
        .append("rect")
        .attr("x", (d, i) => i * (legendRectSize + legendSpacing))
        .attr("width", legendRectSize)
        .attr("height", legendRectSize)
        .style("fill", (d) => d)
        .style("stroke", "black")
        .style("stroke-width", "1px");

      legend
        .selectAll("text")
        .data(colorScale.range())
        .enter()
        .append("text")
        .attr("x", (d, i) => i * (legendRectSize + legendSpacing) + legendRectSize / 2)
        .attr("y", legendRectSize + legendSpacing)
        .text((d, i) => {
          const extent = colorScale.invertExtent(d);
          return `${Math.round(extent[0])}-${Math.round(extent[1])}`;
        })
        .attr("text-anchor", "middle")
        .attr("dy", "0.35em")
        .style("font-size", "12px");
    },
  },
};
</script>

<style scoped>
.tooltip {
  font-size: 12px;
  pointer-events: none;
}
</style>
