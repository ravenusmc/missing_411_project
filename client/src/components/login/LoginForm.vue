<template>
    <div>
      <section>
        <div class="form-area">
          <div class="form-input-area">
            <h2 class="center signup-title title-size font">Login</h2>
            <h3 v-if="userNotFound" class="center login-problem">
              User is not found.
              <br />
              <a><router-link class="alert" to="/signup"
                  >sign up</router-link
                ></a
              >
            </h3>
            <div v-if="passwordNoMatch">
              <h1 class="password-invalid-text center">
                Password is Invalid
              </h1>
            </div>
            <form @submit="login">
              <div class="field">
                <label class="email-input" for="email">EMAIL:</label>
                <input
                  class="input is-primary is-rounded"
                  type="email"
                  v-model="email"
                  placeholder="email"
                />
              </div>
              <div class="field">
                <label for="password">PASSWORD:</label>
                <input
                  class="input is-primary is-rounded"
                  type="password"
                  v-model="password"
                  placeholder="Password"
                />
              </div>
              <div class="button-div">
                <button class="styled-button">Login</button>
              </div>
            </form>
          </div>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  import { mapGetters, mapActions } from "vuex";
  export default {
    name: "Form",
    computed: {
      ...mapGetters("common", ["userNotFound", "passwordNoMatch"]),
    },
    data() {
      return {
        email: "",
        password: "",
      };
    },
    methods: {
      ...mapActions("common", ["loginUser"]),
      login(evt) {
        evt.preventDefault();
        const payload = {
          email: this.email,
          password: this.password,
        };
        this.loginUser({ payload });
      },
    },
  };
  </script>
  
  <style scoped>
  section {
    height: 75vh;
    margin: 3%;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  
  .signup-title {
    text-transform: uppercase;
    font-weight: bold;
  }
  
  .login-problem {
    font-size: 1.5rem;
  }
  
  .password-invalid-text {
    font-size: 25px;
    text-transform: uppercase;
  }
  
  .form-area {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  
  .form-input-area {
    background-color: rgba(53, 58, 66, 0.7);
    padding: 15px;
    border-radius: 15px;
    width: 350px;
  }
  
  .button-div {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 10px;
  }
  
  .email-input {
    margin-right: 30px;
  }
  
  .field {
    display: flex;
    flex-direction: column;
    margin-bottom: 10px;
  }
  
  .label {
    width: 100px; /* Adjust the width as needed */
  }
  
  .input {
    width: 300px; /* Adjust the width as needed */
  }

  .alert {
    color: white;
    text-decoration: none;
    font-size: 1.5rem;
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
  
  @media only all and (max-width: 900px) {
    section {
      margin-top: -100px;
    }
  }
  </style>