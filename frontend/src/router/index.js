import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'

Vue.use(Router)

export default new Router({
  // パス末尾へ'#'が追加されるのを防ぐ
  mode: 'history',
  routes: [
    {
      // '/'に対して、frontend/src/components/ 配下のHelloWorld.vueファイルを参照する
      path: '/',
      name: 'Home',
      component: Home
    }
  ]
})
