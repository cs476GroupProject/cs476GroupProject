function validateForm() {
	var email = document.getElementById("email").value;

	// if email is empty
	if (email == "") {
		alert("Email is empty");
		return false;
	}

	// Check if email is valid
	var email_pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
	if (!email_pattern.test(email)) {
		alert("Please enter a valid email address");
		return false;
	}

	return true;
}