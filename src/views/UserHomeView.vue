<template>
    <div class="home">
        
    </div>
    <div class="search-container">
        <h1 class="text-center">Search Users</h1>
        <div class="search-field">
            <input v-if="nameSearch" type="text" v-model="name" placeholder="Search by name..." />
            <input v-if="birthSearch" type="text" v-model="birthYear" placeholder="Search by birth year..." />
            <input v-if="sexSearch" type="text" v-model="sex" placeholder="Search by sex..." />
            <input v-if="raceSearch" type="text" v-model="race" placeholder="Search by race..." />
            <button id="btn" @click="searchUser">Search</button>
        </div>
    </div>
    
</template>