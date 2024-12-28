let selectedProgram = "";
const hasExistingApplication = true; // Change this to `false` if no existing application

function handleSelectChange(event) {
  selectedProgram = event.target.value;
  document.getElementById('start-application-btn').disabled = !selectedProgram;
}

function handleStartApplication() {
  if (!selectedProgram) return;
  console.log('Starting application for program:', selectedProgram);
  alert('Application started for program: ' + selectedProgram);
}

function handleContinueApplication() {
  console.log('Continuing existing application');
  alert('Continuing existing application');
}

// Show the continue button if there's an existing application
if (hasExistingApplication) {
  document.getElementById('continue-application-btn').classList.remove('hidden');
}