import os

states_data = {
    'adamawa': {
        'full_name': 'Adamawa State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Adamawa State has partnered with the SPIN project to drive large-scale agricultural improvements. The state has chosen Model 1, which involves a collaborative partnership with the Federal Government on an existing River Basin Development Authority (RBDA) scheme. To fulfill this objective, Adamawa has selected the Gerio Irrigation Scheme for rehabilitation.</p>

<p class="text-lg text-slate-600 leading-relaxed">The Gerio Irrigation Scheme is located at coordinates Lat: 10.03165° and Long: 11.9549°. The state is currently working with designated focal officers to integrate the project with federal frameworks and ensure smooth execution at the local level.</p>'''
    },
    'bauchi': {
        'full_name': 'Bauchi State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Bauchi State is participating in the SPIN project to enhance its federal-state agricultural partnerships. Operating under Model 1, the state is collaborating directly with the Federal Government on a designated RBDA scheme to improve water distribution and crop yields. The Galala Irrigation scheme is the chosen site for this Model 1 partnership.</p>

<p class="text-lg text-slate-600 leading-relaxed">The Galala Irrigation scheme covers an area located between Latitude 11° 12' 54" N to 11° 14' 42" N and Longitude 9° 40' 30" E to 9° 44' 6" E. State focal officers are actively managing the on-ground coordination to align with the Federal Ministry's broader development goals.</p>'''
    },
    'benue': {
        'full_name': 'Benue State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Benue State, known as the food basket of the nation, is utilizing the SPIN project to upgrade its irrigation networks. By opting for Model 1, Benue is engaging in a strategic partnership with the Federal Government to co-manage an RBDA scheme. The Katsina-Ala Irrigation scheme has been prioritized for this critical infrastructure upgrade.</p>

<p class="text-lg text-slate-600 leading-relaxed">The Katsina-Ala Irrigation scheme is geographically marked at Lat: 7˚8'44''N and Long: 9˚16'47''E. Implementation is being guided by local focal officers who interface between the state agricultural bodies and federal regulators.</p>'''
    },
    'borno': {
        'full_name': 'Borno State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Borno State has joined the SPIN project to revitalize its agricultural sector and promote sustainable farming practices. The state has selected Model 1, choosing to rehabilitate an existing Federal RBDA scheme in partnership with the national government. The Alau Irrigation scheme serves as the cornerstone of this initiative in the state.</p>

<p class="text-lg text-slate-600 leading-relaxed">The Alau Irrigation scheme is situated at coordinates Lat: 11.724423° and Long: 13.285392°. The project is being supported by state focal officers who are committed to executing the project milestones and restoring the region's agricultural capacity.</p>'''
    },
    'ebonyi': {
        'full_name': 'Ebonyi State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Ebonyi State is expanding its rice and general crop production capabilities through its participation in the SPIN project. The state is operating under Model 1, partnering with the Federal Government to enhance a federal RBDA scheme located within its borders. The Ndieze Irrigation scheme has been selected to receive these vital developmental investments.</p>

<p class="text-lg text-slate-600 leading-relaxed">The Ndieze Irrigation scheme is located at Longitude 6° 26' 21'' N and Latitude 8° 18' 14" E. State-appointed focal officers are overseeing the alignment of local farming operations with the overarching federal management structure.</p>'''
    },
    'ekiti': {
        'full_name': 'Ekiti State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Ekiti State is leveraging the SPIN project to maximize the potential of its water resources for agriculture. Under Model 1, the state is collaborating with the Federal Government to rehabilitate an established RBDA scheme, ensuring shared responsibilities and robust funding. The Ogbese Irrigation scheme is the selected project for Ekiti State.</p>

<p class="text-lg text-slate-600 leading-relaxed">The Ogbese Irrigation scheme is found at coordinates Lat: 7.455833° and Long: 5.328334°. The project operations are being liaised by focal officers who ensure that the state's agricultural objectives are met through this federal partnership.</p>'''
    },
    'enugu': {
        'full_name': 'Enugu State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Enugu State is boosting its agricultural output by actively participating in the SPIN project. By adopting Model 1, the state is partnering directly with the Federal Government to manage and improve a federal RBDA scheme. The Ada Rice Irrigation scheme has been carefully selected to undergo rehabilitation under this program.</p>

<p class="text-lg text-slate-600 leading-relaxed">The Ada Rice Irrigation scheme is located at Lat: 6.727763° and Long: 7.015664°. State focal officers are currently coordinating the foundational phases of the project, working to integrate local farmers with the newly improved federal infrastructure.</p>'''
    },
    'kogi': {
        'full_name': 'Kogi State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Kogi State is participating in the SPIN project to enhance its irrigation systems and promote year-round agricultural productivity. Choosing Model 1, the state is working in tandem with the Federal Government to revitalize a targeted RBDA scheme. The Kampe-Omi Irrigation scheme is the designated site for this joint investment.</p>

<p class="text-lg text-slate-600 leading-relaxed">The Kampe-Omi Irrigation scheme is situated at Lat: 8° 34′ and Long: 6° 37'. The project is managed locally by focal officers who are dedicated to ensuring the state meets its co-financing and operational readiness requirements.</p>'''
    },
    'kwara': {
        'full_name': 'Kwara State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Kwara State has embraced the SPIN project as a pathway to significant agricultural growth and sustainability. Under Model 1, Kwara is collaborating with the Federal Government on an RBDA scheme, pooling resources for effective infrastructure rehabilitation. The Duku Lade Irrigation scheme has been chosen as the focal project in the state.</p>

<p class="text-lg text-slate-600 leading-relaxed">The Duku Lade Irrigation scheme is located at coordinates Lat: 8.7888390 and Long: 5.6288770. Coordination is handled by state focal officers who are actively engaged in facilitating the Federal-State partnership.</p>'''
    },
    'nasarawa': {
        'full_name': 'Nasarawa State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Nasarawa State is upgrading its farming capabilities by taking part in the SPIN project. The state is implementing Model 1, focusing on a synergistic partnership with the Federal Government to rehabilitate a federal RBDA scheme. The Doma Irrigation scheme has been selected as the priority site for these interventions.</p>

<p class="text-lg text-slate-600 leading-relaxed">The Doma Irrigation scheme is mapped at Latitude 8° 24'N and Longitude 8° 30'E. The state's assigned focal officers are directing the initial phases of the project, ensuring alignment with both local agricultural needs and federal standards.</p>'''
    },
    'plateau': {
        'full_name': 'Plateau State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Plateau State is utilizing the SPIN project to secure its water supply for extensive agricultural use. By opting for Model 1, Plateau is committing to a collaborative effort with the Federal Government to restore an existing RBDA scheme. The Longkat Irrigation scheme has been identified as the key project for the state.</p>

<p class="text-lg text-slate-600 leading-relaxed">The Longkat Irrigation scheme is positioned at coordinates Lat: 9.154167° and Long: 9.359722°. Implementation and stakeholder engagement are being led by the state's focal officers to ensure the successful rollout of the SPIN initiative.</p>'''
    },
    'cross-river': {
        'full_name': 'Cross-River State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Cross-River State is an active participant in the Sustainable Power and Irrigation for Nigeria (SPIN) project, aiming to boost regional agricultural productivity. The state has opted for Model 2, which focuses on developing and managing a State Irrigation Scheme. Under this model, the state assumes primary responsibility for its irrigation infrastructure and management. To achieve its agricultural targets, Cross-River has officially selected the Bansara Irrigation Scheme for rehabilitation and expansion under the SPIN project.</p>

<p class="text-lg text-slate-600 leading-relaxed">The Bansara Irrigation Scheme is geographically situated at coordinates Lat: 6°30'49.30"N and Long: 8°38'8.80"E. The SPIN project implementation in the state is being spearheaded by the designated state coordinator, Justina John Ulafor. Stakeholders and interested parties can reach the coordinator via email at tinulafor@yahoo.com.</p>'''
    },
    'gombe': {
        'full_name': 'Gombe State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Gombe State has joined the SPIN project to enhance its irrigated agriculture sector and contribute to national food security. The state has chosen to implement Model 2, empowering the state government to take direct ownership and regulatory control over its irrigation and drainage programs. As its flagship project under this initiative, Gombe State has selected the Balanga Irrigation Scheme.</p>

<p class="text-lg text-slate-600 leading-relaxed">The selected Balanga Irrigation Scheme is located at coordinates Lat: 9.851274° and Long: 11.481658°. The state's efforts are being coordinated by Dr. Kabir M. Aliyu. For official inquiries or project updates, the coordinator can be contacted directly via email at mk4aliyu@gmail.com.</p>'''
    },
    'jigawa': {
        'full_name': 'Jigawa State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Dedicated to expanding its agricultural output, Jigawa State is participating in the SPIN project under the Model 2 framework. By selecting this model, Jigawa is committing to the State Irrigation Scheme structure, prioritizing local state governance over its water resources and farming infrastructure. The Warwade Irrigation Scheme has been designated as the state's primary focus for this investment.</p>

<p class="text-lg text-slate-600 leading-relaxed">The Warwade Irrigation Scheme can be found at Latitude: 11° 45' 0''N and Longitude: 9° 13' 0'' E. Overseeing the SPIN project operations in Jigawa is Engr. Alhassan Abbas. The coordinator is available and can be reached via email at alhassandutse@yahoo.com.</p>'''
    },
    'kaduna': {
        'full_name': 'Kaduna State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Kaduna State is leveraging the SPIN project to revitalize its agricultural landscapes. Operating under Model 2, Kaduna is adopting the State Irrigation Scheme approach, ensuring that the state ministry directly regulates and manages the targeted irrigation assets. The Kangimi Irrigation Scheme has been formally selected as the project site to benefit from this initiative.</p>

<p class="text-lg text-slate-600 leading-relaxed">Geographically, the Kangimi Irrigation Scheme is mapped at Lat: 10.629444° and Long: 7.597500°. Engr. Hashimu J. Usman serves as the state coordinator for the SPIN project. He can be contacted for project-related matters by email at engineerhashim50@gmail.com.</p>'''
    },
    'kano': {
        'full_name': 'Kano State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Recognized for its vast agricultural potential, Kano State is participating in the SPIN project through the Model 2 pathway. This State Irrigation Scheme model allows Kano to directly rehabilitate and expand its state-owned dams and irrigation networks. The state has put forward the Jakara Irrigation scheme for development under the program.</p>

<p class="text-lg text-slate-600 leading-relaxed">The Jakara Irrigation project spans the coordinates of 12.20°N – 12.35°N (Latitude) and 8.60°E – 8.75°E (Longitude). The administration of the project is led by the state coordinator, Nuraddeen Isah Abubakar. Interested parties can contact him via phone at 08037562323 or through email at ahmannur2@gmail.com.</p>'''
    },
    'katsina': {
        'full_name': 'Katsina State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Katsina State is committed to improving water management for its farmers through the SPIN project. By selecting Model 2, Katsina assumes responsibility for a State Irrigation Scheme, aiming to optimise local resources and infrastructure for maximum agricultural yield. The Danja Irrigation scheme is the chosen site for the state's SPIN interventions.</p>

<p class="text-lg text-slate-600 leading-relaxed">The Danja Irrigation scheme is located at coordinates Lat: 11.379367° and Long: 7.5599321°. Engr. Shamsudeen S. is acting as the official state coordinator for the project. He can be reached by email at sskafur@gmail.com.</p>'''
    },
    'kebbi': {
        'full_name': 'Kebbi State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Details for Kebbi State will be added soon.</p>'''
    },
    'niger': {
        'full_name': 'Niger State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Niger State is advancing its agricultural infrastructure as a participant in the SPIN project. Participating under Model 2, the state is focused on the State Irrigation Scheme structure to independently manage and improve its regional irrigation assets. To anchor this initiative, Niger State has selected the Rabbah Irrigation scheme.</p>

<p class="text-lg text-slate-600 leading-relaxed">The Rabbah Irrigation scheme's geographic coordinates are Lat: 09°12.189' and Long: 05°02.293'. The implementation is being coordinated by Mansur Aliyu Goro. For further information, the coordinator can be contacted via email at mansurgoro@gmail.com.</p>'''
    },
    'sokoto': {
        'full_name': 'Sokoto State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Sokoto State is utilizing the SPIN project to expand its irrigated land and support local farmers. The state has adopted Model 2, meaning it will oversee the regulatory and operational aspects of a State Irrigation Scheme. The Kware Irrigation scheme has been identified as the core project for Sokoto under this arrangement.</p>

<p class="text-lg text-slate-600 leading-relaxed">The Kware Irrigation scheme is positioned at Lat 13º.4412N and Long 5º.2171°E. Dr. Adamu has been appointed as the state coordinator to oversee the project's progress. He can be contacted via email at damgad83@gmail.com.</p>'''
    },
    'taraba': {
        'full_name': 'Taraba State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Taraba State is a key participant in the SPIN project, aiming to harness its water resources for year-round farming. By choosing Model 2, Taraba operates under the State Irrigation Scheme model, allowing state ministries to drive the rehabilitation efforts. The Lau Irrigation scheme has been selected to receive the SPIN project investments.</p>

<p class="text-lg text-slate-600 leading-relaxed">Geolocated using the coordinates 748434.529 - 750321.225 E and 1015977.426 - 1015932.268 N, the Lau Irrigation scheme represents a significant agricultural hub. The project is managed by Engr. Philip L. Batare, the state coordinator. He can be reached at philipbatare19@gmail.com.</p>'''
    },
    'yobe': {
        'full_name': 'Yobe State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Yobe State is strengthening its resilience against climate variability by participating in the SPIN project. Opting for Model 2, the state is taking charge of a State Irrigation Scheme to directly impact its agricultural output. The Nguru Irrigation scheme has been chosen as the focal point for this developmental initiative.</p>

<p class="text-lg text-slate-600 leading-relaxed">The Nguru Irrigation scheme lies between Longitude 10°10' and 10°35' E, and Latitude 12°35' and 12°57'N. Abdullahi Abba serves as the state coordinator, ensuring the project meets its objectives. Contact can be made by email at abdullahiabba448@gmail.com.</p>'''
    },
    'zamfara': {
        'full_name': 'Zamfara State',
        'content': '''<p class="text-lg text-slate-600 leading-relaxed">Zamfara State is leveraging the SPIN project to modernize its farming practices and secure water availability. The state has selected Model 2, establishing a State Irrigation Scheme that puts local authorities in the driver's seat for asset management. The Natu Irrigation scheme is the selected site for Zamfara's SPIN project operations.</p>

<p class="text-lg text-slate-600 leading-relaxed">The Natu Irrigation scheme is located at coordinates 12°40'9.78"N and 5°53'28.43"E. The state coordinator, Engr. Illyasu Labaran, is leading the project's execution. He is available for correspondence via email at iliyasulabaran@gmail.com.</p>'''
    }
}

