document.getElementById('currentYear').textContent = new Date().getFullYear();

const staffMembers = [
  {
    name: "Professor Ayodele Samuel ONAWUMI ",
    qualification: "B.Sc. M.Sc. Ph.D FNSE. FNIMechE MNISafetyE. COREN Regd",
    designation: "Dean of the College",
    email: "@achievers.edu.ng, ",
    phone: "+234 803 666 9825",
    image: "prof_ayodele_sa.jpg",
  },
  {
    name: "Engr. Dr. Oluwole John FAMORIJI (Associate Professor)",
    qualification: "B.Tech. Electrical and Electronics Engineering (LAUTECH), M.Eng Communication Engineering (FUTA), PhD Electronic Science and Technology (USTC), MIEEE, MNSE, COREN Regd",
    designation: "SubDean of the College, and HOD (Department of Electrical and Information Engineering",
    email: "eie@achievers.edu.ng, famoriji.oj@achievers.edu.ng",
    phone: "+234 816 441 9471",
    image: "engr_Oluwole_jf.png",
  },
  {
    name: "Engr. Prof. B. Kareem",
    qualification: "B.Eng, M.Eng. PhD,  MNSE,  R. Engr., MMSN, FNIEM, MIAENG, MWASET, MAASCIT, FIMPD, FICISE",
    designation: "HOD (Department of Mechanical and Mechatronics Engineering)",
    email: "@achievers.edu.ng",
    phone: "+234 803 373 7251",
    image: "engr_prof_kareem.png",
  },
  {
    name: "Engr. Prof. Sesan Peter Ayodeji",
    qualification: "FNSE",
    designation: "HOD (Department of Biomedical Engineering)",
    email: "@achievers.edu.ng",
    phone: "+234 803 670 9782",
    image: "prof_sesan_pa.jpg",
  },
  {
    name: "Professor David Akinyiwola OPEYEMI",
    qualification: "B.Eng Civil Engineering (Ilorin), M.Eng Structural Engineering (Akure), PhD Engineering (Liverpool, UK), FNSE, FNICE, M.ASCE, COREN Regd",
    designation: "HOD (Department of Civil and Environmental Engineering)",
    email: "@achievers.edu.ng",
    phone: "+234 803 439 8502",
    image: "prof_david_ao.png",
  },
];

const staffContainer = document.getElementById('staff-container');

staffMembers.forEach((staff) => {
  const staffCard = `
    <div class="overflow-hidden border rounded-lg">
      <div class="grid md:grid-cols-[200px_1fr] gap-6">
        <div class="bg-gray-100">
          <img src="/static/assets/${staff.image}" alt="${staff.name}" class="w-full h-full object-cover">
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