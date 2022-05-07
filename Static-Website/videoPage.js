$(document).ready(function () {
    var trigger = $('.hamburger'),
        overlay = $('.overlay'),
        isClosed = false;

    trigger.click(function () {
        hamburger_cross();
    });

    function hamburger_cross() {

        if (isClosed == true) {
            overlay.hide();
            trigger.removeClass('is-open');
            trigger.addClass('is-closed');
            isClosed = false;
        } else {
            overlay.show();
            trigger.removeClass('is-closed');
            trigger.addClass('is-open');
            isClosed = true;
        }
    }

    $('[data-toggle="offcanvas"]').click(function () {
        $('#wrapper').toggleClass('toggled');
    });
});
document.getElementById('inputfile')
    .addEventListener('change', function () {
        var fr = new FileReader();
        fr.onload = function () {
            document.getElementById('output')
                .textContent = fr.result;
        }
        fr.readAsText(this.files[0]);
    })
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
firebase.auth().onAuthStateChanged((user) => {
    if (!user) {
        location.replace("index.html")
    } else {
        document.getElementById("user").innerHTML = "Logged-in as " + user.email
    }
})
function logout() {
    firebase.auth().signOut()
}