base_html = '''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{full_name} | SPIN</title>

  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet" />
  <link rel="icon" type="image/png" href="../images/spin_logo.jpeg" />
  <link rel="shortcut icon" href="../images/spin_logo.jpeg" type="image/jpeg" />
  <link rel="stylesheet" href="../style.css" />
</head>
<body class="antialiased font-sans text-gray-900 bg-white">

  <a href="#main" class="sr-only focus:not-sr-only absolute left-2 top-2 z-[999] rounded bg-white px-3 py-2 text-sm font-semibold shadow outline outline-2 outline-offset-2 outline-[#aaff33]">
    Skip to main content
  </a>

  <div class="bg-white shadow-sm border-b border-gray-100">
    <div class="max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-10 xl:px-16 py-2.5 flex items-center justify-between gap-4 text-sm">
      <a href="../index.html" class="flex items-center gap-3 rounded focus:outline-none focus:ring-2 focus:ring-[#aaff33]">
        <img src="../images/spin_logo.jpeg" alt="SPIN — Sustainable Power Initiative Nigeria" class="h-14 w-auto" />
        <span class="sr-only">Home</span>
      </a>
      <div class="flex items-center space-x-6 md:space-x-8 text-slate-600 text-xs sm:text-sm">
        <div class="flex items-center space-x-2">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-custom-green" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
          <div class="hidden sm:block">
            <p class="text-xs text-gray-500">Call us</p>
            <p class="font-semibold text-black">+2348034432501</p>
          </div>
        </div>
        <div class="flex items-center space-x-2">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-custom-green" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M3 8l7.893-3.893 7.893 3.893a2 2 0 011.107 1.776v7.351a2 2 0 01-2 2H4a2 2 0 01-2-2v-7.351a2 2 0 011.107-1.776zM4 8l8 5 8-5"/></svg>
          <div class="hidden sm:block">
            <p class="text-xs text-gray-500">Send mail</p>
            <p class="font-semibold text-black">info@spinproject.ng</p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <header class="bg-custom-green sticky top-0 z-50 shadow">
    <div class="max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-10 xl:px-16 h-14 grid items-center" style="grid-template-columns: 1fr auto 1fr;">
      <div class="hidden md:block"></div>
      <nav aria-label="Primary" class="hidden md:flex justify-center items-center gap-6 text-[0.95rem] font-semibold relative">
        <a href="../index.html" class="text-white/90 hover:text-white border-b-2 border-transparent hover:border-white px-1.5">Home</a>
        <a href="../about.html" class="text-white/90 hover:text-white border-b-2 border-transparent hover:border-white px-1.5">About us</a>
        <a href="../mandate.html" class="text-white/90 hover:text-white border-b-2 border-transparent hover:border-white px-1.5">Mandate</a>
        <a href="../advertisements.html" class="text-white/90 hover:text-white border-b-2 border-transparent hover:border-white px-1.5">Advertisements</a>
        <a href="../news.html" class="text-white/90 hover:text-white border-b-2 border-transparent hover:border-white px-1.5">News</a>
        <a href="../participating-states.html" class="text-white/90 hover:text-white border-b-2 border-transparent hover:border-white px-1.5">Participating States</a>
        <a href="../gallery.html" class="text-white/90 hover:text-white border-b-2 border-transparent hover:border-white px-1.5">Gallery</a>
        <a href="../project.html" class="text-white/90 hover:text-white border-b-2 border-transparent hover:border-white px-1.5">Projects</a>
        <a href="../resources.html" class="text-white/90 hover:text-white border-b-2 border-transparent hover:border-white px-1.5">Resources</a>
        <a href="../contact.html" class="text-white/90 hover:text-white border-b-2 border-transparent hover:border-white px-1.5">Contact</a>
      </nav>
      <div class="flex justify-end items-center"></div>
      <button id="mobile-menu-button" class="md:hidden absolute -right-4 text-white hover:text-white/90 p-2 rounded focus:outline-none focus:ring-2 focus:ring-[#aaff33]" aria-controls="mobile-menu" aria-expanded="false" aria-label="Open menu">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16m0 6H4"/>
        </svg>
      </button>
    </div>

    <div id="mobile-menu" class="md:hidden hidden border-t border-white/20 bg-custom-green/95 backdrop-blur">
      <div class="max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-10 xl:px-16 py-3 space-y-1 text-white/95">
        <a href="../index.html" class="block py-2 rounded focus:outline-none focus:ring-2 focus:ring-[#aaff33]">Home</a>
        <a href="../about.html" class="block py-2 rounded focus:outline-none focus:ring-2 focus:ring-[#aaff33]">About us</a>
        <a href="../mandate.html" class="block py-2 rounded focus:outline-none focus:ring-2 focus:ring-[#aaff33]">Mandate</a>
        <a href="../advertisements.html" class="block py-2 rounded focus:outline-none focus:ring-2 focus:ring-[#aaff33]">Advertisements</a>
        <a href="../news.html" class="block py-2 rounded focus:outline-none focus:ring-2 focus:ring-[#aaff33]">News</a>
        <a href="../participating-states.html" class="block py-2 rounded focus:outline-none focus:ring-2 focus:ring-[#aaff33]">Participating States</a>
        <a href="../gallery.html" class="block py-2 rounded focus:outline-none focus:ring-2 focus:ring-[#aaff33]">Gallery</a>
        <a href="../project.html" class="block py-2 rounded focus:outline-none focus:ring-2 focus:ring-[#aaff33]">Projects</a>
        <a href="../resources.html" class="block py-2 rounded focus:outline-none focus:ring-2 focus:ring-[#aaff33]">Resources</a>
        <a href="../contact.html" class="block py-2 rounded focus:outline-none focus:ring-2 focus:ring-[#aaff33]">Contact</a>
      </div>
    </div>
  </header>

  <section class="relative w-full h-64 md:h-80 flex items-center justify-center bg-cover bg-center" style="background-image: url('../images/solar2.jpg');">
    <div class="absolute inset-0 bg-gradient-to-r from-green-900/95 to-green-800/70 mix-blend-multiply transition-opacity duration-700"></div>
    <div class="relative z-10 text-center px-4 sm:px-6 transform translate-y-0 opacity-100 transition-all duration-1000 ease-out">
      <nav class="text-sm text-white mb-6 inline-flex items-center gap-2 bg-white/10 backdrop-blur-md px-5 py-2 rounded-full border border-white/20 shadow-lg">
        <a href="../index.html" class="hover:text-[#aaff33] transition-colors">Home</a>
        <span class="text-white/50">/</span>
        <a href="../participating-states.html" class="hover:text-[#aaff33] transition-colors">Participating States</a>
        <span class="text-white/50">/</span>
        <span class="font-semibold text-white">{full_name}</span>
      </nav>
      <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold text-white max-w-4xl mx-auto tracking-tight drop-shadow-md">{full_name}</h1>
    </div>
  </section>

  <main id="main" class="py-20 bg-white">
    <div class="max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-10 xl:px-16 space-y-16">
      <img src="../images/{slug}.png" alt="{full_name} Map" class="w-full rounded-lg shadow-lg mb-8">
      <div class="space-y-6">
        {content}
      </div>
    </div>
  </main>

  <footer class="bg-custom-dark-footer text-white">
    <div class="max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-10 xl:px-16 py-14">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-10 border-b border-white/10 pb-8 mb-8">
        <div>
          <div class="flex items-center space-x-3 mb-3">
            <img src="../images/spin_logo.jpeg" alt="SPIN Project Logo" class="w-12 h-12 object-contain" />
            <h3 class="text-xl font-extrabold tracking-wider text-[#aaff33]">SPIN Project</h3>
          </div>
          <p class="text-sm text-gray-300">Sustainable Power and Irrigation for Nigeria — building a resilient future through integrated water and energy solutions.</p>
        </div>
        <nav aria-label="Quick Links">
          <h4 class="text-base font-bold mb-3">Quick Links</h4>
          <ul class="space-y-2 text-sm">
            <li><a href="../about.html" class="text-gray-300 hover:text-[#aaff33]">About</a></li>
            <li><a href="../mandate.html" class="text-gray-300 hover:text-[#aaff33]">Mandate</a></li>
            <li><a href="../gallery.html" class="text-gray-300 hover:text-[#aaff33]">Gallery</a></li>
            <li><a href="../contact.html" class="text-gray-300 hover:text-[#aaff33]">Contact</a></li>
          </ul>
        </nav>
        <nav aria-label="Resources">
          <h4 class="text-base font-bold mb-3">Resources</h4>
          <ul class="space-y-2 text-sm">
            <li><a href="#" class="text-gray-300 hover:text-[#aaff33]">Project Documents</a></li>
            <li><a href="#" class="text-gray-300 hover:text-[#aaff33]">Reports</a></li>
            <li><a href="#" class="text-gray-300 hover:text-[#aaff33]">News & Updates</a></li>
            <li><a href="../contact.html" class="text-gray-300 hover:text-[#aaff33]">Contact</a></li>
          </ul>
        </nav>
        <div>
          <h4 class="text-base font-bold mb-3">Connect</h4>
          <p class="mt-4 text-xs text-gray-400">Email: <a href="mailto:info@spinproject.ng" class="hover:text-[#aaff33]">info@spinproject.ng</a></p>
        </div>
      </div>
      <p class="text-center text-sm text-gray-400">&copy; 2025 SPIN Project. All rights reserved. Supported by the World Bank.</p>
    </div>
  </footer>

  <script>
    const menuBtn = document.getElementById('mobile-menu-button');
    const menuPanel = document.getElementById('mobile-menu');

    menuBtn?.addEventListener('click', () => {{
      const expanded = menuBtn.getAttribute('aria-expanded') === 'true';
      menuBtn.setAttribute('aria-expanded', String(!expanded));
      menuPanel.classList.toggle('hidden');
    }});
  </script>
</body>
</html>'''

os.makedirs('states', exist_ok=True)

for slug, data in states_data.items():
    html = base_html.format(
        full_name=data['full_name'],
        slug=slug,
        content=data['content']
    )

    with open(f'states/{slug}.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'Created states/{slug}.html')