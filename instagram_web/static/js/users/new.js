let username = document.getElementById("username");
let submit = document.getElementById("submit");
let password = document.getElementById("password");

password.addEventListener("input", function() {
  if (
    /[a-z]+/.test(password.value) == true &&
    /[A-Z]+/.test(password.value) == true &&
    /[\d]+/.test(password.value) == true &&
    /[\W]+/.test(password.value) == true &&
    /[\s]+/.test(password.value) == false &&
    password.value.length >= 8
  ) {
    submit.disabled = false;
    
  } else {
    submit.disabled = true;
  }
});
