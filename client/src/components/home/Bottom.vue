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
  height: 100px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.link-appearance {
  display: block;
  margin: 5px 0;
}


a {
  text-decoration: none;
  text-align: center;
  color: black;
}


</style>