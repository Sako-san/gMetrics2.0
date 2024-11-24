const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') },
      { path: 'players', component: () => import('pages/PlayersPage.vue') },
    ],
  },
]

export default routes

