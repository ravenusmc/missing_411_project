<template>
  <div>
    <div class="signup-heading">
      <h1 class='center'>SIGN UP</h1>
    </div>
    <div class="container">
      <form @submit="signup">
        <div class="input-area">
          <label for="firstname">First Name:</label>
          <input
            type="text"
            name="firstname"
            v-model="firstName"
            id="firstname"
            placeholder="First Name"
          />
        </div>
        <div class="input-area">
          <label for="lastName">Last Name:</label>
          <input
            type="text"
            name="lastName"
            class="form-control"
            id="lastName"
            v-model="lastName"
            placeholder="Last Name"
          />
        </div>
        <div class="input-area">
          <label for="email">User Name:</label>
          <input
            type="text"
            name="usernamee"
            class="form-control"
            id="username"
            v-model="username"
            placeholder="User Name"
          />
        </div>
        <div class="input-area">
          <label for="email">Email:</label>
          <input
            type="text"
            name="email"
            class="form-control"
            id="email"
            v-model="email"
            placeholder="Email"
          />
        </div>
        <div class="input-area">
          <label for="exampleInputPassword1">Password: </label>
          <input
            type="password"
            name="password"
            class="form-control"
            id="exampleInputPassword1"
            v-model="password"
            placeholder="Password"
          />
        </div>
        <div class="input-area">
          <label for="exampleInputPassword2">Confirm Password:</label>
          <input
            type="password"
            name="password2"
            class="form-control"
            id="exampleInputPassword2"
            v-model="confirmPassword"
            placeholder="Confirm Password"
          />
        </div>
        <button
          type="submit"
          name="login"
          class="styled-button "
        >
          Submit
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "Form",
  data() {
    return {
      firstName: "",
      lastName: "",
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
    };
  },
  methods: {
    ...mapActions("common", ["setUpUser"]),
    signup(evt) {
      evt.preventDefault();
      if (this.firstName === "") {
        alert("First name must be entered");
      } else if (this.lastName === "") {
        alert("Last name must be entered");
      } else if (this.email === "") {
        alert("Email must be entered");
      } else if (this.password === "") {
        alert("Password must be entered");
      } else if (this.password !== this.confirmPassword) {
        alert("Passwords must be the same");
      } else if (this.password.length < 6) {
        alert("Password must be at least 6 characters long");
      } else {
        const payload = {
          firstName: this.firstName,
          lastName: this.lastName,
          email: this.email,
          password: this.password,
          confirmPassword: this.confirmPassword,
        };
        this.setUpUser({ payload });
      }
    },
  },
};
</script>

<style scoped>
.signup-heading {
  margin-top: 30px;
  font-size: 1.5REM;
}

.container {
  display: flex; 
  justify-content: center;
  align-items: center;
}

.container input {
  width: 100%;
  clear: both;
}

form {
  display: grid;
  grid-template-columns: 1fr 1fr;
  border-radius: 15px;
  margin-bottom: 30px;
  padding: 20px;
  background-color: rgba(53, 58, 66, 0.7);
}

.input-area {
  margin: 10px;
}

input {
  height: 25px;
}

.styled-button {
  margin-top: 10px;
  background-color: steelblue;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.styled-button:hover {
  background-color: #4682b4;
}

.styled-button:active {
  background-color: #4169e1;
  transform: scale(0.98);
}

.styled-button:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(70, 130, 180, 0.5);
}
</style>