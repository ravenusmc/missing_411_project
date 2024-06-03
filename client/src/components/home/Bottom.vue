<template>
  <div>
    <hr />
    <div class='pic-div'>
      <div class="main-div">
        <div class="link-div">
          <a><router-link class="link-appearance" to="/">Login</router-link></a>
          <hr />
          <a><router-link class="" to="/">Sign Up</router-link></a>
        </div>
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
.pic-div {
  height: 80vh;
  background: url("../../assets/images/home_2.jpg") center/cover no-repeat;
  background-size: cover;
  display: flex;
  justify-content: center;
  align-items: center;
}

.main-div {
  display: flex;
  justify-content: center;
  align-items: center;
}

.link-div {
  padding: 15px;
  border: 2px solid black;
  border-radius: 50%;
  width: 200px;
  height: 200px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  background-color: rgba(0, 0, 0, 0.6);
}

.link-appearance {
  display: block;
  margin: 5px 0;
}

a {
  text-decoration: none;
  text-align: center;
  color: white;
  font-size: 2rem;
  text-transform: uppercase;
}
</style>