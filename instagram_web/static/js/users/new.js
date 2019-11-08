let username = document.getElementById("username");
let submit = document.getElementById("submit");
let password = document.getElementById("password");

password.addEventListener("input", function() {
  if (password.value.length >= 6) {
    submit.disabled = false;
  } else {
    submit.disabled = true;
  }
});
