<template>
  <div class="dashboard px-2">
    <h3 class="subheading grey--text mt-4">Dashboard</h3>
  
    <v-container fluid class="my-3">
      <v-layout row wrap>
        <v-flex xs12 sm6 md4 lg3 v-for="(screen_value, i) in screen_values" :key="i">
          <v-card class="text-xs-center ma-3" outlined elevation="2">
            <v-card-title class="pl-3 pt-2">{{ screen_value.node }} </v-card-title>
            <v-card-text>
              <div class="grey--text">{{ screen_value.point }}</div>
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
import db from '@/fb' 

export default {
  components: { Popup },
  data() {
    return {    
      screen_values: []
    }
  },
  methods:{
    sortBy(prop){
      this.screen_values.sort((a, b) => a[prop] < b[prop] ? -1 : 1)
    }
  },
  created() {
    db.collection('screens').onSnapshot(res => {
      const changes = res.docChanges();

      changes.forEach(change => {
        if(change.type === 'added'){
          this.screen_values.push({
            ...change.doc.data(),
            id: change.doc.id
          })
        }
      })

    })
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