<template>
    <v-dialog max-width="600px">
        <template  v-slot:activator="{ on, attrs}">
            <v-btn v-on="on" v-bind="attrs" icon>
                <v-icon dark>add</v-icon>
            </v-btn>
        </template>
        <v-card>
            <v-card-title>
                <h3>Add a new Node</h3>
            </v-card-title>
            <v-card-text>
                <v-form class="px-3" ref="form">
                    <v-text-field label="Node" v-model="node" prepend-icon="keyboard" :rules="inputRules"></v-text-field>
                    <v-text-field label="Point" v-model="point" prepend-icon="speed" :rules="inputRules"></v-text-field>
                    <v-btn text class="success mx-0 mt-3" @click="submit">Add Node</v-btn>
                </v-form>
            </v-card-text>
        
        </v-card>
    </v-dialog>
</template>

<script>
export default {
    data() {
        return {
            node: '',
            point: '',
            inputRules: [
                v => v.length >= 3 || 'Invalid input'
            ]
        }
    },
    methods: {
        submit(){
            if(this.$refs.form.validate()){
                console.log(this.node, this.point)
            }
        }
    }
}
</script>