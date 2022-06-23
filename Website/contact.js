// Initialize Firebase
var config = {
    apiKey: "AIzaSyBYjQ204RuBhuJFnj0MyAZL6ObfLP0XV1M",
    authDomain: "indian-plagiarism-tool.firebaseapp.com",
    databaseURL: "https://indian-plagiarism-tool-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "indian-plagiarism-tool",
    storageBucket: "indian-plagiarism-tool.appspot.com",
    messagingSenderId: "204343244106",
    appId: "1:204343244106:web:0c11ca4b5de3abd204fdb3"
};
  firebase.initializeApp(config);
  
  // Reference messages collection
  var messagesRef = firebase.database().ref('messages');
  
  // Listen for form submit
  document.getElementById('contactForm').addEventListener('submit', submitForm);
  
  // Submit form
  function submitForm(e){
    e.preventDefault();
  
    //Get value
    var name = getInputVal('name');
    var company = getInputVal('company');
    var email = getInputVal('email');
    var phone = getInputVal('phone');
    var message = getInputVal('message');
  
    // Save message
    saveMessage(name, company, email, phone, message);
  
    // Show alert
    document.querySelector('.alert').style.display = 'block';
  
    // Hide alert after 3 seconds
    setTimeout(function(){
      document.querySelector('.alert').style.display = 'none';
    },3000);
  
    // Clear form
    document.getElementById('contactForm').reset();
  }
  
  // Function to get form value
  function getInputVal(id){
    return document.getElementById(id).value;
  }
  
  // Save message to firebase
  function saveMessage(name, company, email, phone, message){
    var newMessageRef = messagesRef.push();
    newMessageRef.set({
      name: name,
      company: company,
      email: email,
      phone: phone,
      message: message
    });
  }
  