const loginForm = document.getElementById('loginForm');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const errorAlert = document.getElementById('errorAlert');
const errorMessage = document.getElementById('errorMessage');

loginForm.addEventListener('submit', function (e) {
  e.preventDefault();

  const email = emailInput.value.trim();
  const password = passwordInput.value.trim();

  if (!email || !password) {
    errorMessage.textContent = 'Please enter both email and password';
    errorAlert.classList.remove('hidden');
  } else {
    errorAlert.classList.add('hidden');
    console.log('Login attempted with:', email, password);
    // Add your login logic here
  }
});