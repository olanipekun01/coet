document.getElementById('currentYear').textContent = new Date().getFullYear();

const staffMembers = [
  {
    name: "Professor Ayodele Samuel ONAWUMI ",
    qualification: "B.Sc. M.Sc. Ph.D FNSE. FNIMechE MNISafetyE. COREN Regd",
    designation: "Dean of the College",
    email: "onawumi.as@achievers.edu.ng, ",
    phone: "+234 803 666 9825",
    image: "https://res.cloudinary.com/dztirmlfv/image/upload/v1738530223/prof_ayodele_sa_o3xm0k.jpg",
    bio: `<p>Engr. Prof. Onawumi, Ayodele Samuel is a Professor of Mechanical Engineering, He holds both the Bachelor of Science (B.Sc.) and Master of Science (M.Sc.) in Industrial Engineering from University of Ibadan and a Doctor of Philosophy (PhD) in Mechanical Engineering from Ladoke Akintola University of Technology, Nigeria,. He is currently the Dean of the College of Engineering and Technology, Achievers University, Owo, Ondo State, Nigeria.</p> <p class='mt-2'>Prof. Onawumi joined the Department of Mechanical Engineering at LAUTECH as an Assistant Lecturer, marking the beginning of a distinguished academic career that saw him rise to the rank of Professor in 2016. During his sojourn as academics Prof. Onawumi, has actively participated in over fifty professional and academic conferences and workshops, both within Nigeria and internationally. His research interest is focused on human factors engineering and applied ergonomics in systems design, manufacturing, and installation. Notably, among the inventions supervised by are the development of a solar power generator equipped with a solar tracker device and the design and construction of an electric generator enclosure aimed at mitigating noise pollution. His research portfolio also includes environmental impact assessments of heavy metals from auto exhaust, ergonomic investigations of selected local fabrications, modelling of anthropometric variables and biomechanics of the human skeletal system.</p> 
          <p class='mt-2'>Prof. Onawumi’s thirst for knowledge and professional accomplishment led him to pursue various international training opportunities. Under the joint India Technical and Economic Cooperation (ITEC), and Special Commonwealth Assistance for Africa Programme (SCAAP) Scholarship, he received specialized training in CNC programming and manufacturing systems in India. Furthering his expertise, he was also awarded TETFund grants to attend courses on Project Management at the Galilee International Management Institute in Israel and on ergonomic and human factors strategic solutions for workplace safety and health at Harvard University's School of Public Health in Boston, USA.</p>
          <p class='mt-2'>His academic achievements include supervising over 200 undergraduate and postgraduate student projects and published more than eighty peer-reviewed articles, conference proceedings, books, and monographs in reputable international and local journals. He has served as reviewer of some local and international peer reviewed journals and conference proceeding with impact factor. He has served as external examiner for several Universities, including the Federal University Oye Ekiti, Redeemer's University, Ede, and Afe Babalola University, Ado Ekiti.</p>
          <p>Prof. Onawumi is a registered engineer with the Council for the Regulation of Engineering in Nigeria (COREN) and Fellow of both the Nigerian Society of Engineers (NSE) and the Nigerian Institution of Mechanical Engineers (NIMechE). He is also a member of the Nigerian Institute of Safety Engineers (NISafetyE), the Nigerian Institute of Industrial Engineers (NIIE), and the African Engineering Education Association (AEEA).</p>` 
    },
  {
    name: "Engr. Dr. Oluwole John FAMORIJI (Associate Professor)",
    qualification: "B.Tech. Electrical and Electronics Engineering (LAUTECH), M.Eng Communication Engineering (FUTA), PhD Electronic Science and Technology (USTC), MIEEE, MNSE, COREN Regd",
    designation: "SubDean of the College, and HOD (Department of Electrical and Information Engineering",
    email: "eie@achievers.edu.ng, famoriji.oj@achievers.edu.ng",
    phone: "+234 816 441 9471",
    image: "https://res.cloudinary.com/dztirmlfv/image/upload/v1738530217/engr_Oluwole_jf_tnbdmr.png",
    bio: `<p>Oluwole John Famoriji received the B.Tech. Degree in Electrical and Electronic Engineering from the Ladoke Akintola University of Technology, Ogbomosho, Nigeria, in 2009, the M.Eng. Degree in Communications Engineering from the Federal University of Technology Akure, Nigeria, in 2014, and the Ph.D. Degree in Electronic Science and Technology from the University of Science and Technology of China (USTC), Hefei, China, in 2019. He is currently an Associate Professor in the Department of Electrical and Information Engineering, Achievers University, Owo, Nigeria, and a Senior Research Fellow with the University of Johannesburg, South Africa. His research interests include signals and systems, array processing, electromagnetic sensing, antennas, and propagation. He was a recipient of one of the Best Paper and Oral Presentation Award from the 2018 IEEE International Conference on Integrated Circuits and Technology Applications (ICTA), Beijing, China; and the 2016 Innovation Spirit Award of the Micro-/Nano Electronics System Integration Centre of the University of Science and Technology of China. He is a member of the IEEE International Conference on Ubiquitous Wireless Broadband Technical Committee member (2017-2018). In addition, he Presented papers and chaired a Session at the 2024 International Conference on Electrical, Computer and Energy Technologies (2024 ICECET), Sydney, Australia. He is a CAS-TWAS Scholar.</p>
          <p class='mt-2'>Dr. Famoriji has been an IEEE Member, NSE Member, COREN Regd., and regularly invited to review papers submitted to international journals (the IEEE TAP, the IEEE ACCESS, the IEEE TCS, the IEEE TEMC, the IEEE TIM, the IEEE Sensors, the Journal of Electromagnetic Waves and Applications, the IET Communications, the IET MAP, the International Journal of Electronics, and so on) and International books (Wiley, Springer, Intech Science, and so on). Supervised undergraduate projects, master’s research, and Co-supervising PhD students. </p>`
  },
  {
    name: "Engr. Prof. B. Kareem",
    qualification: "B.Eng, M.Eng. PhD,  MNSE,  R. Engr., MMSN, FNIEM, MIAENG, MWASET, MAASCIT, FIMPD, FICISE",
    designation: "HOD (Department of Mechanical and Mechatronics Engineering)",
    email: "kareem.b@achievers.edu.ng",
    phone: "+234 803 373 7251",
    image: "https://res.cloudinary.com/dztirmlfv/image/upload/v1738530218/engr_prof_kareem_zud5mu.png",
    bio: `<p>Engr. Prof. B. Kareem, B.Eng, M.Eng. PhD,  MNSE,  R. Engr., MMSN, FNIEM, MIAENG, MWASET, MAASCIT, FIMPD, FICISE, specializes in Mechatronics Systems Design, Optimization, and Management;  Systems Engineering, Industrial Engineering; Production Engineering; Operations Research, Systems Modeling, Artificial Intelligence, Automotive systems and Engineering Failure Analysis. He has published extensively in several reputable journal outlets in his areas of specialization. He has supervised to completion several M. Eng. and Ph.D. students in the field.  He has won many research grants nationally and internationally. As academic   and researcher, he has visited and has been an external examiner to many universities around the globe. Apart from being an academic, he has a good industrial experience and at the same time an  administrator per excellence. </p>`
  },
  {
    name: "Engr. Prof. Sesan Peter Ayodeji",
    qualification: "FNSE",
    designation: "HOD (Department of Biomedical Engineering)",
    email: "spayodeji@achievers.edu.ng",
    phone: "+234 803 670 9782",
    image: "https://res.cloudinary.com/dztirmlfv/image/upload/v1738530225/prof_sesan_pa_oiynbx.jpg",
    bio: `<p>Engr. Professor Sesan Peter AYODEJI FNSE, is a Professor of Mechanical Engineering with specialization in Machine & Process Design and Applied Ergonomics. He obtained B.Eng, M.Eng and PhD degree certificates in Mechanical Engineering in 1999, 2003 and 2009 respectively from the Federal University of Technology, Akure (FUTA), Ondo State, Nigeria. He was at the Tshwane University of Technology, Pretoria, South Africa for a year Postdoctoral programme in the Department of Industrial Engineering between 2012 and 2013. He registered as an engineer with the Council for the Regulation of Engineering in Nigeria (COREN) and a Fellow of the Nigerian Society of Engineers (FNSE), International Association of Engineers (IAENG), Nigerian Institution of Mechanical Engineers (NiMechE), Material Society of Nigeria (MMSN) and Nigerian Institution of Engineering Management (MNIEM).</p>
          <p class='mt-2'>Engr. Prof. Ayodeji joined the services of Federal University of Technology, Akure over two decades ago and has since then been continuously engaged in teaching, research and community service.  He had also demonstrated administrative leadership in the University over the years, having creditably served at several capacities such as: Departmental Examination Officer, Postgraduate coordinator, member of the University Postgraduate Board, Sub-Dean (PGD) for School of Postgraduate Studies, member of Business Committee of Senate, member of senate and pioneer Head of Department of Industrial and Production Engineering. He was the Editor- in- Chief of FUTA Journal of Engineering and Engineering Technology for four years and Chairman Local Organizing Committee for School of Engineering and Engineering Technology Annual Conference, FUTA. He served as a member of 40th Anniversary Alumni Industrial Linkage Publicity Task Force and currently serving as a Member of FUTA-NASENI Memorandum of Understanding Implementation Committee. He had served and still serving as a reviewer to several journals both within and outside the country. He was the Dean, College of Engineering and Technology, Achievers University, Owo, Ondo State as a Visiting Professor between year 2021 and October 2024 and He was appointed the Squadron Leader of Special Road Traffic Mayors by the Ondo State Government in 2021.</p>
          <p class='mt-2'>He had successfully supervised several Undergraduate and Postgraduate Diploma projects, supervised over forty postgraduate (PhD and Masters) students of Engineering theses to completion and several others at various stages of completion. He had published over ninety (90) scientific papers in reputable journals both nationally and internationally and attended various conferences. He had published book chapters in refereed and edited books. He had developed several machines among which are; planetary mixer for small scale paint  production industry; Leg and Arm Exercise Machine; Push Crank Mechanism Off-Road Wheel Chair’ ; an adaptive Left Throttling Pedal for V-Boot Wagon 230 for Right Leg Paraplegic Patient; Hospital Meal Carts; Battery Powered Vehicle for Children Amusement Park using Nigerian Anthropometry Parameters; Automated Page Turning Machine; tricycle for the paraplegics; Body Mass Index (BMI) and Waist-hip Ratio (WHR) Measuring Device; processing plants for poundo yam production; A Dual - Purpose Wheelchair for Covid-19 Paraplegic Patients Using Nigerian Anthropometry Data; A Form - Fill Sealing Machine for Roselle Particulate Process Plant; Processing Plant for the Production of Vegetable Leaf Powder; and process plant for plantain flour production among others.</p>
          <p class='mt-2'>He is a Joint winner of the prestigious 2022 Nigeria Prize for Science award by Nigeria LNG Limited with reference number NLNG/ER/ERP/2022/9/289 on the Development of a Process Plant for Plantain Flour. He had four (4) inventions patented in Nigeria.</p>
          <p class='mt-2'>He lead the team that developed the prototype of a positive pressure ventilator for FUTA as part of contributions to the fight against COVID-19 in 2020 which was published in two national dailies (Tribune page 5 and The Nation page 2) on Wednesday 3 June, 2020.</p>
          <p class='mt-2'>His ongoing works include: Artificial Intelligence Application in a Reconfigurable Leather Cutting Machine; Multi-functional Particulates Packaging Machine; a Mechatronically Controlled Upper and Lower Limbs Post-stroke Rehabilitation Machine; Patients’ Suction Machine using voice recognition principle and Automated Plant for Processing African Locust Beans into Food Seasonings. He specializes in, Machine & System Design and Applied Ergonomics</p>
          <p class='mt-2'>He had won a number of research grants and awards to his credit such as 2023 AGIP Research Grant for Establishing Centre for Maintenance Engineering at the Federal University of Technology, Akure, Ondo State (awaiting implementation); Tertiary Education Trust Fund (TETFund) Research Grants Intervention, 2017; International Development Association towards the course of Science and Technology Education Post Basic Project (STEP-B) Research Grant award, 2008; and University Research Grant of The Federal University of Technology, Akure, 2007.</p>`
  },
  {
    name: "Professor David Akinyiwola OPEYEMI",
    qualification: "B.Eng Civil Engineering (Ilorin), M.Eng Structural Engineering (Akure), PhD Engineering (Liverpool, UK), FNSE, FNICE, M.ASCE, COREN Regd",
    designation: "HOD (Department of Civil and Environmental Engineering)",
    email: "@achievers.edu.ng",
    phone: "+234 803 439 8502",
    image: "https://res.cloudinary.com/dztirmlfv/image/upload/v1738530224/prof_david_ao_mouxza.png",
    bio: `<p>Engr. Prof. David Opeyemi is an experienced Civil and Structural Engineer, Researcher and Lecturer with a demonstrated history of working in the construction and research industry. His varied experiences in the engineering and academic worlds have shown him to be skilled in research, strategic planning, lecturing, teaching, and higher education. He is an engineer par excellence who holds a Doctor of Philosophy (PhD) in Engineering from the University of Liverpool, in the United Kingdom.</p>
           <p class='mt-2'>His major contribution is on stochastic and non-traditional uncertainty models in engineering with emphasis on reliability analysis, risk analysis and robust design, which is utilized to address engineering challenges arising from environmental changes with a multi-disciplinary view. He has put his knowledge to work by collaborating with many researchers at local and international levels leading to research grants, technical exchange, and many research articles. This also led to the presentation of his research work in Nigeria, South Africa, Canada, United Kingdom, Switzerland, Russia, and China (four continents). He has been actively involved in construction, design, and supervision of various Civil and Structural Engineering works for more than three decades. His journey in the engineering world took off in the year 1985 as an Engineer-in-training with the Federal Ministry of Works and Housing. The journey has spanned stints as Engineering Technician, Pupil Engineer, Project Engineer, and Project Manager with different notable national and international firms.</p>
           <p class='mt-2'>His foray into the academic world where he has been teaching, nurturing, and training budding engineers started in the year 2005 at the Department of Civil Engineering as a Lecturer II at the state-owned Rufus Giwa Polytechnic, Owo. He rose through the ranks before leaving the services of the Polytechnic in the year 2018 as a Principal Lecturer. Thereafter, he transferred his services to the Olusegun Agagu University of Science and Technology, Okitipupa (formerly Ondo State University of Science and Technology), as a Senior Lecturer in the year 2018, and Reader (Associate Professor) in 2022. His administrative experience includes acting Head of Departments, Chairmen of many committees, member of Senate and University Governing Council. He has worked as adjunct and visiting lecturer at several institutions including Landmark University, Omu Aran, Kwara State, Joseph Ayo Babalola University, Ikeji Arakeji, Osun State and Federal University of Oye-Ekiti, Ekiti State.</p>
           <p class='mt-2'>Supervised undergraduate, master’s and PhD students’ projects and research; and has served as external examiner to Institutions. Prof. Opeyemi, is a member of many national and global bodies among which are: Registered Engineer by the Council for the Regulation of Engineering in Nigeria (COREN); Fellow of both Nigerian Society of Engineers and Nigerian Institution of Civil Engineers; Member, American Society of Civil Engineers; Member, International Association for Bridge and Structural Engineering; Member, Nigerian Institution of Civil Engineers; Senior Member, International Union of Laboratories and Experts in Construction Materials; Member, International Association of Engineers; and Member, International Civil Engineering Risk and Reliability Association (CERRA), among others.</p>`
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
            <a href="mailto:${staff.email}" class="text-[#04481b] hover:underline">${staff.email}</a>

            
          </div>
         
        </div>

        <div class="col-span-2 mt-1 px-5 py-5">
          <button class="text-[#04481b] inline-flex items-center accordion">
            → View Details
          </button>
          <div class="panel hidden">
            <p>${staff.bio}</p>
          </div>
        </div>

      </div>
    </div>
  `;
  staffContainer.innerHTML += staffCard;
});