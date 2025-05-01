// stores/auth.js
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
    state: () => ({
        isAuthenticated: false,
        user: null,
        token: null
    }),
    actions: {
        login(userData, token) {
            this.isAuthenticated = true;
            this.user = userData;
            this.token = token;
            localStorage.setItem('authToken', token);
        },
        logout() {
            this.isAuthenticated = false;
            this.user = null;
            this.token = null;
            localStorage.removeItem('authToken');
        },
        checkAuth() {
            const token = localStorage.getItem('authToken');
            if (token) {
                this.isAuthenticated = true;
                this.token = token;
        }
        }
    }
})