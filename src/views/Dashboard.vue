<template>
  <div class="dashboard px-2">
    <h3 class="subheading grey--text mt-4">Dashboard</h3>
  
    <v-container fluid class="my-3">
      <v-layout row wrap>
        <v-flex xs12 sm6 md4 lg3 v-for="(screen_value, i) in screen_values" :key="i">
          <v-card class="text-xs-center ma-3" outlined elevation="2">
            <v-card-title class="pl-3 pt-2" >{{ screen_value.name }} </v-card-title>
            <v-card-text>
              <div id="chips-container">
                <v-chip :class="`${screen_value.value} ma-2`" text-color="white" 
                @click="change(`${ screen_value.id }`, `${screen_value.value}`)" :id="`${ screen_value.id }`">
                  {{ screen_value.value }}
                </v-chip>
              </div>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
              <v-spacer></v-spacer>
              
              <v-btn icon>
                <v-icon>arrow_upward</v-icon>
              </v-btn>
              <v-btn icon>
                <v-icon>arrow_downward</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>

  </div>


</template>

<script>
// @ is an alias to /src

export default {
  data() {
    return {    
      screen_values: [],
      connection: null
    }
  },
  methods:{
    sendMessasge: function(message) {
      console.log(this.connection);
      this.connection.send(message);
    },
    change: (id, value) => {
      console.log(id);
      console.log(value)
    }
  },
  created() {

    var points_array = new Array()

    console.log("Starting Connection to WebSocket Server")
    this.connection = new WebSocket("ws://127.0.0.1:6789/")

    this.connection.onopen = function(event){
      console.log(event)
      console.log("Connected")
    }

    this.connection.onmessage = function (event){
      const data = JSON.parse(event.data);
      switch(data.type){
        
        case "schema":
          var points = data.points
          
          for (let i = 0; i < points.length; i++){
            points_array.push({name: points[i].name, value:0, type: points[i].type, id:i})
          }
          console.log(points)
          break
        
        case "initial_values":

          for (let i = 0; i < data.values.length; i++){
            points_array[i].value = data.values[i]
          }
          console.log(data.values)
          break
      }
    }
    this.screen_values = points_array
  }
}
</script>

<style>
#chips-container .v-chip.on{
  background: green;
}

#chips-container .v-chip.off{
  background: red;
}


#chips-container .v-chip {
  background: blue;
}
</style>