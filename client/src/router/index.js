import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store/index';
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView.vue')
  },
  {
    path: '/data',
    name: 'missing',
    component: () => import('../views/Missing.vue'),
    // The code below keeps the user from going to the missing page without signing up
    beforeEnter: (to, from, next) => {
      if (store.state.common.loginFlag === false) {
        next('/login');
      } else {
        next();
      }
    },
    beforeRouteLeave: (to, from, next) => {
      if (store.state.common.loginFlag === false) {
        next('/login');
      } else {
        next();
      }
    },
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import('../views/SignUp.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
