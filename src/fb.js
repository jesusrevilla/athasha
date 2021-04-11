import firebase from 'firebase/app'
import 'firebase/firestore'
// Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  var firebaseConfig = {
    apiKey: "AIzaSyCMLgBBAe9B1gXdAptXWFyE-W830C63r3Q",
    authDomain: "athasha-7bf64.firebaseapp.com",
    projectId: "athasha-7bf64",
    storageBucket: "athasha-7bf64.appspot.com",
    messagingSenderId: "596156114083",
    appId: "1:596156114083:web:5a85bf546157608a8c4b16",
    measurementId: "G-5JVS95M3NW"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  const db = firebase.firestore();

  db.settings({ timeStampsInSnapshots: true});

  export default db;