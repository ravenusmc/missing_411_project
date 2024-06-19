<template>
  <div>
    <form>
      <div>
        <label for="year">Enter Year:</label>
        <input v-model="year" placeholder="edit me" />
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
    // ...mapActions("csv", ["submitGenreSelectionToServer"]),
    submitSelectedYear() {
			event.preventDefault();
			console.log(this.year)
      // const payload = {
      //   selectedGenres: this.selectedGenres,
      // };
      // this.submitGenreSelectionToServer({ payload });
    },
  },
};
</script>