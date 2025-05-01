<template>
    <div class="dating-app-content">
      <div v-if="error" class="profile-error-message">
        {{ error }}
      </div>
      <div v-else-if="!user" class="loading">Loading...</div>
  
      <div v-if="user" class="main-profile-details">
        <h1>{{ user.name }}'s Profile</h1>
        <img :src="user.photo" alt="Profile Photo" class="main-profile-photo" />
        <p><strong>Username:</strong> {{ user.username }}</p>
        <p><strong>Email:</strong> {{ user.email }}</p>
        <p><strong>Date Joined:</strong> {{ new Date(user.date_joined).toLocaleDateString() }}</p>
      </div>
  
      <h2 class="favorites-header">My Profiles</h2>
      <div v-if="profiles.length" class="profile-grid-layout">
        <div v-for="profile in profiles" :key="profile.id" class="favorite-user-details">
          <h3>{{ profile.name }}</h3>
          <p><strong>Parish:</strong> {{ profile.parish }}</p>
          <p><strong>Biography:</strong> {{ profile.biography }}</p>
          <button @click="viewProfile(profile.id)">View More Details</button>
          <button @click="findMatches(profile.id)">Match Me</button>
        </div>
      </div>
      <p v-else>No profiles found.</p>
  
      <h2 class="favorites-header">My Favorites</h2>
      <div v-if="favorites.length" class="profile-grid-layout">
        <div v-for="fav in favorites" :key="fav.id" class="favorite-user-details">
          <img :src="fav.photo" alt="Favorite User Photo" class="favorite-user-details img" />
          <h3>{{ fav.name }}</h3>
        </div>
      </div>
      <p v-else>No favorite users yet.</p>
    </div>
  </template>
  
  


  <script setup>
  import { ref, onMounted } from "vue";
  import { useRouter } from "vue-router";
  // import { getToken } from "../auth.js";
  
  const router = useRouter();
  // const token = getToken();
  const user = ref(null);
  const profiles = ref([]);
  const favorites = ref([]);
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
        alert("Matches found! Check the matches section.");
      } else {
        alert("No matches found.");
      }
    } catch (error) {
      console.error("Error fetching matches:", error);
    }
  }
  </script>
  

  <style scoped>

  
  .profile-error-message {
    color: white;
    text-align: center;
    padding: 1rem;
  }

  .main-profile-details {
    background-color: #fa7777;
    border-radius: 100px;
    padding: 50px;
    max-width: 600px;
    margin: 40px auto;
  }
  
  p {
    font-size: 1.5rem;
    margin: 0.5rem 0;
    font-size: 25;
    font-family: 'Times New Roman', Times, serif;
  }
  
  .dating-app-content {
    /* background-image: url(../assets/back2.jpg); */
    min-height: 100vh;
    max-height: 100vh;
    background-repeat: no-repeat;
    background-position: center top;
    background-size: cover;
    width: 100%;
    height: auto;
    overflow-y: auto;
  }
  
  @media (max-width: 600px) {
    .dating-app-content {
      min-height: 100vh;
      max-height: 100vh;
    }
  }
  
  @media (min-width: 1200px) {
    .dating-app-content {
      min-height: 100vh;
      max-height: 100vh;
    }
  }
  
  .add-to-favorites-icon {
    margin-left: 26px;
  }
  
  .add-to-favorites-icon:hover {
    cursor: pointer;
  }
  
  .send-email-button {
    margin-left: 40px;
    padding: 7px;
    background-color: green;
    border-radius: 5px;
    color: #fff;
  }
  
  .send-email-button:hover {
    background-color: pink;
  }
  
  .favorite-user-details {
    background-color: rgb(228, 191, 198);
    margin-right: 80%;
    padding: 20px;
    border-radius: 20px;
    margin-bottom: 5px;
    width: fit-content;
  }

  .favorites-header {
    margin-top: 40px;
  }
  
  .favorite-user-details img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 1rem;
  }
  
  
  .profile-grid-layout {
    display: grid;
    grid-template-columns: auto auto;
    gap: 5px;
  }

  .main-profile-photo {
    width: 250px;
    height: 250px;
    border-radius: 40%;
    object-fit: cover;
    /* margin-bottom: 1rem; */
  }
  </style>
  