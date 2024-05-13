<template>
  <div>
    <div class="pic-area">
      <div class="pic-one generic-pic-styling"></div>
      <div class="pic-two generic-pic-styling"></div>
      <div class="pic-three generic-pic-styling"></div>
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

.generic-pic-styling {
  height: 500px;
  width: 300px;
	background-size: cover;
}

.pic-one {
  background: url("../../assets/images/missing_one.jpg") center/cover no-repeat; /* Combine background properties */
}

.pic-two {
  background: url("../../assets/images/missing_two.jpg") center/cover no-repeat; /* Combine background properties */
}

.pic-three {
  background: url("../../assets/images/missing_three.jpg") center/cover no-repeat; /* Combine background properties */
}
</style>