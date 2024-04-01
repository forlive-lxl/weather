import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Weather from '@/components/Weather'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/weather', // Define the path for the Weather component
      name: 'Weather',
      component: Weather // Use the Weather component as the route component
    },
    {
      path: '/',
      name: 'HelloWorld',
      component: Weather
    }
  ]
})
