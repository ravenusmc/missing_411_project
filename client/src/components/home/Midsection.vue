<template>
  <div>
    <div class="sub-title-div">
      <div class="div-for-words">
        <p>Missing 411</p>
      </div>
    </div>
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

<style scoped>
.sub-title-div {
  z-index: 100;
  text-align: center;
  font-size: 3rem;
  letter-spacing: 4.5rem;
  text-transform: uppercase;
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  left: 0;
  right: 0;
  top: 110%;
  margin-left: auto;
  margin-right: auto;
}

.div-for-words {
  background-color: rgba(0, 0, 0, 0.8);
  color: white;
  padding: 5px;
  border-radius: 15px;
}

.pic-area {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  margin: 25px;
  margin-top: 100px;
}

.generic-pic-styling {
  height: 500px;
  width: 300px;
  background-size: cover;
  position: relative;
  overflow: hidden;
}

.generic-pic-styling::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: inherit;
  z-index: 2;
  opacity: 0;
  transition: opacity 0.3s;
}

.pic-one {
  background: url("../../assets/images/missing_one.jpg") center/cover no-repeat;
}

.pic-two {
  background: url("../../assets/images/missing_two.jpg") center/cover no-repeat;
}

.pic-three {
  background: url("../../assets/images/missing_three.jpg") center/cover
    no-repeat;
}

.generic-pic-styling:hover::after {
  opacity: 1;
  animation: wave 1s infinite;
}

@keyframes wave {
  0% {
    clip-path: polygon(
      0 40%,
      25% 45%,
      50% 40%,
      75% 45%,
      100% 40%,
      100% 50%,
      75% 55%,
      50% 50%,
      25% 55%,
      0 50%
    );
  }
  50% {
    clip-path: polygon(
      0 50%,
      25% 55%,
      50% 50%,
      75% 55%,
      100% 50%,
      100% 60%,
      75% 65%,
      50% 60%,
      25% 65%,
      0 60%
    );
  }
  100% {
    clip-path: polygon(
      0 40%,
      25% 45%,
      50% 40%,
      75% 45%,
      100% 40%,
      100% 50%,
      75% 55%,
      50% 50%,
      25% 55%,
      0 50%
    );
  }
}

@media only screen and (max-width: 950px) {
  .sub-title-div {
    writing-mode: vertical-lr;
    text-orientation: upright;
    margin-left: auto;
    margin-right: auto;
    height: 1450px;
  }

  .pic-area {
    flex-direction: column;
    align-items: center;
  }

  .generic-pic-styling {
    height: 500px;
    width: 300px;
    margin: 30px;
  }
}
</style>
