<template>
  <div class="profile-container" v-if="user">
    <h1>Edit User Profile</h1>
    <form @submit.prevent="submitForm" class="profile-form">
      <div class="form-group">
        <label for="name">Name:</label>
        <input id="name" v-model="user.name" type="text" />
      </div>
      <div class="form-group">
        <label for="username">Username:</label>
        <input id="username" v-model="user.username" type="text" />
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input id="email" v-model="user.email" type="email" />
      </div>
      <button type="submit" class="btn">Save Changes</button>
      <button type="button" @click="goBack" class="btn cancel-btn">Cancel</button>
    </form>
    <div v-if="error" class="error-message">{{ error }}</div>
  </div>
  <div v-else>
    <p>Loading user profile...</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';

const route = useRoute();
const router = useRouter();
const authStore = useAuthStore();

const user = ref(null);
const error = ref('');

async function fetchUser() {
  const token = authStore.token;
  const userId = route.params.id || null;

  try {
    const response = await fetch(`/api/users/${userId}`, {
      headers: { Authorization: `Bearer ${token}` }
    });
    if (!response.ok) {
      throw new Error('Failed to load user profile');
    }
    const data = await response.json();
    user.value = data;
  } catch (err) {
    error.value = err.message;
  }
}

async function submitForm() {
  const token = authStore.token;
  try {
    const response = await fetch(`/api/users/${user.value.id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`
      },
      body: JSON.stringify(user.value)
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || 'Failed to update user profile');
    }
    alert('User profile updated successfully!');
    router.push('/profile');
  } catch (err) {
    error.value = err.message;
  }
}

function goBack() {
  router.back();
}

onMounted(() => {
  fetchUser();
});
</script>

<style scoped>
.profile-container {
  max-width: 700px;
  margin: 50px auto;
  padding: 20px;
  background-color: #fff9f9;
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(255, 105, 97, 0.2);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #333;
  text-align: center;
}

h1 {
  margin-bottom: 20px;
}

.profile-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
  text-align: left;
}

.form-group {
  display: flex;
  flex-direction: column;
}

label {
  font-weight: bold;
  margin-bottom: 5px;
}

input[type="text"],
input[type="email"] {
  padding: 8px;
  border-radius: 5px;
  border: 1px solid #ccc;
  font-size: 1rem;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

button.btn {
  background: linear-gradient(135deg, #ffb347 0%, #ff69b4 100%);
  color: white;
  padding: 10px 18px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: bold;
  font-size: 1rem;
  transition: background 0.3s ease;
  width: 150px;
  align-self: center;
}

button.btn:hover {
  background: linear-gradient(135deg, #ffcc70 0%, #ff85c1 100%);
}

button.cancel-btn {
  background-color: #f4a261;
  margin-top: 10px;
}

button.cancel-btn:hover {
  background-color: #d18e3a;
}

.error-message {
  color: #dc3545;
  margin-top: 10px;
  text-align: center;
}
</style>
