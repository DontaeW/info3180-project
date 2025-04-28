<template>
    <div class="profile-container">
      <h1>My Profile</h1>
  
      <div v-if="error" class="error-message">{{ error }}</div>
      <div v-else-if="!user" class="loading">Loading...</div>
  
      <div v-if="user" class="user-details">
        <img :src="user.photo" alt="Profile Photo" class="profile-photo" />
        <h2>{{ user.name }}</h2>
        <p><strong>Username:</strong> {{ user.username }}</p>
        <p><strong>Email:</strong> {{ user.email }}</p>
        <p><strong>Joined:</strong> {{ new Date(user.date_joined).toLocaleDateString() }}</p>
  
        <button @click="editProfile">Edit Profile</button>
      </div>
  
      <h2>My Profiles</h2>
      <div v-if="profiles.length">
        <div v-for="profile in profiles" :key="profile.id" class="profile-card">
          <h3>{{ profile.name }}</h3>
          <p><strong>Parish:</strong> {{ profile.parish }}</p>
          <p><strong>Biography:</strong> {{ profile.biography }}</p>
          <button @click="viewProfile(profile.id)">View Profile</button>
        </div>
      </div>
      <p v-else>No profiles found.</p>
  
      <h2>My Favorites</h2>
      <div v-if="favorites.length">
        <div v-for="fav in favorites" :key="fav.id" class="fav-card">
          <img :src="fav.photo" alt="Favorite User Photo" class="fav-photo" />
          <h3>{{ fav.name }}</h3>
        </div>
      </div>
      <p v-else>No favorite users yet.</p>
    </div>
  </template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { getToken } from "../auth.js";

const router = useRouter();
const token = getToken();
const user = ref(null);
const profiles = ref([]);
const favorites = ref([]);
const matchedProfiles = ref([]);
const error = ref("");

async function fetchData(url, errorMessage) {
  try {
    const res = await fetch(url, {
      method: "GET",
      headers: { Authorization: `Bearer ${token}` },
    });
    if (!res.ok) {
      throw new Error(errorMessage);
    }
    return await res.json();
  } catch (err) {
    error.value = err.message;
  }
}

onMounted(async () => {
  const userId = localStorage.getItem("user_id");

  user.value = await fetchData(`/api/users/${userId}`, "Failed to load user details.");
  profiles.value = await fetchData(`/api/profiles/${userId}`, "Failed to load profiles.");
  favorites.value = await fetchData(`/api/users/${userId}/favourites`, "Failed to load favorite users.");
});

function viewProfile(profileId) {
  router.push(`/profiles/${profileId}`);
}

async function findMatches(profileId) {
  try {
    const response = await fetch(`/api/profiles/matches/${profileId}`, {
      method: "GET",
      headers: { Authorization: `Bearer ${token}` },
    });
    const data = await response.json();
    if (data.matching_profiles.length) {
      matchedProfiles.value = data.matching_profiles;
    } else {
      alert("No matches found.");
    }
  } catch (error) {
    console.error("Error fetching matches:", error);
  }
}
</script>


<style scoped>
.profile-container {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  background: #f4f4f4;
  border-radius: 10px;
  text-align: center;
}

.profile-photo {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
}

.profile-card, .fav-card {
  padding: 15px;
  margin: 10px 0;
  border-radius: 8px;
  background: white;
  box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
}

.fav-photo {
  width: 80px;
  height: 80px;
  border-radius: 50%;
}

button {
  background: #007bff;
  color: white;
  padding: 8px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
button:hover {
  background: #0056b3;
}
</style>


  