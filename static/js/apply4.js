document.getElementById('entry-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);
    console.log('Form submitted:', data);
  });

  const inputs = document.querySelectorAll('input[type="number"]');
  inputs.forEach(input => {
    input.addEventListener('input', () => {
      let total = 0;
      inputs.forEach(input => {
        total += parseInt(input.value || 0, 10);
      });
      document.getElementById('totalScore').innerText = total;
    });
  });