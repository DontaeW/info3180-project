<template>
    <div class="container">

      <main>
        <div class="search">
          <label for="search-dropdown">Select Filter: </label>
          <select id="search-dropdown" v-model="selectedFilter">
            <option value="sowPlach">Sow Plach</option>
            <!-- Add more dropdown options as needed -->
          </select>
        </div>
  
        <div class="filters">
          <button class="btn" @click="applyFilter('name')">Name</button>
          <button class="btn" @click="applyFilter('birth')">Birth</button>
          <button class="btn" @click="applyFilter('sex')">Sex</button>
          <button class="btn" @click="applyFilter('race')">Race</button>
        </div>
  
        <section class="profiles">
          <h2>Latest Added Profiles</h2>
          <div class="profile-card" v-for="profile in profiles" :key="profile.id">
            <img :src="profile.image" alt="Profile" class="profile-image">
            <div class="profile-name">{{ profile.name }}</div>
          </div>
        </section>
      </main>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        selectedFilter: "sowPlach",
        profiles: [
          { id: 1, name: "Jamica", image: "path/to/image1.jpg" },
          { id: 2, name: "Anilasmaly", image: "path/to/image2.jpg" },
          { id: 3, name: "Jamaica", image: "path/to/image3.jpg" }
        ]
      };
    },
    methods: {
      goToProfile() {
        // Logic for navigating to the user's profile
        console.log("Navigating to profile");
      },
      logout() {
        // Handle user logout
        console.log("User logged out");
      },
      showReput() {
        // Show reput details or functionality
        console.log("Showing reput");
      },
      applyFilter(filter) {
        // Logic to filter profiles based on 'name', 'birth', 'sex', or 'race'
        console.log(`Filter applied: ${filter}`);
      }
    }
  };
  </script>
  
  <style>
  .container {
    font-family: Arial, sans-serif;
    max-width: 1200px;
    margin: 0 auto;
    padding: 10px;
  }
  
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #ffd700;
    padding: 10px 20px;
  }
  
  .logo {
    font-size: 24px;
    font-weight: bold;
  }
  
  .nav .btn {
    margin-left: 10px;
    padding: 10px;
    background-color: #ffa500;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .main {
    margin-top: 20px;
  }
  
  .filters .btn, .search select {
    margin: 5px;
    padding: 8px 15px;
  }
  
  .profiles {
    display: flex;
    gap: 15px;
    flex-wrap: wrap;
    margin-top: 20px;
  }
  
  .profile-card {
    text-align: center;
    border: 1px solid #ddd;
    padding: 10px;
    border-radius: 5px;
    background: #f9f9f9;
  }
  
  .profile-image {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 10px;
  }
  
  .profile-name {
    font-weight: bold;
  }
  </style>