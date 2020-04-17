import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import Dashboard from "./components/Dashboard.vue"
import Profiles from "./components/Profiles.vue"
Vue.use(VueRouter)
Vue.config.productionTip = false

const router= new VueRouter({
  routes: [
    {
      path: '/',
      name: 'Default',
      component: Dashboard
    },
    {
      path: '/profiles',
      name: 'Profiles',
      component: Profiles
    },
  ]
})

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')