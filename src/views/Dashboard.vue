<template>
  <div class="dashboard">
    <h3 class="subheading grey--text mt-4">Dashboard</h3>
  
    <v-container class="my-3">

      <v-layout row class="pa-4">
        <v-btn small flat color="grey-lighten-4" @click="sortBy('node')">
          <v-icon left small>height</v-icon>
          <span class="caption text-lowercase">By node</span>
        </v-btn>
      </v-layout>

      <v-card outlined flat v-for="(screen_value, i) in screen_values" :key="i" class="ma-1 pa-1">
        <v-layout row wrap class="pa-3">
          <v-flex xs12 md3>
            <div class="caption grey--text">Node</div>
            <div>{{ screen_value.node }}</div>
          </v-flex>
          <v-flex xs6 md3>
            <div class="caption grey--text">Point</div>
            <div>
              {{ screen_value.point }}
            </div>
          </v-flex>          
          <v-flex xs4 md3>
            <div class="caption grey--text">Value</div>
            <div>
              <v-btn plain fab x-small color="green" dark>
                <v-icon>edit</v-icon>
              </v-btn>
              {{ screen_value.value }}
            </div>
          </v-flex>
          <v-flex xs2 md3>
            <div class="caption grey--text">Delete</div>
            <div>
              <v-btn plain fab dark color="red" falt x-small>
                <v-icon right>delete</v-icon>
              </v-btn>
            </div>
          </v-flex>
        </v-layout>
      </v-card>
    </v-container>

  </div>


</template>

<script>
// @ is an alias to /src

export default {
  data() {
    return {    
      screen_values: [
        {node: 'Modbus0', point: 'Emergency Stop', value: 'ON'},
        {node: 'Modbus1', point: 'Buzzer', value: 'OFF'},
        {node: 'Modbus3', point: 'Stop Button', value: 'ON'},
        {node: 'Modbus0', point: 'Red Light', value: 'ON'},
        {node: 'Modbus2', point: 'Green Light', value: 'OFF'},
        {node: 'Modbus4', point: 'Emergency Stop', value: 'OFF'},
        {node: 'Modbus5', point: 'Temperature', value: '10V'},
      
      ]
    }
  },
  methods:{
    sortBy(prop){
      this.screen_values.sort((a, b) => a[prop] < b[prop] ? -1 : 1)
    }
  }
}
</script>

<style scoped>
ul{
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
</style>