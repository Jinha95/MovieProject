import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '@/views/Index'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import ArticleList from '@/views/community/ArticleList'
import ArticleDetail from '@/views/community/ArticleDetail'
import CreateArticle from '@/views/community/CreateArticle'
import MovieList from '@/views/movies/MovieList'
import MovieRecommend from '@/views/movies/MovieRecommend'
import UpdateArticle from '@/views/community/UpdateArticle'

Vue.use(VueRouter)

const routes = [
  {
    path: '',
    name: 'Index',
    component: Index,
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/community/',
    name: 'ArticleList',
    component: ArticleList,
  },
  {
    path: '/community/create-article',
    name: 'CreateArticle',
    component: CreateArticle,
  },
  {
    path: '/community/:article_id',
    name: 'ArticleDetail',
    component: ArticleDetail,
  },
  {
    path: '/community/:article_id/update',
    name: 'UpdateArticle',
    component: UpdateArticle,
  },
  {
    path: '/movies/',
    name: 'MovieList',
    component: MovieList,
  },
  {
    path: '/movies/recommend/',
    name: 'MovieRecommend',
    component: MovieRecommend,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
