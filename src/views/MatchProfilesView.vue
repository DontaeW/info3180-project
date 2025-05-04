<template>
  <div class="match-profiles-container">
    <h1>Matched Profiles</h1>
    <div v-if="error" class="error-message">{{ error }}</div>
    <div v-if="loading">Loading matches...</div>
    <div v-if="matches.length === 0 && !loading">No matches found.</div>
    <ul v-if="matches.length > 0">
      <li v-for="match in matches" :key="match.profile_id" class="match-item">
        <img :src="match.photo" alt="Profile Photo" class="profile-photo" v-if="match.photo" />
        <div class="match-info">
          <h3>{{ match.name }}</h3>
          <p>Birth Year: {{ match.birth_year }}</p>
          <p>Height: {{ match.height }} inches</p>
          <p>Favorite Cuisine: {{ match.fav_cuisine }}</p>
          <p>Favorite Colour: {{ match.fav_colour }}</p>
          <p>Favorite School Subject: {{ match.fav_school_subject }}</p>
          <p>Political: {{ match.political ? 'Yes' : 'No' }}</p>
          <p>Religious: {{ match.religious ? 'Yes' : 'No' }}</p>
          <p>Family Oriented: {{ match.family_oriented ? 'Yes' : 'No' }}</p>
          <router-link :to="`/profiles/${match.profile_id}`">View Profile</router-link>
        </div>
      </li>
    </ul>
    <button @click="goBack">Back</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';

const route = useRoute();
const router = useRouter();
const authStore = useAuthStore();

const matches = ref([]);
const error = ref('');
const loading = ref(false);

const backendBaseUrl = 'http://localhost:5001';

async function fetchMatches() {
  loading.value = true;
  error.value = '';
  const profileId = route.params.id;
  try {
    const response = await fetch(`${backendBaseUrl}/api/profiles/matches/${profileId}`, {
      headers: {
        Authorization: `Bearer ${authStore.token}`
      },
      credentials: 'include'
    });
    if (!response.ok) {
      throw new Error('Failed to fetch matches');
    }
    const data = await response.json();
    matches.value = data.matching_profiles || [];
  } catch (err) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
}

function goBack() {
  router.back();
}

onMounted(() => {
  fetchMatches();
});
</script>

<style scoped>
.match-profiles-container {
  max-width: 700px;
  margin: auto;
  padding: 20px;
  background: #f9f9f9;
  border-radius: 10px;
}

.match-item {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
  padding-bottom: 10px;
  border-bottom: 1px solid #ccc;
}

.profile-photo {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
  margin-right: 15px;
}

.match-info h3 {
  margin: 0 0 5px 0;
}

.error-message {
  color: red;
  margin-bottom: 10px;
}
</style>
