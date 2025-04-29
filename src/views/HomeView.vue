<template>
  <br>
  <div class="home-page">
    <div v-if="route.path === '/login'" class="login-container">
      <LoginForm/>
    </div>
    <div v-if="route.path === '/register'" class="register-container">
      <SignUpForm/>
    </div>
  </div>
</template>

<script setup>
  import { useRoute } from "vue-router";
  import LoginForm from "@/components/LoginForm.vue";
  import SignUpForm from "@/components/SignUpForm.vue";

  const route = useRoute();
</script>

<style>
/* Add any component specific styles here */
</style>