import { createRouter, createWebHistory } from "vue-router";
import ResultView from "../views/ResultView.vue";
import FieldView from "../views/FieldView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "result",
      component: ResultView,
    },
    {
      path: "/field",
      name: "field",
      component: FieldView,
    },
  ],
});

export default router;
