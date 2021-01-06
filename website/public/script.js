// Your web app's Firebase configuration
const firebaseConfig = {
apiKey: "AIzaSyCl1PNdiLx2EZ31bz0eTReM8oIn3yPFcSk",
    authDomain: "mrfox-26445.firebaseapp.com",
    databaseURL: "https://mrfox-26445-default-rtdb.firebaseio.com",
    projectId: "mrfox-26445",
    storageBucket: "mrfox-26445.appspot.com",
    messagingSenderId: "830273993753",
    appId: "1:830273993753:web:1f9f98c92b9fd9a35c7e88"
};

firebase.initializeApp(firebaseConfig);

// Get a reference to the file storage service
const storage = firebase.storage();
// Get a reference to the database service
const database = firebase.database();

// Create camera database reference
const camRef = database.ref("file");

// Sync on any updates to the DB. THIS CODE RUNS EVERY TIME AN UPDATE OCCURS ON THE DB.
camRef.limitToLast(1).on("value", function(snapshot) {
  snapshot.forEach(function(childSnapshot) {
    const image = childSnapshot.val()["image"];
    const time = childSnapshot.val()["timestamp"];
    const storageRef = storage.ref(image);

    storageRef
      .getDownloadURL()
      .then(function(url) {
        console.log(url);
        document.getElementById("photo").src = url;
        document.getElementById("time").innerText = time;
      })
      .catch(function(error) {
        console.log(error);
      });
  });
});