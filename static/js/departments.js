document.getElementById('currentYear').textContent = new Date().getFullYear();

    const departments = [
    {
      name: "Department of Biomedical Engineering",
      description: "Lorem ipsum dolor sit amet conse iusto dolorum animi temporibus similique nobis praesentium quasi qui. Accusamus.",
      image: "/placeholder.svg?height=300&width=400",
    },
    {
      name: "Department of Civil and Environmental Engineering",
      description: "Lorem ipsum dolor sit amet conse iusto dolorum animi temporibus similique nobis praesentium quasi qui. Accusamus.",
      image: "/placeholder.svg?height=300&width=400",
    },
    {
      name: "Department of Electrical & Information Engineering",
      description: "Lorem ipsum dolor sit amet conse iusto dolorum animi temporibus similique nobis praesentium quasi qui. Accusamus.",
      image: "/placeholder.svg?height=300&width=400",
    },
    {
      name: "Department of Mechanical and Mechatronics Engineering",
      description: "Lorem ipsum dolor sit amet conse iusto dolorum animi temporibus similique nobis praesentium quasi qui. Accusamus.",
      image: "/placeholder.svg?height=300&width=400",
    },
   
  ];

  const departmentContainer = document.getElementById("departments");

  departments.forEach((dept) => {
    const card = document.createElement("div");
    card.className = "overflow-hidden border rounded-lg shadow-md";

    card.innerHTML = `
      <img src="${dept.image}" alt="${dept.name}" class="w-full h-48 object-cover">
      <div class="p-6">
        <h2 class="text-xl font-bold mb-2">${dept.name}</h2>
        <p class="text-gray-600 mb-4">${dept.description}</p>
        <a 
          href="/departments/${dept.name.toLowerCase().replace(/\s+/g, '-')}" 
          class="text-[#04481b] hover:text-[#00923f] flex items-center"
        >
          Learn More
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </a>
      </div>
    `;

    departmentContainer.appendChild(card);
  });