document.getElementById('currentYear').textContent = new Date().getFullYear();

const staffMembers = [
  {
    name: "Dr. John Smith",
    qualification: "Diploma",
    designation: "Dental surgery Technician 1",
    email: "jsmith@achievers.edu.ng",
    image: "/placeholder.svg",
  },
  {
    name: "Florence Adekunle",
    qualification: "N.D",
    designation: "Dental Health Technician",
    email: "fadekunle@achievers.edu.ng",
    image: "/placeholder.svg",
  },
  {
    name: "Victoria Fasuan",
    qualification: "B.Sc.,HND,ND",
    designation: "Confidential Secretary",
    email: "vfasuan@achievers.edu.ng",
    image: "/placeholder.svg",
  },
];

const staffContainer = document.getElementById('staff-container');

staffMembers.forEach((staff) => {
  const staffCard = `
    <div class="overflow-hidden border rounded-lg">
      <div class="grid md:grid-cols-[200px_1fr] gap-6">
        <div class="bg-gray-100">
          <img src="${staff.image}" alt="${staff.name}" class="w-full h-full object-cover">
        </div>
        <div class="p-6">
          <div class="grid grid-cols-[120px_1fr] gap-4 items-baseline">
            <span class="text-gray-500">NAME:</span>
            <span class="font-medium">${staff.name}</span>

            <span class="text-gray-500">QUALIFICATION:</span>
            <span>${staff.qualification}</span>

            <span class="text-gray-500">DESIGNATION:</span>
            <span>${staff.designation}</span>

            <span class="text-gray-500">E-MAIL:</span>
            <a href="mailto:${staff.email}" class="text-blue-600 hover:underline">${staff.email}</a>

            <div class="col-span-2 mt-4">
              <a href="/staff/${staff.name.toLowerCase().replace(/ /g, '-')}" class="text-[#FFA500] hover:text-orange-600 inline-flex items-center">
                → View Details
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  `;
  staffContainer.innerHTML += staffCard;
});