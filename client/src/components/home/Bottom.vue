<template>
  <div>
    <hr />
    <div class='main-div'>
      <div class="button-div">
        <button>Login</button>
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
	margin: 10%;
	display: flex;
	justify-content: center;
	align-items: center;
}

.button-div {
  border: 2px solid black;
  border-radius: 50px;
  width: 100px;
}

button {
}
</style>