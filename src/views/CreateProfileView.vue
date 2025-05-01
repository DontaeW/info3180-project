<template>
  <div class="create-profile-container">
    <h1>Create Profile</h1>
    <form @submit.prevent="handleCreateProfile" enctype="multipart/form-data">
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="profile.name" required />
      </div>

      <div class="form-group">
        <label for="parish">Parish:</label>
        <input type="text" id="parish" v-model="profile.parish" required />
      </div>

      <div class="form-group">
        <label for="biography">Biography:</label>
        <textarea id="biography" v-model="profile.biography" required></textarea>
      </div>

      <div class="form-group">
        <label for="photo">Profile Photo:</label>
        <input type="file" id="photo" @change="handlePhotoUpload" accept="image/png, image/jpeg" />
        <small>Please upload a JPG or PNG image for your profile picture.</small>
      </div>

      <button type="submit">Create Profile</button>

      <div v-if="message" class="success-message">{{ message }}</div>
      <div v-if="errors.length" class="error-messages">
        <ul>
          <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
        </ul>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';

const authStore = useAuthStore();

const router = useRouter();
const token = authStore.token;

const profile = ref({
  name: '',
  parish: '',
  biography: '',
});
const photo = ref(null);
const message = ref('');
const errors = ref([]);

function handlePhotoUpload(event) {
  photo.value = event.target.files[0];
}

async function handleCreateProfile() {
  errors.value = [];
  message.value = '';

  const formData = new FormData();
  formData.append('name', profile.value.name);
  formData.append('parish', profile.value.parish);
  formData.append('biography', profile.value.biography);
  if (photo.value) {
    formData.append('photo', photo.value);
  }

  try {
    const response = await fetch('/api/profiles', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${token}`,
      },
      body: formData,
    });

    const data = await response.json();

    if (!response.ok) {
      if (data.errors) {
        errors.value = Object.values(data.errors).flat();
      } else if (data.message) {
        errors.value = [data.message];
      } else {
        errors.value = ['Failed to create profile.'];
      }
    } else {
      message.value = 'Profile created successfully!';
      errors.value = [];
      // Optionally redirect to profile list or details page
      router.push('/my-profile');
    }
  } catch (error) {
    errors.value = ['An error occurred while creating the profile.'];
    console.error(error);
  }
}
</script>

<style scoped>
.create-profile-container {
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
  background: #f4f4f4;
  border-radius: 10px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
}

input[type="text"],
textarea {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
  border-radius: 5px;
  border: 1px solid #ccc;
}

textarea {
  resize: vertical;
  min-height: 80px;
}

button {
  background-color: #007bff;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.success-message {
  color: green;
  margin-top: 10px;
}

.error-messages {
  color: red;
  margin-top: 10px;
}
</style>
