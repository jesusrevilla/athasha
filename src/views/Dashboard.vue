<template>
  <div class="dashboard px-2">
    <h3 class="subheading grey--text mt-4">Dashboard</h3>
  
    <v-container fluid class="my-3">
      <v-layout row wrap>
        <v-flex xs12 sm6 md4 lg3>
          <v-card class="text-xs-center ma-3" outlined elevation="2">
            <v-card-title class="pl-3 pt-2">Modbus07</v-card-title>
            <v-card-text>
              <div class="grey--text">Temperature degrees C</div>
              <div>
                <v-row class="py-3" justify="space-around">
                  <v-chip-group mandatory active-class="primary">
                    <v-chip>20</v-chip>
                    <v-chip>25</v-chip>
                    <v-chip>30</v-chip>
                    <v-chip>35</v-chip>
                    <v-chip>40</v-chip>            
                  </v-chip-group>
                </v-row>
              </div>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
              <v-spacer></v-spacer>
              <Popup />
              <v-btn icon>
                <v-icon>edit</v-icon>
              </v-btn>
              <v-btn icon>
                <v-icon>delete</v-icon>
              </v-btn>
            </v-card-actions>           
          </v-card>
        </v-flex>
        <v-flex xs12 sm6 md4 lg3 v-for="(screen_value, i) in screen_values" :key="i">
          <v-card class="text-xs-center ma-3" outlined elevation="2">
            <v-card-title class="pl-3 pt-2">{{ screen_value.name }} </v-card-title>
            <v-card-text>
              <div id="chips-container">
                <v-chip :class="`${screen_value.value} ma-2`" text-color="white">
                  {{ screen_value.value }}
                </v-chip>
              </div>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
              <v-spacer></v-spacer>
              <Popup />
              <v-btn icon>
                <v-icon>edit</v-icon>
              </v-btn>
              <v-btn icon>
                <v-icon>delete</v-icon>
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
import Popup from '../components/Popup'

export default {
  components: { Popup },
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
          
          for (var i = 0; i < points.length; i++){
            points_array.push({name: points[i].name, value:0, type: points[i].type})
          }
        
          break
        case "initial_values":
          console.log(data)
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