import Vue from 'vue';
import Router from 'vue-router';
import InputURL from '../components/InputURL';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'InputURL',
      component: InputURL,
    },
  ],
});
