function validateForm() {
	var username = document.getElementById("username").value;
	var email = document.getElementById("email").value;
	var password = document.getElementById("password").value;
	var confirm_password = document.getElementById("confirm-password").value;
	//var checkbox = document.getElementById("interesting-topics");

	var checkboxes = document.querySelectorAll('input[type="checkbox"]');
  var checkedCount = 0;

	// if any blank is empty
	if (username == "" || email == "" || password == "" || confirm_password == "") {
		alert("All blanks must be filled");
		return false;
	}

	// if password and confirm password match
	if (password != confirm_password) {
		alert("Password and confirm password must match");
		return false;
	}

	// Check if email is valid
	var email_pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
	if (!email_pattern.test(email)) {
		alert("Please enter a valid email address");
		return false;
	}

	// password must have at least one uppercase, one lowercase, one number, and one special character
	var password_pattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+]).{8,}$/;
	if (!password_pattern.test(password)) {
		alert("Password must have at least one uppercase, one lowercase, one number, and one special character and must be at least 8 characters long");
		return false;
	}
	//check if at least three topics be selected
	//if (!checkbox.checked) {
  //  alert("Please select at least three interesing topics");
  //  return false;
  //}

	// loop through checkboxes to count checked ones
  for (var i = 0; i < checkboxes.length; i++) {
    if (checkboxes[i].checked) {
      checkedCount++;
    }
  }
  
  if (checkedCount != 3) {
    alert("Please select at three interesing topics");
    return false;
  }

	// If all validations pass, return true
	return true;
}
