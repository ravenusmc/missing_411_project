<template>
  <div>
    <form>
      <div>
        <label for="year">Enter Year:</label>
        <input v-model="year" />
      </div>
      <div class="form-group">
        <button type="button" @click="submitSelectedYear">Submit</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "Mapform",
  data() {
    return {
      year: 1900,
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