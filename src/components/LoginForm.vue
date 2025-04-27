<template>
    <form id="loginForm" @submit.prevent="handleLogin" enctype="multipart/form-data">
        <div class="login-container">
            <h1>Login</h1>
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" class="form-control" v-model="username" required placeholder="Enter your username" />
                <label for="password">Password:</label>
                <input type="password" id="password" class="form-control" v-model="password" placeholder="Enter your password" required/>
            </div>
            <button type="submit">Login</button>
            <div v-if="message" class="alert alert-success">{{ message }}</div>
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

    const username = ref('');
    const password = ref('');
    const message = ref('');
    const csrfToken = ref('');
    const errors = ref([]);

    // Method to fetch CSRF token
    function getCsrfToken() {
            fetch("/api/v1/csrf-token")
            .then(response => {
                if (!response.ok) {
                throw new Error("Failed to get CSRF token");
                }
                return response.json();
            })
            .then(data => {
                console.log(data);
                csrfToken.value = data.csrf_token;
            })
            .catch(err => {
                console.error("Error fetching CSRF token", err);
            });
        }

    // Fetch CSRF token when component is mounted
    onMounted(() => {
            getCsrfToken();
        });

    function handleLogin() {
        const loginForm = document.getElementById('loginForm');
        let form_data = new FormData(loginForm);

        fetch("/api/v1/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRF-Token": csrfToken.value,
            },
            body: form_data
        })
        .then(response => {
            if (response.ok) {
                message.value = 'Login successful!';
                router.push('/userHome'); // Redirect to home page
            } else {
                return response.json().then(data => {
                    errors.value = data.errors || ['Login failed.'];
                });
            }
        })
        .catch(error => {
            errors.value.push('An error occurred during login.');
        });
    };
</script>

<style scoped>
.login-container {
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