<template>
    <form id="signupForm" @submit.prevent="handleRegister" enctype="multipart/form-data">
        <div class="signup-container">
            <h1>Register</h1>
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" class="form-control" v-model="user.username" placeholder="Enter your username" required />
                
                <label for="password">Password:</label>
                <input type="password" id="password" class="form-control" v-model="user.password" placeholder="Enter your password" required/>

                <label for="name">Name:</label>
                <input type="text" id="name" class="form-control" v-model="user.name" placeholder="Enter your full name" required />
                
                <label for="email">Email:</label>
                <input type="text" id="email" class="form-control" v-model="user.email" placeholder="Enter your email" required />
                
                <label for="photo_data">Profile Photo:</label>
                <input type="file" id="photo_data" class="form-control" @change="handlePhotoUpload"/>
                <small class="form-text text-muted">Please upload a JPG or PNG image for your profile picture.</small>
            </div>
            <button type="submit">Register</button>

            <div v-if="successMessage" class="alert alert-success">{{ successMessage }}</div>
            <div v-if="errors.length" class="alert alert-danger">
                <ul>
                <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
                </ul>
            </div>
        </div>
    </form>
</template>

<script setup>
    import { ref, onMounted } from 'vue';
    import { useRouter } from 'vue-router';
    const router = useRouter();

    const csrf_token = ref("");
    const user = ref({
        username: "",
        password: "",
        name: "",
        email: "",
    });
    const photo_data = ref(null);
    const successMessage = ref("");
    const errors = ref([]);

    // Fetch CSRF token when component is mounted
    onMounted(() => {
        getCsrfToken();
    });

    // Method to fetch CSRF token
    function getCsrfToken() {
    fetch('/api/v1/csrf-token')
        .then(response => response.json())
        .then(data => {
        csrfToken.value = data.csrf_token;
        })
        .catch(error => console.log(error));
    }
        
    // Method to handle photo upload
    function handlePhotoUpload(event) {
        photo_data.value = event.target.files[0];
    }

    function handleRegister() {
        errors.value = [];
        successMessage.value = "";

        const signupForm = document.getElementById('signupForm');
        const form_data = new FormData(signupForm);

        form_data.append("username", user.value.username);
        form_data.append("password", user.value.password);
        form_data.append("name", user.value.name);
        form_data.append("email", user.value.email);
        form_data.append("photo_data", photo_data.value);
        form_data.append("csrf_token", csrf_token.value);

        fetch("/api/register", {
            method: "POST",
            body: form_data,
            headers: {
                "X-CSRF-Token": csrf_token.value,
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                successMessage.value = data.message;
                console.log("Registration successful: ", data);
                router.push('/login'); // Redirect to login page
            } else {
                errors.value = data.errors || ["Failed to register user."];
                console.error("Backend errors:", data.errors);
            }
        })
        .catch (err => {
        errors.value = ["An error occurred while registering."];
        console.error("Error registering: ", err);
        });
    };
</script>

<style scoped>
.signup-container {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
    margin-bottom: 20px;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

input {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #ff789a;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #ff3d6d;
    transition: background-color 0.3s ease;
}
</style>