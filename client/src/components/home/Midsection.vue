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
  background: url("../../assets/images/missing_one.jpg") center/cover no-repeat; 
}

.pic-two {
  background: url("../../assets/images/missing_two.jpg") center/cover no-repeat; 
}

.pic-three {
  background: url("../../assets/images/missing_three.jpg") center/cover no-repeat; 
}

@media only screen and (max-width: 769px) {

  .pic-area {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
  }

  .generic-pic-styling {
    height: 500px;
    width: 300px;
    margin: 30px;
  }

}
</style>