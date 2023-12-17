var toggleButton = document.getElementById("toggleButton");
var passwordInput = document.getElementById("passwordInput");

toggleButton.addEventListener("click", function(event) {
event.preventDefault();
if (passwordInput.type === "password")
{
  passwordInput.type = "text";
}
else
{
  passwordInput.type = "password";
}
});