// State for subjects
const oLevelSubjects = Array.from({ length: 8 }, (_, i) => ({ id: i + 1, subject: "", grade: "" }));
const oLevelSubjects1 = Array.from({ length: 8 }, (_, i) => ({ id: i + 1, subject: "", grade: "" }));

// Populate Subjects Table
const subjectsTable = document.getElementById("subjectsTable");
const subjectsTable1 = document.getElementById("subjectsTable1");

oLevelSubjects.forEach(({ id }) => {
  const row = document.createElement("tr");
  row.innerHTML = `
    <td class="px-4 py-2 text-sm text-gray-700">${id}</td>
    <td class="px-4 py-2">
      <input
        type="text"
        data-id="${id}"
        data-field="subject"
        name="subject"
        class="block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
      />
    </td>
    <td class="px-4 py-2">
      <input
        type="text"
        data-id="${id}"
        data-field="grade"
        name="grade"
        class="block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
      />
    </td>
  `;
  subjectsTable.appendChild(row);
});

oLevelSubjects1.forEach(({ id }) => {
  const row = document.createElement("tr");
  row.innerHTML = `
    <td class="px-4 py-2 text-sm text-gray-700">${id}</td>
    <td class="px-4 py-2">
      <input
        type="text"
        data-id="${id}"
        data-field="subject1"
        name="subject1"
        class="block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
      />
    </td>
    <td class="px-4 py-2">
      <input
        type="text"
        data-id="${id}"
        data-field="grade1"
        name="grade1"
        class="block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
      />
    </td>
  `;
  subjectsTable1.appendChild(row);
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
            data-id="${subject.id}"
            data-field="asubject1"
            name="asubject1"
            onchange="handleALevelSubjectChange(${subject.id}, 'subject', this.value)"
          />
        </td>
        <td class="px-4 py-2 border border-gray-300">
          <input
            type="text"
            class="block w-full px-2 py-1 border border-gray-300 rounded-md"
            value="${subject.grade}"
            data-id="${subject.id}"
            data-field="agrade1"
            name="agrade1"
            onchange="handleALevelSubjectChange(${subject.id}, 'grade', this.value)"
          />
        </td>
      `;
      aLevelSubjectsTable.appendChild(row);
    });
  });

  function toggleSecondSitting() {
    const secondSitting = document.getElementById('secondSitting');
    const isTwoSittings = document.querySelector('input[name="sitting"]:checked').value === 'two';
    secondSitting.style.display = isTwoSittings ? 'block' : 'none';
  }