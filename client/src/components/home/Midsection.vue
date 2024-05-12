<template>
  <div>
    <div class="pic-area">
      <div class="pic-one"></div>
      <div class="pic-two"></div>
      <div class="pic-three"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Midsection",
};
</script>

<style scope>
.pic-area {
  display: flex;
  flex-direction: row;
	justify-content: space-around;
	margin: 25px;
}

.pic-one {
  height: 500px;
  width: 300px;
  background: url("../../assets/images/missing_one.jpg") center/cover no-repeat; /* Combine background properties */
  background-size: cover;
}

.pic-two {
  height: 500px;
  width: 300px;
  background: url("../../assets/images/missing_two.jpg") center/cover no-repeat; /* Combine background properties */
  background-size: cover;
}

.pic-three {
  height: 500px;
  width: 300px;
  background: url("../../assets/images/missing_three.jpg") center/cover no-repeat; /* Combine background properties */
  background-size: cover;
}
</style>