// State for subjects
const oLevelSubjects = Array.from({ length: 8 }, (_, i) => ({ id: i + 1, subject: "", grade: "" }));

// Populate Subjects Table
const subjectsTable = document.getElementById("subjectsTable");
oLevelSubjects.forEach(({ id }) => {
  const row = document.createElement("tr");
  row.innerHTML = `
    <td class="px-4 py-2 text-sm text-gray-700">${id}</td>
    <td class="px-4 py-2">
      <input
        type="text"
        data-id="${id}"
        data-field="subject"
        class="block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
      />
    </td>
    <td class="px-4 py-2">
      <input
        type="text"
        data-id="${id}"
        data-field="grade"
        class="block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
      />
    </td>
  `;
  subjectsTable.appendChild(row);
});

// Handle Form Submission
const oLevelForm = document.getElementById("oLevelForm");
oLevelForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const formData = {
    schoolName: document.getElementById("oLevelSchool").value,
    address: document.getElementById("oLevelAddress").value,
    centre: document.getElementById("oLevelCentre").value,
    fromDate: document.getElementById("oLevelFrom").value,
    toDate: document.getElementById("oLevelTo").value,
    subjects: oLevelSubjects.map(({ id }) => ({
      subject: document.querySelector(`input[data-id="${id}"][data-field="subject"]`).value,
      grade: document.querySelector(`input[data-id="${id}"][data-field="grade"]`).value,
    })),
  };
  console.log("O Level Data:", formData);
});



const formData = {
    aLevel: {
      subjects: [
        { id: 1, subject: '', grade: '' },
        { id: 2, subject: '', grade: '' },
        { id: 3, subject: '', grade: '' }
      ]
    },
    additionalQualification: {
      schoolName: '',
      address: '',
      courseOfStudy: '',
      certificateIssued: '',
      graduatingGrade: '',
      fromDate: '',
      toDate: ''
    }
  };

  function handleALevelSubjectChange(id, field, value) {
    const subject = formData.aLevel.subjects.find(sub => sub.id === id);
    if (subject) subject[field] = value;
    console.log('Updated A-Level Subjects:', formData.aLevel.subjects);
  }

  function handleAdditionalQualificationChange(field, value) {
    formData.additionalQualification[field] = value;
    console.log('Updated Additional Qualification:', formData.additionalQualification);
  }

  document.addEventListener('DOMContentLoaded', () => {
    const aLevelSubjectsTable = document.getElementById('aLevelSubjects');
    formData.aLevel.subjects.forEach((subject) => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td class="px-4 py-2 border border-gray-300">${subject.id}</td>
        <td class="px-4 py-2 border border-gray-300">
          <input
            type="text"
            class="block w-full px-2 py-1 border border-gray-300 rounded-md"
            value="${subject.subject}"
            onchange="handleALevelSubjectChange(${subject.id}, 'subject', this.value)"
          />
        </td>
        <td class="px-4 py-2 border border-gray-300">
          <input
            type="text"
            class="block w-full px-2 py-1 border border-gray-300 rounded-md"
            value="${subject.grade}"
            onchange="handleALevelSubjectChange(${subject.id}, 'grade', this.value)"
          />
        </td>
      `;
      aLevelSubjectsTable.appendChild(row);
    });
  });