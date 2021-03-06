import Vue from 'vue'
import App from './App.vue'
import VueResource from "vue-resource"

Vue.use(VueResource)

Vue.http.options.root = "http://localhost:5000/api"

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
