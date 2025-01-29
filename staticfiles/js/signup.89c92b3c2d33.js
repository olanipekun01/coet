const form = document.getElementById('registerForm');
const errorAlert = document.getElementById('errorAlert');
const successAlert = document.getElementById('successAlert');
const errorMessage = document.getElementById('errorMessage');

form.addEventListener('submit', (e) => {
  e.preventDefault();

  const formData = {
    firstName: form.firstName.value.trim(),
    lastName: form.lastName.value.trim(),
    email: form.email.value.trim(),
    password: form.password.value.trim(),
    confirmPassword: form.confirmPassword.value.trim(),
  };

  // Validation
  if (Object.values(formData).some((value) => value === '')) {
    showError('Please fill out all fields');
    return;
  }
  if (formData.password !== formData.confirmPassword) {
    showError('Passwords do not match');
    return;
  }

  // Clear error and show success
  hideError();
  showSuccess();

  console.log('Registration attempted with:', formData);
});

function showError(message) {
  errorAlert.classList.remove('hidden');
  successAlert.classList.add('hidden');
  errorMessage.textContent = message;
}

function hideError() {
  errorAlert.classList.add('hidden');
}

function showSuccess() {
  successAlert.classList.remove('hidden');
}