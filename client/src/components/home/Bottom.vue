<template>
  <div>
    <hr />
    <div class="main-div">
      <div class="link-div">
        <a><router-link class="link-appearance" to="/">Login</router-link></a>
        <hr />
        <a><router-link class="" to="/">Sign Up</router-link></a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Bottom",
};
</script>

<style scoped>
.main-div {
  margin: 5%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.link-div {
  padding: 15px;
  border: 2px solid black;
  border-radius: 50%;
  width: 100px;
  height: 100px; /* Ensure the height is equal to the width */
  box-sizing: border-box; /* Include padding and border in the element's total width and height */
}

a {
  text-decoration: none;
  text-align: center;
}

/* .link-appearance {
  color: blue;
} */
</style>