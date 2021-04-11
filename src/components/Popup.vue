<template>
    <v-dialog max-width="600px">
        <template  v-slot:activator="{ on, attrs}">
            <v-btn v-on="on" v-bind="attrs" small flat class="mx-1 primary">
                <span class="hidden-sm-and-down">Add New Node</span>
                <v-icon dark>add</v-icon>
            </v-btn>
        </template>
        <v-card>
            <v-card-title>
                <h3>Add a new Node</h3>
            </v-card-title>
            <v-card-text>
                <v-form class="px-3">
                    <v-text-field label="Node" v-model="node" prepend-icon="keyboard"></v-text-field>
                    <v-text-field label="Point" v-model="node" prepend-icon="speed"></v-text-field>
                </v-form>
            </v-card-text>
        
        </v-card>
    </v-dialog>
</template>

<script>
export default {
    data() {
        return {
            node: ''
        }
    }
}
</script>