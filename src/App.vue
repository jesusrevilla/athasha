<template>
  <v-app class="grey lighten-3">
    <Navbar />
    <v-main class="grey lighten-3">
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar'


export default {
  name: 'App',
  components: { Navbar},
  data: function() {
    return {
      connection: null
    }
  }
};
</script>
