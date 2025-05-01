<template>
  <div class="container">
    <main class="main-layout">
      <!-- Search Form -->
      <div class="search-container">
        <h1 class="title">Search</h1>
        <form @submit.prevent="handleSearch" class="search-form">
          <input v-model="search.name" type="text" placeholder="Name" />
          <input v-model="search.birthYear" type="number" placeholder="Birth Year" />
          <select v-model="search.sex">
            <option value="">Select Sex</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
          </select>
          <input v-model="search.race" type="text" placeholder="Race" />

          <button type="submit">Search</button>
        </form>
      </div>

      <!-- Right-side content -->
      <div class="content-panel">
        <div class="filters">
          <span class="filter-title">Filter by:</span>
          <button class="btn" @click="applyFilter('name')">Name</button>
          <button class="btn" @click="applyFilter('birth')">Birth</button>
          <button class="btn" @click="applyFilter('sex')">Sex</button>
          <button class="btn" @click="applyFilter('race')">Race</button>
        </div>

        <section class="profiles">
          <div class="profile-card" v-for="profile in profiles" :key="profile.id">
            <img :src="profile.image" alt="Profile" class="profile-image">
            <div class="profile-info">
              <div class="profile-name">
                {{ profile.name }}
                <!-- <button class="heart" @click="toggleFavorite(profile)">
                  <span :class="{ favorited: profile.favorited }">♥</span>
                </button> -->
              </div>
              <div class="actions">
                <a href="#" class="view-more">View more details</a>
              </div>
            </div>
          </div>
        </section>
      </div>
    </main>
  </div>
</template>

<script setup>
  import { ref, reactive } from 'vue'
  
  const search = reactive({
    name: '',
    birthYear: '',
    sex: '',
    race: ''
  })
  
  const profiles = ref([
    { id: 1, name: 'Alice Smith', image: 'https://via.placeholder.com/50', favorited: false },
    { id: 2, name: 'John Doe', image: 'https://via.placeholder.com/50', favorited: false }
  ])

  const handleSearch = () => {
    console.log('Search Criteria:', search)
    // Implement your actual search logic here
  }

  const toggleFavorite = (profile) => {
    profile.favorited = !profile.favorited;
  }

  const applyFilter = (filterType) => {
    console.log('Applying filter:', filterType);

  }
</script>
  
<style scoped>
  .container {
    min-height: 100vh;
    padding: 1rem;
    max-width: 100%;
  }

  .main-layout {
    display: flex;
    gap: 2rem;
    align-items: flex-start;
  }

  
  /* Search Form Styles */
  .search-container {
    background-color: white;
    padding: 1.5rem;
    border-radius: 1rem;
    width: 350px;
    box-shadow: 0 0 10px black;
  }

  .title {
    text-align: center;
    color: red;
    font-size: 1.5rem;
    margin-bottom: 1rem;
  }

  .search-form {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }

  .search-form input,
  .search-form select {
    padding: 0.5rem;
    border: 2px solid orange;
    border-radius: 0.5rem;
    font-size: 0.95rem;
  }

  .search-form input:focus,
  .search-form select:focus {
    outline: none;
    border-color: pink;
  }

  .search-form button {
    padding: 0.5rem;
    background: linear-gradient(90deg, pink, rgb(255, 0, 85), rgb(255, 123, 0));
    border: none;
    border-radius: 0.5rem;
    color: white;
    font-weight: bold;
    font-size: 1rem;
    cursor: pointer;
    transition: background 0.3s ease;
  }

  .search-form button:hover {
    background: linear-gradient(90deg, rgb(255, 128, 0), rgb(255, 0, 102), pink);
  }

  /* Right Side Content */
  .content-panel {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }

  /* Filters */
  .filters {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
  }

  .filter-title {
    text-align: center;
    color: rgb(255, 162, 0);
    font-size: 1.4rem;
    font-style: italic;
    margin-bottom: 1rem;
  }

  .btn {
    background-color: pink;
    color: black;
    padding: 0.5rem 1.2rem;
    border-radius: 0.5rem;
    cursor: pointer;
    transition: background 0.3s ease;
  }

  .btn:hover {
    background-color: rgb(255, 0, 72);
    color: white;
  }

  /* Profiles */
  .profiles {
    background-color: white;
    padding: 1rem;
    border-radius: 1rem;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
  }

  .profile-info {
    display: flex;
    flex-direction: column;
    gap: 0.3rem;
    flex: 1;
  }
  .profile-name {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .heart {
    background: none;
    border: none;
    cursor: pointer;
    color: pink;
    font-size: 1.5rem;
  }
  .heart.favorited {
    color: red;
  }

  .profile-card {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1rem;
  }

  .profile-image {
    width: 50px;
    height: 50px;
    object-fit: cover;
    border-radius: 50%;
    border: 2px solid pink;
  }

  .actions {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
  }

  .view-more {
    color: orange;
    text-decoration: underline;
    font-weight: bold;
    font-size: 0.9rem;
    cursor: pointer;
  }
</style>
