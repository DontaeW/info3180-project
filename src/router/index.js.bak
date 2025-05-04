import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserHomeView from '../views/UserHomeView.vue'
import MyProfileView from '../views/MyProfileView.vue'
import CreateProfileView from '../views/CreateProfileView.vue'
<<<<<<< HEAD
=======
import LoginForm from '../components/LoginForm.vue'
import SignUpForm from '../components/SignUpForm.vue'
>>>>>>> 7dcaeba (Initial commit with updated ProfileDetailView button styles)

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/home',
      name: 'userHome',
      component: UserHomeView,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/about',
      name: 'about',
<<<<<<< HEAD
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
=======
>>>>>>> 7dcaeba (Initial commit with updated ProfileDetailView button styles)
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/login',
      name: 'login',
<<<<<<< HEAD
      component: HomeView
=======
      component: LoginForm
>>>>>>> 7dcaeba (Initial commit with updated ProfileDetailView button styles)
    },
    {
      path: '/register',
      name: 'register',
<<<<<<< HEAD
      component: HomeView
=======
      component: SignUpForm
>>>>>>> 7dcaeba (Initial commit with updated ProfileDetailView button styles)
    },
    {
      path: '/profile',
      name: 'profile',
      component: MyProfileView
    },
    {
      path: '/create',
      name: 'create',
      component: CreateProfileView,
<<<<<<< HEAD
    }
=======
    },
    {
      path: '/profiles/:id',
      name: 'profileDetail',
      component: () => import('../views/ProfileDetailView.vue'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/edit-profile/:id',
      name: 'editProfile',
      component: () => import('../views/EditProfileView.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/edit-user-profile/:id',
      name: 'editUserProfile',
      component: () => import('../views/EditUserProfileView.vue'),
      meta: { requiresAuth: true }
      }
    
>>>>>>> 7dcaeba (Initial commit with updated ProfileDetailView button styles)
  ]
})

export default router
<<<<<<< HEAD

=======
>>>>>>> 7dcaeba (Initial commit with updated ProfileDetailView button styles)
