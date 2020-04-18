import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import Dashboard from "./components/Dashboard.vue"
import Tests from "./components/Tests.vue"
import Profiles from "./components/Profiles.vue"
import Analytics from "./components/Analytics.vue"
import TestSession from "./components/TestSession.vue"
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
      path: '/tests',
      name: 'Tests',
      component: Tests
    },
    {
      path: '/profiles',
      name: 'Profiles',
      component: Profiles
    },
    {
      path: '/analytics',
      name: 'Analytics',
      component: Analytics
    },
    {
      path: '/session/:id',
      name: 'Session',
      component: TestSession
    },
  ]
})

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')