<template color="grey lighten-3">
    <nav>
        <v-app-bar app>
            <v-app-bar-title>
                <img class="mx-3" :src="require('../assets/logo28.png')" height="25"/>
            </v-app-bar-title>
            <v-spacer></v-spacer>
            <v-btn small text class="mx-1 primary" to="/">
                <span class="hidden-sm-and-down">Dashboard</span>
                <v-icon right >dashboard</v-icon>
            </v-btn>
            <v-btn small text class="mx-1 primary" to="/admin">
                <span class="hidden-sm-and-down">Admin</span>
                <v-icon right >manage_accounts</v-icon>
            </v-btn>
        </v-app-bar>
    </nav>

</template>

<script>

export default {
    data(){
        return{
            drawer: false,
            links: [
                { icon: 'dashboard', 'text': 'Dashboard', 'route': '/'},
                { icon: 'folder', 'text': 'My Projects', 'route': '/projects'},
                { icon: 'person', 'text': 'Team', 'route': '/team'},
            ]
        }
    }
}
</script>