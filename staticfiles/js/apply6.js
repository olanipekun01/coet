document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('healthDetailsForm');
    const alertBox = document.getElementById('alert');
    const ailmentDetailsContainer = document.getElementById('ailmentDetailsContainer');
    const ailmentDetails = document.getElementById('ailmentDetails');
    let formData = {
      hasAilment: null,
      ailmentDetails: ''
    };
  
    form.addEventListener('change', (e) => {
      if (e.target.name === 'hasAilment') {
        formData.hasAilment = e.target.value;
        if (formData.hasAilment === 'yes') {
          ailmentDetailsContainer.classList.remove('hidden');
          ailmentDetails.required = true;
        } else {
          ailmentDetailsContainer.classList.add('hidden');
          ailmentDetails.value = '';
          formData.ailmentDetails = '';
          ailmentDetails.required = false;
        }
      } else if (e.target.id === 'ailmentDetails') {
        formData.ailmentDetails = e.target.value;
      }
    });
  
    // form.addEventListener('submit', (e) => {
    //   e.preventDefault();
    //   if (!formData.hasAilment || (formData.hasAilment === 'yes' && !formData.ailmentDetails.trim())) {
    //     alert('Please complete all required fields.');
    //     return;
    //   }
    //   console.log('Form submitted:', formData);
    //   alertBox.classList.remove('hidden');
    //   form.reset();
    //   ailmentDetailsContainer.classList.add('hidden');
    //   formData = { hasAilment: null, ailmentDetails: '' };
    // });
  });