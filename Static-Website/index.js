const firebaseConfig = {
    apiKey: "AIzaSyBYjQ204RuBhuJFnj0MyAZL6ObfLP0XV1M",
    authDomain: "indian-plagiarism-tool.firebaseapp.com",
    databaseURL: "https://indian-plagiarism-tool-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "indian-plagiarism-tool",
    storageBucket: "indian-plagiarism-tool.appspot.com",
    messagingSenderId: "204343244106",
    appId: "1:204343244106:web:0c11ca4b5de3abd204fdb3"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();
document.getElementById("loginForm").addEventListener("submit", (event) => {
    event.preventDefault()
})
firebase.auth().onAuthStateChanged((user) => {
    if (user) {
        location.replace("welcome.html")
    }
})
function login() {
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value
    firebase.auth().signInWithEmailAndPassword(email, password)
        .catch((error) => {
            document.getElementById("error").innerHTML = error.message
        })
}
function signUp() {
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value
    firebase.auth().createUserWithEmailAndPassword(email, password)
        .catch((error) => {
            document.getElementById("error").innerHTML = error.message
        });
}
function forgotPass() {
    const email = document.getElementById("email").value
    firebase.auth().sendPasswordResetEmail(email)
        .then(() => {
            alert("Reset link sent to your Email ID")
        })
        .catch((error) => {
            document.getElementById("error").innerHTML = error.message
        });
}