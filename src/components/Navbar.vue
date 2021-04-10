<template>
    <nav>
        <v-toolbar app>
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
            <v-toolbar-title>
                <span>Athasha</span>
                <span class="font-weight-light">App</span>
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn flat color="grey">
                <span>Sing Out</span>
                <v-icon right>exit_to_app</v-icon>
            </v-btn>
        </v-toolbar>

        <v-navigation-drawer v-model="drawer" app class="primary"></v-navigation-drawer>
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