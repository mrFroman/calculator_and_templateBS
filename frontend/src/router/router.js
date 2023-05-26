import {createRouter, createWebHistory} from "vue-router";
import TemplaterPage from "@/pages/TemplaterPage.vue";
import CalculatorPage from "@/pages/CalculatorPage.vue";

const routes = [
    {
        path: '/',
        component: CalculatorPage
    },
    {
        path: '/email-templater',
        component: TemplaterPage
    },
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router
