import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/home",
      name: "home",
      component: () => import("../views/LandingPage.vue"),
    },
    {
      path: "/notas",
      name: "notas",
      component: () => import("../views/GradesView.vue"),
    }
  ],
});

export default router;
