<template>
  <div>
    <div class="main-image">
      <div class="title-div">
        <h1 class="center">Missing 411 Study</h1>
        <hr />
        <h3 class="center">A Project Examining Missing Person Data</h3>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomePage"
};
</script>

<style scoped>
.main-image {
  height: 80vh;
  background: url("../../assets/images/home.jpg") center/cover no-repeat;
  background-size: cover;
  display: flex;
  justify-content: center;
  align-items: center;
  animation: zoom 20s ease-in-out infinite;
}

@keyframes zoom {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
}

.title-div {
  background-color: rgba(0, 0, 0, 0.6);
  border-radius: 15px;
  color: white;
  padding: 20px;
}

.center {
  text-align: center;
}
</style>

