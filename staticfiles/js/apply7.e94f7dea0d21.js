// document.getElementById('declarationForm').addEventListener('submit', function (e) {
//     e.preventDefault();
  
//     const fullName = document.getElementById('fullName').value;
//     const consent = document.querySelector('input[name="consent"]:checked')?.value;
//     const bankName = document.getElementById('bankName').value;
//     const amount = document.getElementById('amount').value;
//     const date = document.getElementById('date').value;
//     const receiptNumber = document.getElementById('receiptNumber').value;
//     const heardFrom = document.getElementById('heardFrom').value;
  
//     if (consent !== 'yes') {
//       alert('You must consent to the declaration to proceed.');
//       return;
//     }
  
//     const formData = {
//       fullName,
//       consent,
//       bankName,
//       amount,
//       date,
//       receiptNumber,
//       heardFrom,
//     };
  
//     console.log('Form submitted:', formData);
  
//     document.getElementById('alert').classList.remove('hidden');
//     setTimeout(() => {
//       document.getElementById('alert').classList.add('hidden');
//     }, 3000);
  
//     // Optionally reset the form
//     this.reset();
// });