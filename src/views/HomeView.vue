<template>
<<<<<<< HEAD
  <br>
  <div class="home-page">
    <div v-if="route.path === '/login'" class="login-container">
      <LoginForm/>
    </div>
    <div v-if="route.path === '/register'" class="register-container">
      <SignUpForm/>
=======
  <div class="home-page">
    <h1>Welcome to the Profile Matching App</h1>
    <p>Please log in or register to continue.</p>
    <div class="buttons">
      <router-link to="/login" class="btn">Login</router-link>
      <router-link to="/register" class="btn">Register</router-link>
>>>>>>> 7dcaeba (Initial commit with updated ProfileDetailView button styles)
    </div>
  </div>
</template>

<script setup>
<<<<<<< HEAD
  import { useRoute } from "vue-router";
  import LoginForm from "@/components/LoginForm.vue";
  import SignUpForm from "@/components/SignUpForm.vue";

  const route = useRoute();
</script>

<style>
/* Add any component specific styles here */
</style>
=======
import { useRoute } from "vue-router";
import LoginForm from '../components/LoginForm.vue';
import SignUpForm from '../components/SignUpForm.vue';

const route = useRoute();
</script>

<style scoped>
.home-page {
  text-align: center;
  margin-top: 100px;
}

.buttons {
  margin-top: 20px;
}

.btn {
  display: inline-block;
  margin: 0 10px;
  padding: 10px 20px;
  background-color: pink;
  color: white;
  text-decoration: none;
  border-radius: 5px;
  font-weight: bold;
}

.btn:hover {
  background-color: deeppink;
}
</style>
>>>>>>> 7dcaeba (Initial commit with updated ProfileDetailView button styles)
