<template>
  <q-layout view="hHh LpR fff">
    <div class="background-image">
      <q-header reveal elevated class="bg-primary text-white" height-hint="98">
        <q-toolbar>
          <q-toolbar-title>
            <img
              src="../assets/1711953510380.png"
              alt="TanX Logo"
              style="
                height: 60px;
                width: auto;
                margin-top: 20px;
                margin-bottom: 0px;
              "
            /> </q-toolbar-title
          ><q-tabs align="right">
            <q-route-tab to="/" label="首页" class="text-h5" />
            <q-route-tab to="/search" label="企业碳足迹" />
            <q-route-tab to="/about" label="关于" />
          </q-tabs>
        </q-toolbar>
      </q-header>

      <q-page-container>
        <router-view />
      </q-page-container>

      <q-footer elevated class="bg-grey-7 text-white">
        <q-toolbar>
          <q-toolbar-title>
            <img
              src="../assets/1711953510380.png"
              alt="TanX Logo"
              style="
                height: 40px;
                width: auto;
                margin-top: 20px;
                margin-bottom: 5px;
              "
            />
          </q-toolbar-title>
        </q-toolbar>
      </q-footer>
    </div>
  </q-layout>
</template>
<!-- YourComponent.vue -->
<style scoped>

.background-image {
  background-color: #e9fbec;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 80 40' width='80' height='40'%3E%3Cpath fill='%23b5c7ab' fill-opacity='0.3' d='M0 40a19.96 19.96 0 0 1 5.9-14.11 20.17 20.17 0 0 1 19.44-5.2A20 20 0 0 1 20.2 40H0zM65.32.75A20.02 20.02 0 0 1 40.8 25.26 20.02 20.02 0 0 1 65.32.76zM.07 0h20.1l-.08.07A20.02 20.02 0 0 1 .75 5.25 20.08 20.08 0 0 1 .07 0zm1.94 40h2.53l4.26-4.24v-9.78A17.96 17.96 0 0 0 2 40zm5.38 0h9.8a17.98 17.98 0 0 0 6.67-16.42L7.4 40zm3.43-15.42v9.17l11.62-11.59c-3.97-.5-8.08.3-11.62 2.42zm32.86-.78A18 18 0 0 0 63.85 3.63L43.68 23.8zm7.2-19.17v9.15L62.43 2.22c-3.96-.5-8.05.3-11.57 2.4zm-3.49 2.72c-4.1 4.1-5.81 9.69-5.13 15.03l6.61-6.6V6.02c-.51.41-1 .85-1.48 1.33zM17.18 0H7.42L3.64 3.78A18 18 0 0 0 17.18 0zM2.08 0c-.01.8.04 1.58.14 2.37L4.59 0H2.07z'%3E%3C/path%3E%3C/svg%3E");
}
</style>
