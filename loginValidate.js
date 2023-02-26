function validateForm() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  
  // check if username and password are not empty
  if (username == "" || password == "") {
    alert("Please enter the username and password");
    return false;
  }
  
  // check if username and password match expected values
  if (username !== "username" || password !== "password") {
    alert("Incorrect username or password");
    return false;
  }
  
  return true;
}