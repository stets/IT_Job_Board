import Vue from 'vue';
import VueRouter from 'vue-router';
// import Jobs from '../views/Jobs.vue';


Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'jobs',
    component: () => import('../views/Jobs.vue'),
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
