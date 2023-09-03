function showLogin() {
    document.getElementById("login").style.display = "block";
}

function hideLogin() {
    document.getElementById("login").style.display = "none";
}

function showRegistration() {
    document.getElementById("registration").style.display = "block";
}

function hideRegistration() {
    document.getElementById("registration").style.display = "none";
}

function isValidEmail(email) {
    var pattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    return pattern.test(email);
}

function isValidPassword(password) {
    // Minimum 8 characters, at least one uppercase letter, 
    // one lowercase letter, one number and one special character
    var pattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$/;
    return pattern.test(password);
}

function isValidPassword(password) {
    // Minimum 8 characters, at least one uppercase letter, 
    // one lowercase letter, and one number
    var pattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$/;
    return pattern.test(password);
}

function validateAndRegister() {
    if (validateRegistration()) {
        registerUser();
    }
}

function validateRegistration() {
    let name = document.querySelector("[name='name']").value;
    let email = document.querySelector("[name='email-register']").value;
    let password = document.querySelector("[name='password-register']").value;
    let repassword = document.querySelector("[name='repassword']").value;


    if (!name || !email || !password || !repassword) {
        alert('All fields are mandatory.');
        return false;
    }

    if (password !== repassword) {
        alert('Passwords do not match.');
        return false;
    }

    if (!isValidEmail(email)) {
        alert('Please enter a valid email address.');
        return false;
    }

    if (!isValidPassword(password)) {
        alert('Password should have a minimum length of 8 characters and contain at least one uppercase letter, one lowercase letter and one number.');
        return false;
    }

    // Further validations like email format, password strength can be added here
    console.log('Validation is succefful!')
    return true;
}

function registerUser() {
    let formData = new FormData(document.querySelector('#registrationForm'));

    fetch('/department/registrate/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            console.log('HELLO')
            hideRegistration();
            showLogin();
            alert("Successfully registered!");
        } else {
            alert("Error: " + data.error);
        }
    })
    .catch(error => {
        console.error("There was an error with the registration:", error);
    });
}

function validateLogin(event) {
    event.preventDefault();  // Prevent the default form submission

    let email = document.querySelector("input[name='email-login']").value;
    let password = document.querySelector("input[name='password-login']").value;

    // AJAX call to send the login data
    $.ajax({
        url: '/department/login/',
        method: 'POST',
        data: {
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            email: email,
            password: password,
        },
        success: function(response) {
            if (response.success) {
                // You can redirect the user or show a success message
                hideLogin();  // Example redirect
            } else {
                alert(response.error);
            }
        }
    });
}