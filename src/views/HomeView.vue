<template>
  <div class="home-page">
    <h2>Jam-Date</h2>
    <button class="start" @click="handleLogin">Login</button>
    <button class="start" @click="handleRegister">Register</button>
    
    <div v-if="route.path === '/login'" class="login-container">
      <LoginForm/>
    </div>
    <div v-if="route.path === '/register'" class="register-container">
      <SignUpForm/>
    </div>
  </div>
</template>

<script setup>
  import { useRouter, useRoute } from "vue-router";
  import LoginForm from "@/components/LoginForm.vue";
  import SignUpForm from "@/components/SignUpForm.vue";

  const router = useRouter();
  const route = useRoute();

  const handleLogin = () => {
    router.push("/login");
  };

  const handleRegister = () => {
    router.push("/register");
  };
</script>

<style>
/* Add any component specific styles here */
</style>