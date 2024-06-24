<template>
  <div>
    <h3 class="center map-title">Map of Missing</h3>
    <div class='form-div'>
      <form>
        <div>
          <label for="year">Enter Year:</label>
          <input v-model="year" />
        </div>
        <div class="form-group">
          <button class='styled-button' type="button" @click="submitSelectedYear">Submit</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "Mapform",
  data() {
    return {
      year: 1868,
    };
  },
  methods: {
    ...mapActions("missing", ["submitSelectedYearToServer"]),
    submitSelectedYear() {
      event.preventDefault();
      if (this.year < 1868) {
        alert("Please Select a year greater than 1868");
      } else if (this.year > 2010) {
        alert("Please Select a Year Less than 2010");
      } else {
        const payload = {
          year: this.year,
        };
        this.submitSelectedYearToServer({ payload });
      }
    },
  },
};
</script>

<style scoped>
.map-title {
  text-transform: uppercase;
  font-size: 2rem;
}

.form-div {
  display: flex; 
  justify-content: center;
}

.styled-button {
  margin-top: 10px;
  background-color: steelblue;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.styled-button:hover {
  background-color: #4682b4;
}

.styled-button:active {
  background-color: #4169e1;
  transform: scale(0.98);
}

.styled-button:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(70, 130, 180, 0.5);
}
</style>