const routes = [
  {
    path: '/',
    component: () => import('layouts/EnterpriseLayout.vue'),
    children: [
      { path: '', component: () => import('pages/LogInPage.vue') },
      { path: 'form', component: () => import('pages/FormPage.vue') },
      { path: 'signup', component: () => import('pages/SignInPage.vue') },
      { path: 'personal', component: () => import('pages/PersonalPage.vue') },
      { path: 'login', component: () => import('pages/LogInPage.vue') },
      { path: 'login', component: () => import('pages/LogInPage.vue') },
      { path: 'about', component: () => import('pages/AboutPage.vue') },
    ]
  },
  {
    path: '/',
    component: () => import('layouts/BankLayout.vue'),
    children: [
      { path: 'search', component: () => import('pages/SearchPage.vue') },
      { path: 'detail', component: () => import('pages/DetailedInfoPage.vue') }
    ]
  },
  { path: '/login', redirect: '/' },
  // {
  //   path: '/login',
  //   component: () => import('pages/LogInPage.vue')
  // },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
