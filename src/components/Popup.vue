<template>
    <v-dialog max-width="600px" v-model="dialog">
        <template  v-slot:activator="{ on, attrs}">
            <v-btn v-on="on" v-bind="attrs" icon>
                <v-icon dark>add</v-icon>
            </v-btn>
        </template>
        <v-card>
            <v-card-title>
                <h3>Add a new Point</h3>
            </v-card-title>
            <v-card-text>
                <v-form class="px-3" ref="form">
                    <v-text-field label="Node" v-model="node" prepend-icon="keyboard" :rules="inputRules"></v-text-field>
                    <v-text-field label="Point" v-model="point" prepend-icon="speed" :rules="inputRules"></v-text-field>
                    <v-btn text class="success mx-0 mt-3" @click="submit" :loading="loading">Add Point</v-btn>
                </v-form>
            </v-card-text>
        
        </v-card>
    </v-dialog>
</template>

<script>
import db from '@/fb'

export default {
    data() {
        return {
            node: '',
            point: '',
            inputRules: [
                v => v.length >= 3 || 'Invalid input'
            ],
            loading: false,
            dialog: false
        }
    },
    methods: {
        submit(){
            if(this.$refs.form.validate()){
                this.loading = true;
                this.dialog = false;
                
                console.log(this.node, this.point)
                const node_point = {
                    node: this.node,
                    point: this.point,
                    value: ''
                }
                db.collection('screens').add(node_point).then(() => {
                    this.loading = false;
                })
            }
        }
    }
}
</script>