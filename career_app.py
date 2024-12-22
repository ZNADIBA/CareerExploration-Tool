import streamlit as st

# Title of the app
st.title("Career Exploration Tool")

# Greet the user
st.header("Welcome, Future Professional! 👑👑👑")
st.write("""
Welcome to the Career Exploration Tool! 🚀🌟 Here, we’ll help you discover various careers based on your interests. Each career listed provides average salary ranges for every country, but keep in mind that these can vary greatly depending on the location, industry, and level of experience. Salaries may be higher in some countries or regions, and it's important to consider local job markets when making your career choice. 

Every profession comes with great responsibilities, but they also offer the chance to make a significant difference in the world. And remember, there are many more professions beyond what we’ve listed here! Let’s get started!
""")

# Ask for user input
name = st.text_input("What's your name, future professional?")
age = st.number_input("How old are you?", min_value=5, max_value=100, step=1)

# Ask what area they are interested in
career_area = st.selectbox("Which area are you interested in?", 
                           ["Healthcare", "Technology", "Business", "Creative Arts", "Education", "Engineering", 
                            "Psychology and Therapy", "Criminal Justice and Legal Studies"])

# Display a friendly message with advice for professionals
st.write("""
### Career Advice for All Professionals
No matter which career path you choose, remember that success requires dedication, passion, and continuous learning. Each profession brings its own set of challenges, but overcoming them can be incredibly rewarding. Always be prepared to grow, adapt, and contribute to the world in your own unique way. And don’t forget – your work has the potential to impact not only your life but the lives of others around you. 🌟

### Salary Considerations
Salaries for different careers can vary greatly from country to country. The figures we provide are based on average salaries for each profession, but local job markets, demand, and your experience level can significantly influence your earning potential. Always consider these factors when making decisions about your career.

Good luck on your journey, and remember: there’s always more to explore!
""")


# Career details dictionary
career_details = {
    "Healthcare": {
        "Doctor": {
            "Key Responsibilities": [
                "Diagnose and treat illnesses and injuries.",
                "Prescribe medications and treatments.",
                "Monitor patient progress and maintain records.",
                "Specialize in areas like pediatrics, cardiology, or neurology."
            ],
            "Average Salary (Globally)": "$150,000 - $300,000 annually (varies by country).",
            "Education Requirements": "Bachelor's degree in Medicine, followed by a Doctor of Medicine (MD) or equivalent.",
            "Advice": "Develop strong communication skills and stay updated with medical advancements."
        },
        "Nurse": {
            "Key Responsibilities": [
                "Provide essential care to patients.",
                "Administer medications and treatments.",
                "Monitor patient health and maintain medical records.",
                "Assist doctors during procedures."
            ],
            "Average Salary (Globally)": "$40,000 - $80,000 annually (varies by specialization and country).",
            "Education Requirements": "Bachelor's degree in Nursing (BSN) or equivalent.",
            "Advice": "Build empathy and resilience. Gain experience in different healthcare settings."
        },
        "Pharmacist": {
            "Key Responsibilities": [
                "Dispense prescription medications.",
                "Provide advice on proper medication use.",
                "Monitor patients for side effects and interactions.",
                "Maintain accurate patient medication records."
            ],
            "Average Salary (Globally)": "$90,000 - $120,000 annually.",
            "Education Requirements": "Doctor of Pharmacy (PharmD) degree.",
            "Advice": "Stay current with drug research and be detail-oriented."
        },
        "Physical Therapist": {
            "Key Responsibilities": [
                "Help patients improve movement and manage pain.",
                "Develop personalized rehabilitation programs.",
                "Monitor patient progress and adjust treatments.",
                "Educate patients on exercises and healthy practices."
            ],
            "Average Salary (Globally)": "$70,000 - $90,000 annually.",
            "Education Requirements": "Doctoral or professional degree in physical therapy.",
            "Advice": "Be patient and develop strong interpersonal skills."
        },
        "Radiologic Technologist": {
            "Key Responsibilities": [
                "Perform diagnostic imaging procedures like X-rays and MRIs.",
                "Ensure patient safety during imaging.",
                "Maintain equipment and ensure quality control.",
                "Assist physicians in interpreting images."
            ],
            "Average Salary (Globally)": "$55,000 - $80,000 annually.",
            "Education Requirements": "Associate's degree or bachelor's degree in radiologic technology.",
            "Advice": "Attention to detail and technical expertise are key."
        },
        "Dentist": {
            "Key Responsibilities": [
                "Examine and treat dental issues.",
                "Perform dental procedures like fillings, cleanings, and extractions.",
                "Provide oral health education to patients.",
                "Manage patient records and ensure comfort during procedures."
            ],
            "Average Salary (Globally)": "$130,000 - $250,000 annually.",
            "Education Requirements": "Bachelor's degree in Dentistry, followed by a Doctor of Dental Surgery (DDS) or Doctor of Dental Medicine (DMD).",
            "Advice": "Develop strong hand-eye coordination and patient care skills."
        },
        "Medical Laboratory Technician": {
            "Key Responsibilities": [
                "Conduct laboratory tests on samples (blood, tissue, etc.).",
                "Analyze results and prepare reports for physicians.",
                "Ensure lab equipment is maintained and calibrated.",
                "Follow strict protocols for handling samples."
            ],
            "Average Salary (Globally)": "$50,000 - $70,000 annually.",
            "Education Requirements": "Associate's degree in medical laboratory technology.",
            "Advice": "Be detail-oriented and understand laboratory safety protocols."
        },
        "Optometrist": {
            "Key Responsibilities": [
                "Examine eyes and diagnose vision problems.",
                "Prescribe corrective lenses and eye treatments.",
                "Monitor eye health and detect conditions like glaucoma.",
                "Educate patients on eye care and protection."
            ],
            "Average Salary (Globally)": "$100,000 - $150,000 annually.",
            "Education Requirements": "Doctor of Optometry (OD) degree.",
            "Advice": "Develop strong communication skills and stay current with eye care research."
        },
        "Psychiatrist": {
            "Key Responsibilities": [
                "Diagnose and treat mental health disorders.",
                "Prescribe medications and therapy treatments.",
                "Monitor patients' mental health progress.",
                "Provide counseling and therapy services."
            ],
            "Average Salary (Globally)": "$200,000 - $300,000 annually.",
            "Education Requirements": "Bachelor's degree, followed by medical school and residency in psychiatry.",
            "Advice": "Empathy and a strong understanding of mental health are crucial."
        },
        "Health Educator": {
            "Key Responsibilities": [
                "Promote healthy lifestyles through education.",
                "Develop and implement health programs.",
                "Advise individuals on managing chronic conditions.",
                "Conduct research to improve public health outcomes."
            ],
            "Average Salary (Globally)": "$50,000 - $70,000 annually.",
            "Education Requirements": "Bachelor's degree in public health or health education.",
            "Advice": "Strong communication and organizational skills are essential."
        },
        "Surgical Technician": {
            "Key Responsibilities": [
                "Assist in surgeries by preparing equipment and sterilizing instruments.",
                "Prepare patients for surgery.",
                "Monitor patients' vital signs during surgery.",
                "Provide support to the surgical team during procedures."
            ],
            "Average Salary (Globally)": "$45,000 - $70,000 annually.",
            "Education Requirements": "Associate's degree in surgical technology.",
            "Advice": "Stay calm under pressure and develop attention to detail."
        },
        "Anesthesiologist Assistant": {
            "Key Responsibilities": [
                "Assist anesthesiologists in administering anesthesia during surgeries.",
                "Monitor patients' vital signs during anesthesia.",
                "Prepare anesthesia equipment and ensure safety protocols are followed.",
                "Document anesthesia records."
            ],
            "Average Salary (Globally)": "$100,000 - $150,000 annually.",
            "Education Requirements": "Master's degree in anesthesiology or related field.",
            "Advice": "Stay focused under pressure and ensure patient safety."
        },
        "Speech-Language Pathologist": {
            "Key Responsibilities": [
                "Assess, diagnose, and treat speech, language, and communication disorders.",
                "Develop personalized therapy plans.",
                "Help patients improve communication skills and swallowing disorders.",
                "Work with individuals across various age groups."
            ],
            "Average Salary (Globally)": "$70,000 - $90,000 annually.",
            "Education Requirements": "Master's degree in Speech-Language Pathology.",
            "Advice": "Develop strong communication and empathy skills."
        },
        "Genetic Counselor": {
            "Key Responsibilities": [
                "Advise individuals and families on genetic conditions.",
                "Interpret genetic test results and provide guidance.",
                "Support patients in understanding their risk of inherited conditions.",
                "Work with doctors to create personalized care plans."
            ],
            "Average Salary (Globally)": "$70,000 - $100,000 annually.",
            "Education Requirements": "Master's degree in genetic counseling or related field.",
            "Advice": "Stay updated on genetic research and developments."
        },
        "Occupational Therapist": {
            "Key Responsibilities": [
                "Help patients improve their ability to perform daily tasks.",
                "Develop personalized rehabilitation plans.",
                "Assess patients' physical and mental capabilities.",
                "Work with patients to enhance their independence."
            ],
            "Average Salary (Globally)": "$60,000 - $85,000 annually.",
            "Education Requirements": "Master's degree in occupational therapy.",
            "Advice": "Patience and creativity are key when helping patients."
        },
    },
    "Technology": {
        "Software Developer": {
            "Key Responsibilities": [
                "Design, develop, and maintain software applications.",
                "Collaborate with cross-functional teams to understand user needs.",
                "Write clean and efficient code using programming languages like Python, Java, or C++.",
                "Test and debug software to ensure functionality and performance."
            ],
            "Average Salary (Globally)": "$70,000 - $120,000 annually.",
            "Education Requirements": "Bachelor's degree in Computer Science or related field.",
            "Advice": "Build a strong portfolio of projects. Stay updated on industry trends and technologies."
        },
        "Data Scientist": {
            "Key Responsibilities": [
                "Analyze and interpret complex data to derive insights.",
                "Develop machine learning models and algorithms.",
                "Collaborate with stakeholders to solve business problems.",
                "Present findings through data visualization tools."
            ],
            "Average Salary (Globally)": "$100,000 - $150,000 annually.",
            "Education Requirements": "Bachelor's or Master's degree in Data Science, Statistics, or related field.",
            "Advice": "Master programming languages like Python and R. Gain expertise in data visualization and machine learning."
        },
        "Cybersecurity Analyst": {
            "Key Responsibilities": [
                "Monitor networks for security breaches.",
                "Conduct vulnerability assessments and penetration tests.",
                "Implement and enforce security policies.",
                "Respond to and mitigate security incidents."
            ],
            "Average Salary (Globally)": "$80,000 - $120,000 annually.",
            "Education Requirements": "Bachelor's degree in Cybersecurity or related field.",
            "Advice": "Stay current with security trends and technologies. Get certifications like CEH or CISSP."
        },
        "AI Engineer": {
            "Key Responsibilities": [
                "Develop and implement AI algorithms and models.",
                "Train AI systems on large datasets.",
                "Collaborate with teams to integrate AI into products.",
                "Test and improve AI models for better performance."
            ],
            "Average Salary (Globally)": "$100,000 - $150,000 annually.",
            "Education Requirements": "Bachelor's or Master's degree in Computer Science, Artificial Intelligence, or related field.",
            "Advice": "Understand machine learning frameworks and keep learning new AI techniques."
        },
        "Web Developer": {
            "Key Responsibilities": [
                "Design and develop websites and web applications.",
                "Ensure websites are responsive and user-friendly.",
                "Collaborate with clients to understand their needs.",
                "Optimize websites for speed and search engine rankings."
            ],
            "Average Salary (Globally)": "$60,000 - $100,000 annually.",
            "Education Requirements": "Bachelor's degree in Computer Science or related field.",
            "Advice": "Develop a strong portfolio of web development projects."
        },
        "Cloud Engineer": {
            "Key Responsibilities": [
                "Design and manage cloud computing infrastructure.",
                "Ensure cloud services are secure and scalable.",
                "Troubleshoot and resolve cloud service issues.",
                "Collaborate with teams to implement cloud-based solutions."
            ],
            "Average Salary (Globally)": "$90,000 - $130,000 annually.",
            "Education Requirements": "Bachelor's degree in Computer Science or related field.",
            "Advice": "Familiarize yourself with cloud platforms like AWS, Azure, or Google Cloud."
        },
        "Network Engineer": {
            "Key Responsibilities": [
                "Design and maintain network systems.",
                "Troubleshoot network issues and optimize performance.",
                "Ensure network security and data protection.",
                "Work with hardware and software solutions to improve network infrastructure."
            ],
            "Average Salary (Globally)": "$70,000 - $100,000 annually.",
            "Education Requirements": "Bachelor's degree in Network Engineering or related field.",
            "Advice": "Gain certifications like Cisco CCNA and understand network protocols."
        },
        "Blockchain Developer": {
            "Key Responsibilities": [
                "Develop and maintain blockchain-based applications.",
                "Work with cryptocurrencies and decentralized systems.",
                "Implement smart contracts and blockchain protocols.",
                "Test and debug blockchain solutions."
            ],
            "Average Salary (Globally)": "$100,000 - $150,000 annually.",
            "Education Requirements": "Bachelor's degree in Computer Science or related field.",
            "Advice": "Learn about blockchain platforms like Ethereum and Hyperledger."
        },
        "DevOps Engineer": {
            "Key Responsibilities": [
                "Collaborate with development and IT operations teams.",
                "Automate processes and integrate continuous delivery pipelines.",
                "Monitor system performance and ensure reliability.",
                "Troubleshoot issues in production environments."
            ],
            "Average Salary (Globally)": "$90,000 - $130,000 annually.",
            "Education Requirements": "Bachelor's degree in Computer Science or related field.",
            "Advice": "Familiarize yourself with tools like Docker, Kubernetes, and Jenkins."
        },
        "Game Developer": {
            "Key Responsibilities": [
                "Design and develop video games.",
                "Collaborate with designers and artists to create immersive experiences.",
                "Write game code and debug issues.",
                "Test games to ensure they are bug-free."
            ],
            "Average Salary (Globally)": "$60,000 - $120,000 annually.",
            "Education Requirements": "Bachelor's degree in Game Development or related field.",
            "Advice": "Build a strong portfolio with game development projects."
        },
        "UX/UI Designer": {
            "Key Responsibilities": [
                "Design user-friendly interfaces for digital products.",
                "Create wireframes, prototypes, and user flows.",
                "Conduct user research and testing.",
                "Collaborate with developers to ensure design implementation."
            ],
            "Average Salary (Globally)": "$70,000 - $110,000 annually.",
            "Education Requirements": "Bachelor's degree in Design or related field.",
            "Advice": "Stay updated on design trends and improve your portfolio."
        },
        "IT Support Specialist": {
            "Key Responsibilities": [
                "Provide technical support to users.",
                "Troubleshoot hardware and software issues.",
                "Install and configure software and systems.",
                "Maintain IT infrastructure and networks."
            ],
            "Average Salary (Globally)": "$50,000 - $70,000 annually.",
            "Education Requirements": "Associate's or Bachelor's degree in Information Technology.",
            "Advice": "Develop strong problem-solving skills and be patient with users."
      },
        "AI Research Scientist": {
            "Key Responsibilities": [
                "Conduct research to advance the field of artificial intelligence.",
                "Develop and test new AI algorithms and models.",
                "Publish findings in academic journals.",
                "Collaborate with teams to apply research to real-world problems."
            ],
            "Average Salary (Globally)": "$110,000 - $160,000 annually.",
            "Education Requirements": "Ph.D. in Artificial Intelligence, Computer Science, or related field.",
            "Advice": "Stay on top of the latest AI trends and research. Contribute to AI conferences."
        },
        "Augmented Reality Developer": {
            "Key Responsibilities": [
                "Design and develop AR applications for mobile and wearable devices.",
                "Create immersive experiences combining the real world with virtual elements.",
                "Work with 3D models and sensors to create realistic environments.",
                "Test and optimize AR apps for various platforms."
            ],
            "Average Salary (Globally)": "$80,000 - $130,000 annually.",
            "Education Requirements": "Bachelor's degree in Computer Science, Game Development, or related field.",
            "Advice": "Learn AR frameworks like ARKit or ARCore and build a strong portfolio."
        },
        "Big Data Engineer": {
            "Key Responsibilities": [
                "Design and maintain systems that store and process large amounts of data.",
                "Develop data pipelines and ensure data quality.",
                "Work with tools like Hadoop, Spark, and Kafka.",
                "Collaborate with data scientists to provide data for analysis."
            ],
            "Average Salary (Globally)": "$90,000 - $140,000 annually.",
            "Education Requirements": "Bachelor's or Master's degree in Computer Science, Data Engineering, or related field.",
            "Advice": "Familiarize yourself with distributed systems and data processing frameworks."
        },
        "Embedded Systems Engineer": {
            "Key Responsibilities": [
                "Design and develop embedded systems for hardware devices.",
                "Write low-level software to interface with hardware components.",
                "Work on real-time operating systems and microcontrollers.",
                "Test and debug embedded systems."
            ],
            "Average Salary (Globally)": "$80,000 - $120,000 annually.",
            "Education Requirements": "Bachelor's degree in Electrical Engineering, Computer Engineering, or related field.",
            "Advice": "Gain experience with microcontrollers, embedded software, and hardware design."
        },
        "Ethical Hacker": {
            "Key Responsibilities": [
                "Test and assess the security of computer systems and networks.",
                "Identify vulnerabilities and exploit weaknesses.",
                "Recommend security measures to improve system protection.",
                "Write detailed reports on findings and solutions."
            ],
            "Average Salary (Globally)": "$80,000 - $130,000 annually.",
            "Education Requirements": "Bachelor's degree in Cybersecurity or related field.",
            "Advice": "Get certifications like CEH and always follow ethical guidelines."
        },
        "Full Stack Developer": {
            "Key Responsibilities": [
                "Design and develop both front-end and back-end components of web applications.",
                "Work with databases, servers, and APIs.",
                "Ensure the application is responsive and user-friendly.",
                "Collaborate with designers and other developers."
            ],
            "Average Salary (Globally)": "$80,000 - $120,000 annually.",
            "Education Requirements": "Bachelor's degree in Computer Science or related field.",
            "Advice": "Master both front-end and back-end technologies, such as JavaScript, Node.js, and databases."
        },
        "Mobile App Developer": {
            "Key Responsibilities": [
                "Design and develop mobile applications for iOS and Android.",
                "Ensure app performance and usability.",
                "Work with APIs and databases for app functionality.",
                "Collaborate with cross-functional teams for app development."
            ],
            "Average Salary (Globally)": "$70,000 - $110,000 annually.",
            "Education Requirements": "Bachelor's degree in Computer Science or related field.",
            "Advice": "Learn Swift for iOS and Kotlin/Java for Android. Build a portfolio of apps."
        },
        "Product Manager (Tech)": {
            "Key Responsibilities": [
                "Oversee the development and lifecycle of tech products.",
                "Collaborate with engineering, design, and marketing teams.",
                "Conduct market research to define product vision and features.",
                "Manage product roadmap and timelines."
            ],
            "Average Salary (Globally)": "$100,000 - $150,000 annually.",
            "Education Requirements": "Bachelor's degree in Business, Engineering, or related field.",
            "Advice": "Develop strong communication and leadership skills. Understand both technical and business aspects."
        },
        "Robotics Engineer": {
            "Key Responsibilities": [
                "Design and build robotic systems and devices.",
                "Work on automation and control systems for robotics.",
                "Collaborate with engineers to integrate sensors and actuators.",
                "Test and optimize robotic systems."
            ],
            "Average Salary (Globally)": "$90,000 - $130,000 annually.",
            "Education Requirements": "Bachelor's degree in Robotics, Mechanical Engineering, or related field.",
            "Advice": "Get hands-on experience with robotics platforms like ROS and learn programming for robots."
        },
        "Security Architect": {
            "Key Responsibilities": [
                "Design and implement secure IT infrastructures.",
                "Evaluate and address security risks within systems.",
                "Develop security policies and procedures.",
                "Collaborate with other teams to ensure system security."
            ],
            "Average Salary (Globally)": "$110,000 - $160,000 annually.",
            "Education Requirements": "Bachelor's degree in Cybersecurity, Information Security, or related field.",
            "Advice": "Gain expertise in security frameworks and certifications like CISSP and CISM."
        },
        "Site Reliability Engineer (SRE)": {
            "Key Responsibilities": [
                "Maintain and improve the reliability of systems and services.",
                "Monitor system performance and address issues.",
                "Automate processes and improve infrastructure.",
                "Work closely with development teams to ensure high availability."
            ],
            "Average Salary (Globally)": "$100,000 - $140,000 annually.",
            "Education Requirements": "Bachelor's degree in Computer Science or related field.",
            "Advice": "Learn about cloud platforms, monitoring tools, and automation frameworks."
        },
        "Software Tester (QA)": {
            "Key Responsibilities": [
                "Test software applications for bugs and defects.",
                "Develop test plans and cases to ensure product quality.",
                "Automate tests for efficient testing processes.",
                "Collaborate with developers to fix issues."
            ],
            "Average Salary (Globally)": "$60,000 - $100,000 annually.",
            "Education Requirements": "Bachelor's degree in Computer Science or related field.",
            "Advice": "Learn about testing tools like Selenium and focus on both manual and automated testing."
        },
        "Technical Writer": {
            "Key Responsibilities": [
                "Write and edit technical documentation and user manuals.",
                "Create clear and concise instructions for complex systems.",
                "Collaborate with engineers and product managers to understand technical concepts.",
                "Update documentation to reflect changes in products."
            ],
            "Average Salary (Globally)": "$60,000 - $90,000 annually.",
            "Education Requirements": "Bachelor's degree in English, Communications, or related field.",
            "Advice": "Develop a strong understanding of technical concepts and learn how to communicate them clearly."
        },
        "Test Automation Engineer": {
            "Key Responsibilities": [
                "Design and implement automated testing solutions.",
                "Develop scripts to test software functionality.",
                "Work with development teams to ensure code quality.",
                "Maintain and update automated tests as products evolve."
            ],
            "Average Salary (Globally)": "$80,000 - $120,000 annually.",
            "Education Requirements": "Bachelor's degree in Computer Science or related field.",
            "Advice": "Familiarize yourself with test automation tools like Selenium, Appium, and JUnit."
        },
        "Technology Consultant": {
            "Key Responsibilities": [
                "Provide strategic advice on technology solutions.",
                "Analyze business needs and recommend software solutions.",
                "Collaborate with stakeholders to implement technology projects.",
                "Stay updated on industry trends and emerging technologies."
            ],
            "Average Salary (Globally)": "$90,000 - $140,000 annually.",
            "Education Requirements": "Bachelor's degree in Computer Science, Business, or related field.",
            "Advice": "Develop strong problem-solving and communication skills. Understand both technical and business aspects."
        },
        "UI Developer": {
            "Key Responsibilities": [
                "Develop and maintain user interfaces for web applications.",
                "Ensure UI design is responsive and accessible.",
                "Collaborate with designers to implement UI/UX requirements.",
                "Optimize UI for performance and user experience."
            ],
            "Average Salary (Globally)": "$70,000 - $100,000 annually.",
            "Education Requirements": "Bachelor's degree in Computer Science or related field.",
            "Advice": "Master HTML, CSS, JavaScript, and modern UI frameworks like React or Angular."
        },
        "Video Game Tester": {
            "Key Responsibilities": [
                "Test video games for bugs, glitches, and issues.",
                "Provide feedback on game mechanics and user experience.",
                "Work closely with developers to identify and fix problems.",
                "Test various platforms and configurations."
            ],
            "Average Salary (Globally)": "$40,000 - $70,000 annually.",
            "Education Requirements": "High school diploma or equivalent. Game-related experience preferred.",
            "Advice": "Play a wide range of games and pay attention to details while testing."
        },
        "Virtual Assistant (Tech)": {
            "Key Responsibilities": [
                "Provide administrative support to tech teams and executives.",
                "Manage schedules, emails, and documents.",
                "Handle data entry and basic technical tasks.",
                "Assist with project management and communications."
            ],
            "Average Salary (Globally)": "$40,000 - $70,000 annually.",
            "Education Requirements": "High school diploma or Bachelor's degree in related field.",
            "Advice": "Develop strong organizational and communication skills, and be proficient with tech tools."
       
     },
},

"Education": {
    "Teacher": {
        "Key Responsibilities": [
            "Plan and deliver lessons to students.",
            "Assess students' progress and provide feedback.",
            "Create a positive and inclusive learning environment.",
            "Collaborate with colleagues and parents to support student development."
        ],
        "Average Salary (Globally)": "$40,000 - $60,000 annually.",
        "Education Requirements": "Bachelor's degree in Education or related field.",
        "Advice": "Develop strong classroom management skills and engage students with creative lessons."
    },
    "Special Education Teacher": {
        "Key Responsibilities": [
            "Work with students who have disabilities or special needs.",
            "Create individualized education plans (IEPs).",
            "Collaborate with parents, therapists, and other professionals.",
            "Adapt teaching methods to meet students' needs."
        ],
        "Average Salary (Globally)": "$45,000 - $70,000 annually.",
        "Education Requirements": "Bachelor's degree in Special Education.",
        "Advice": "Be patient, empathetic, and flexible to cater to students' unique needs."
    },
    "School Counselor": {
        "Key Responsibilities": [
            "Provide academic, emotional, and career guidance to students.",
            "Assist with personal and social issues.",
            "Work with teachers and parents to support student development.",
            "Conduct workshops on topics like stress management and study skills."
        ],
        "Average Salary (Globally)": "$50,000 - $75,000 annually.",
        "Education Requirements": "Master's degree in School Counseling or related field.",
        "Advice": "Develop strong communication and active listening skills."
    },
    "Principal": {
        "Key Responsibilities": [
            "Oversee the daily operations of the school.",
            "Manage school staff and budgets.",
            "Ensure the school's policies are followed.",
            "Communicate with parents, students, and the community."
        ],
        "Average Salary (Globally)": "$90,000 - $150,000 annually.",
        "Education Requirements": "Master's degree in Education Leadership or related field.",
        "Advice": "Strong leadership, organizational, and problem-solving skills are crucial."
    },
    "Instructional Coordinator": {
        "Key Responsibilities": [
            "Develop and implement educational programs and curriculum.",
            "Assess teaching effectiveness and suggest improvements.",
            "Train teachers on new teaching methods and technology.",
            "Monitor educational standards and policies."
        ],
        "Average Salary (Globally)": "$60,000 - $90,000 annually.",
        "Education Requirements": "Master's degree in Curriculum and Instruction.",
        "Advice": "Stay current with educational trends and innovations."
    },
    "Librarian": {
        "Key Responsibilities": [
            "Manage library resources and collections.",
            "Assist students and staff in finding research materials.",
            "Promote literacy and organize educational programs.",
            "Maintain the library’s digital systems."
        ],
        "Average Salary (Globally)": "$50,000 - $70,000 annually.",
        "Education Requirements": "Master's degree in Library Science.",
        "Advice": "Develop organizational skills and a passion for helping others."
    },
    "Education Administrator": {
        "Key Responsibilities": [
            "Oversee the administrative operations of schools or educational institutions.",
            "Ensure compliance with educational laws and policies.",
            "Manage budgets, staffing, and resource allocation.",
            "Develop strategies for improving educational outcomes."
        ],
        "Average Salary (Globally)": "$70,000 - $120,000 annually.",
        "Education Requirements": "Master's degree in Education Administration or related field.",
        "Advice": "Strong leadership, financial, and organizational skills are key."
    },
    "ESL Teacher": {
        "Key Responsibilities": [
            "Teach English as a second language to non-native speakers.",
            "Develop and implement language learning programs.",
            "Assess student progress and adapt lessons.",
            "Provide support in both academic and social language development."
        ],
        "Average Salary (Globally)": "$40,000 - $60,000 annually.",
        "Education Requirements": "Bachelor's degree in English, Education, or TESOL certification.",
        "Advice": "Cultural sensitivity and adaptability are essential."
    },
    "Tutoring Services Manager": {
        "Key Responsibilities": [
            "Oversee operations of tutoring centers.",
            "Hire and train tutors.",
            "Manage schedules, resources, and client relations.",
            "Ensure high-quality educational services are provided."
        ],
        "Average Salary (Globally)": "$50,000 - $75,000 annually.",
        "Education Requirements": "Bachelor's degree in Education or Business Management.",
        "Advice": "Strong organizational and leadership skills are important."
    },
    "Higher Education Instructor": {
        "Key Responsibilities": [
            "Teach college or university-level courses.",
            "Conduct research and publish academic papers.",
            "Guide students through projects and research work.",
            "Participate in academic committees and meetings."
        ],
        "Average Salary (Globally)": "$60,000 - $120,000 annually.",
        "Education Requirements": "Master's or Doctoral degree in the subject area.",
        "Advice": "Stay passionate about your subject and keep up with academic research."
    },
    "Education Consultant": {
        "Key Responsibilities": [
            "Advise educational institutions on curriculum design and teaching strategies.",
            "Conduct workshops and training for educators.",
            "Provide recommendations on school improvement initiatives.",
            "Assist with educational policy development."
        ],
        "Average Salary (Globally)": "$70,000 - $120,000 annually.",
        "Education Requirements": "Master's degree in Education or related field.",
        "Advice": "Develop a deep understanding of educational systems and best practices."
    },
    "Speech-Language Pathologist": {
        "Key Responsibilities": [
            "Assess and treat speech, language, and communication disorders.",
            "Develop individualized treatment plans for students.",
            "Collaborate with teachers and parents to support student development.",
            "Provide therapy to improve speech and language skills."
        ],
        "Average Salary (Globally)": "$60,000 - $90,000 annually.",
        "Education Requirements": "Master's degree in Speech-Language Pathology.",
        "Advice": "Patience and strong communication skills are essential."
    },
    "School Psychologist": {
        "Key Responsibilities": [
            "Assess and diagnose students' emotional, behavioral, and learning issues.",
            "Provide counseling and interventions for students.",
            "Collaborate with teachers, parents, and administrators.",
            "Develop programs to improve student well-being."
        ],
        "Average Salary (Globally)": "$60,000 - $90,000 annually.",
        "Education Requirements": "Master's or Doctoral degree in Psychology.",
        "Advice": "Develop empathy, active listening, and problem-solving skills."
    },
    "School Social Worker": {
        "Key Responsibilities": [
            "Provide support to students and families facing social, emotional, or economic challenges.",
            "Develop programs to address bullying, substance abuse, and mental health issues.",
            "Collaborate with educators, parents, and other professionals.",
            "Assist in crisis management and intervention."
        ],
        "Average Salary (Globally)": "$50,000 - $75,000 annually.",
        "Education Requirements": "Master's degree in Social Work.",
        "Advice": "Empathy, communication, and problem-solving skills are essential."
    },
    "College Admissions Counselor": {
        "Key Responsibilities": [
            "Guide prospective students through the college application process.",
            "Assist with essay writing, interview preparation, and scholarship applications.",
            "Conduct campus tours and information sessions.",
            "Evaluate applications and provide admissions decisions."
        ],
        "Average Salary (Globally)": "$50,000 - $70,000 annually.",
        "Education Requirements": "Bachelor's degree in Education, Counseling, or related field.",
        "Advice": "Be knowledgeable about the application process and scholarships."
    },
    "Academic Advisor": {
        "Key Responsibilities": [
            "Advise students on course selection and academic planning.",
            "Help students with career exploration and academic challenges.",
            "Monitor academic progress and intervene when necessary.",
            "Provide information on internships, study abroad, and career services."
        ],
        "Average Salary (Globally)": "$45,000 - $70,000 annually.",
        "Education Requirements": "Bachelor's or Master's degree in Education or Counseling.",
        "Advice": "Develop strong interpersonal and problem-solving skills."
    },
    "Adult Education Instructor": {
        "Key Responsibilities": [
            "Teach adults in continuing education programs.",
            "Develop curriculum and instructional materials.",
            "Assess students' learning progress and provide feedback.",
            "Provide support to adult learners with varying levels of education."
        ],
        "Average Salary (Globally)": "$45,000 - $65,000 annually.",
        "Education Requirements": "Bachelor's degree in Education or related field.",
        "Advice": "Be adaptable to diverse learning styles and life experiences."
    },
    "Instructional Designer": {
        "Key Responsibilities": [
            "Design and develop instructional materials and courses.",
            "Collaborate with subject matter experts to create effective learning experiences.",
            "Evaluate and improve existing educational programs.",
            "Use technology to enhance learning delivery."
        ],
        "Average Salary (Globally)": "$60,000 - $85,000 annually.",
        "Education Requirements": "Bachelor's degree in Instructional Design or related field.",
        "Advice": "Stay current with instructional design trends and tools."
    },
    "Education Policy Analyst": {
        "Key Responsibilities": [
            "Analyze and research educational policies and trends.",
            "Advise policymakers on the impact of educational policies.",
            "Write reports and make recommendations for policy improvements.",
            "Collaborate with government agencies and educational institutions."
        ],
        "Average Salary (Globally)": "$70,000 - $100,000 annually.",
        "Education Requirements": "Master's degree in Public Policy, Education, or related field.",
        "Advice": "Strong research and analytical skills are essential."
    },
    "Education Technology Specialist": {
        "Key Responsibilities": [
            "Implement and manage educational technology tools.",
            "Train educators on how to use technology in the classroom.",
            "Evaluate and recommend new educational technologies.",
            "Ensure technology aligns with curriculum goals."
        ],
        "Average Salary (Globally)": "$55,000 - $80,000 annually.",
        "Education Requirements": "Bachelor's degree in Education Technology or related field.",
        "Advice": "Stay updated on emerging educational technologies."
    },
    "Vocational Instructor": {
        "Key Responsibilities": [
            "Teach specialized skills and trades to students.",
            "Develop practical and hands-on training programs.",
            "Assess students' progress and provide feedback.",
            "Collaborate with industry professionals to ensure curriculum relevance."
        ],
        "Average Salary (Globally)": "$45,000 - $70,000 annually.",
        "Education Requirements": "Bachelor's degree in Education or relevant trade certification.",
        "Advice": "Focus on real-world applications and practical skills."
    },
    "Educational Content Creator": {
        "Key Responsibilities": [
            "Develop educational content for online platforms.",
            "Create engaging videos, articles, and other learning materials.",
            "Collaborate with educators and experts to produce high-quality content.",
            "Promote educational content to reach a wide audience."
        ],
        "Average Salary (Globally)": "$40,000 - $70,000 annually.",
        "Education Requirements": "Bachelor's degree in Education, Journalism, or related field.",
        "Advice": "Be creative and tech-savvy to create engaging learning experiences."
    },
    "Online Tutor": {
        "Key Responsibilities": [
            "Provide one-on-one tutoring to students via online platforms.",
            "Create customized learning plans for students.",
            "Track student progress and adjust teaching methods.",
            "Assist students with homework and exam preparation."
        ],
        "Average Salary (Globally)": "$20 - $60 per hour.",
        "Education Requirements": "Bachelor's degree in the subject area.",
        "Advice": "Patience, flexibility, and clear communication are key."
    


 
    },
},

    

    "Engineering": {
        "Civil Engineer": {
            "Key Responsibilities": [
                "Design and oversee the construction of infrastructure projects.",
                "Ensure that projects meet safety, environmental, and legal standards.",
                "Coordinate with contractors and project managers.",
                "Conduct site inspections and monitor project progress."
            ],
            "Average Salary (Globally)": "$60,000 - $90,000 annually.",
            "Education Requirements": "Bachelor's degree in Civil Engineering.",
            "Advice": "Strong knowledge of materials, structural design, and safety standards is crucial."
        },
        "Mechanical Engineer": {
            "Key Responsibilities": [
                "Design, develop, and test mechanical systems and devices.",
                "Analyze mechanical systems for performance and safety.",
                "Collaborate with manufacturers to improve product design.",
                "Use computer-aided design (CAD) software to create models."
            ],
            "Average Salary (Globally)": "$60,000 - $85,000 annually.",
            "Education Requirements": "Bachelor's degree in Mechanical Engineering.",
            "Advice": "Focus on problem-solving and analytical skills for complex systems."
        },
        "Electrical Engineer": {
            "Key Responsibilities": [
                "Design, develop, and maintain electrical systems and components.",
                "Test electrical systems for efficiency and safety.",
                "Work on power generation, transmission, and distribution systems.",
                "Collaborate with other engineers on multi-disciplinary projects."
            ],
            "Average Salary (Globally)": "$65,000 - $90,000 annually.",
            "Education Requirements": "Bachelor's degree in Electrical Engineering.",
            "Advice": "Stay updated on emerging technologies in renewable energy and automation."
        },
        "Software Engineer": {
            "Key Responsibilities": [
                "Develop and maintain software applications and systems.",
                "Test software for functionality and performance.",
                "Collaborate with other engineers and stakeholders to define software requirements.",
                "Use programming languages such as Python, Java, or C++."
            ],
            "Average Salary (Globally)": "$70,000 - $110,000 annually.",
            "Education Requirements": "Bachelor's degree in Software Engineering or Computer Science.",
            "Advice": "Develop a strong foundation in coding and problem-solving."
        },
        "Aerospace Engineer": {
            "Key Responsibilities": [
                "Design and test aircraft, spacecraft, and related systems.",
                "Ensure systems meet regulatory and safety standards.",
                "Analyze flight data and optimize performance.",
                "Collaborate with government agencies or private sector companies."
            ],
            "Average Salary (Globally)": "$80,000 - $120,000 annually.",
            "Education Requirements": "Bachelor's degree in Aerospace Engineering.",
            "Advice": "Focus on understanding aerodynamics and propulsion systems."
        },
        "Chemical Engineer": {
            "Key Responsibilities": [
                "Design and operate chemical processes for large-scale manufacturing.",
                "Ensure the safe and efficient use of chemicals in industrial settings.",
                "Monitor and control chemical reactions in various processes.",
                "Develop methods to improve production efficiency and minimize waste."
            ],
            "Average Salary (Globally)": "$70,000 - $95,000 annually.",
            "Education Requirements": "Bachelor's degree in Chemical Engineering.",
            "Advice": "Master process design and chemical reaction optimization."
        },
        "Industrial Engineer": {
            "Key Responsibilities": [
                "Optimize production processes and workflows.",
                "Design systems that integrate people, materials, and technology.",
                "Analyze and improve manufacturing efficiency.",
                "Work on quality control, inventory management, and cost reduction."
            ],
            "Average Salary (Globally)": "$65,000 - $85,000 annually.",
            "Education Requirements": "Bachelor's degree in Industrial Engineering.",
            "Advice": "Develop strong skills in data analysis and process optimization."
        },
        "Environmental Engineer": {
            "Key Responsibilities": [
                "Design systems to protect the environment, such as water treatment plants.",
                "Work on pollution control, waste management, and sustainable practices.",
                "Ensure compliance with environmental regulations.",
                "Develop strategies to mitigate environmental impact in industrial settings."
            ],
            "Average Salary (Globally)": "$60,000 - $90,000 annually.",
            "Education Requirements": "Bachelor's degree in Environmental Engineering.",
            "Advice": "Stay updated on environmental laws and sustainability practices."
        },
        "Structural Engineer": {
            "Key Responsibilities": [
                "Design and analyze structural components for buildings, bridges, and other infrastructure.",
                "Ensure structures are safe, stable, and cost-effective.",
                "Work closely with architects and contractors.",
                "Perform site inspections and assess structural integrity."
            ],
            "Average Salary (Globally)": "$65,000 - $95,000 annually.",
            "Education Requirements": "Bachelor's degree in Structural Engineering.",
            "Advice": "Strong knowledge of materials and load-bearing calculations is essential."
        },
        "Biomedical Engineer": {
            "Key Responsibilities": [
                "Design and develop medical devices and equipment.",
                "Work with healthcare professionals to improve patient care.",
                "Ensure devices meet safety and regulatory standards.",
                "Research new technologies to advance healthcare solutions."
            ],
            "Average Salary (Globally)": "$70,000 - $95,000 annually.",
            "Education Requirements": "Bachelor's degree in Biomedical Engineering.",
            "Advice": "Focus on medical technology innovations and patient safety."
        },
        "Marine Engineer": {
            "Key Responsibilities": [
                "Design, build, and maintain ships and marine equipment.",
                "Oversee the installation of propulsion systems, power generation, and HVAC systems.",
                "Ensure compliance with maritime safety and environmental standards.",
                "Troubleshoot mechanical and electrical systems aboard vessels."
            ],
            "Average Salary (Globally)": "$70,000 - $100,000 annually.",
            "Education Requirements": "Bachelor's degree in Marine Engineering.",
            "Advice": "Master fluid dynamics and systems engineering specific to maritime applications."
        },
        "Mining Engineer": {
            "Key Responsibilities": [
                "Design and implement mining operations and systems.",
                "Evaluate and manage the extraction of minerals and resources.",
                "Ensure the safety and environmental impact of mining projects.",
                "Develop efficient mining processes and equipment."
            ],
            "Average Salary (Globally)": "$75,000 - $110,000 annually.",
            "Education Requirements": "Bachelor's degree in Mining Engineering.",
            "Advice": "Focus on geotechnical engineering and environmental impact assessments."
        },
        "Nuclear Engineer": {
            "Key Responsibilities": [
                "Design and operate nuclear power plants and reactors.",
                "Ensure safety and efficiency in nuclear energy production.",
                "Monitor radiation levels and manage waste disposal.",
                "Develop new technologies for nuclear energy applications."
            ],
            "Average Salary (Globally)": "$85,000 - $130,000 annually.",
            "Education Requirements": "Bachelor's degree in Nuclear Engineering.",
            "Advice": "Develop a strong understanding of nuclear physics and safety protocols."
        },
        "Robotics Engineer": {
            "Key Responsibilities": [
                "Design and develop robotic systems for various industries.",
                "Program and test robotic devices for functionality and efficiency.",
                "Work with manufacturers to implement robotics into production systems.",
                "Research new robotic technologies and applications."
            ],
            "Average Salary (Globally)": "$75,000 - $110,000 annually.",
            "Education Requirements": "Bachelor's degree in Robotics Engineering.",
            "Advice": "Master automation systems and AI programming."
        },
        "Petroleum Engineer": {
            "Key Responsibilities": [
                "Design and develop methods for extracting oil and gas from the earth.",
                "Oversee drilling and production operations.",
                "Ensure safety and efficiency in oil extraction.",
                "Develop technologies to enhance resource recovery and reduce environmental impact."
            ],
            "Average Salary (Globally)": "$85,000 - $120,000 annually.",
            "Education Requirements": "Bachelor's degree in Petroleum Engineering.",
            "Advice": "Develop expertise in reservoir engineering and drilling techniques."
        },
        "Construction Engineer": {
            "Key Responsibilities": [
                "Manage construction projects from start to finish.",
                "Coordinate contractors, architects, and other professionals.",
                "Ensure that construction projects meet legal, safety, and quality standards.",
                "Prepare cost estimates and budgets for projects."
            ],
            "Average Salary (Globally)": "$65,000 - $90,000 annually.",
            "Education Requirements": "Bachelor's degree in Construction Engineering.",
            "Advice": "Develop strong project management and budgeting skills."
        },
        "Geotechnical Engineer": {
            "Key Responsibilities": [
                "Analyze soil, rock, and other materials for construction projects.",
                "Design foundations and earthworks for structures.",
                "Conduct site investigations and geotechnical surveys.",
                "Assess risks related to landslides, earthquakes, and other natural hazards."
            ],
            "Average Salary (Globally)": "$70,000 - $100,000 annually.",
            "Education Requirements": "Bachelor's degree in Geotechnical Engineering.",
            "Advice": "Master the principles of soil mechanics and structural integrity."
        },
        "Automotive Engineer": {
            "Key Responsibilities": [
                "Design and develop vehicles and vehicle systems.",
                "Test vehicle performance and safety.",
                "Collaborate with manufacturers to optimize design and production processes.",
                "Work on improving fuel efficiency, emissions, and overall vehicle performance."
            ],
            "Average Salary (Globally)": "$70,000 - $95,000 annually.",
            "Education Requirements": "Bachelor's degree in Automotive Engineering.",
            "Advice": "Stay current with the latest advancements in vehicle technology."
        },
        "Architectural Engineer": {
            "Key Responsibilities": [
                "Design and manage the construction of buildings and structures.",
                "Integrate architectural and engineering principles into building designs.",
                "Ensure compliance with building codes and safety regulations.",
                "Oversee construction teams and contractors."
            ],
            "Average Salary (Globally)": "$65,000 - $95,000 annually.",
            "Education Requirements": "Bachelor's degree in Architectural Engineering.",
            "Advice": "Focus on understanding the interplay between architecture and engineering."
        },
        "Systems Engineer": {
            "Key Responsibilities": [
                "Design and integrate complex systems for various industries.",
                "Ensure that systems meet performance, safety, and cost-efficiency standards.",
                "Collaborate with other engineers to develop functional systems.",
                "Monitor system performance and implement improvements."
            ],
            "Average Salary (Globally)": "$70,000 - $100,000 annually.",
            "Education Requirements": "Bachelor's degree in Systems Engineering.",
            "Advice": "Develop a strong foundation in systems thinking and project management."
        },
        "Control Systems Engineer": {
            "Key Responsibilities": [
                "Design and implement control systems for automation.",
                "Ensure systems operate efficiently and safely.",
                "Troubleshoot and optimize control systems.",
                "Collaborate with other engineers on system integration."
            ],
            "Average Salary (Globally)": "$75,000 - $100,000 annually.",
            "Education Requirements": "Bachelor's degree in Control Systems Engineering.",
            "Advice": "Focus on mastering automation systems and control algorithms."
        },
        "Quality Assurance Engineer": {
            "Key Responsibilities": [
                "Ensure the quality of products and systems through testing and inspections.",
                "Develop testing procedures and standards.",
                "Identify defects and work with teams to resolve issues.",
                "Monitor production processes to maintain quality standards."
            ],
            "Average Salary (Globally)": "$60,000 - $85,000 annually.",
            "Education Requirements": "Bachelor's degree in Quality Assurance Engineering.",
            "Advice": "Develop a keen eye for detail and an understanding of testing methodologies."
        },
        "Fire Protection Engineer": {
            "Key Responsibilities": [
                "Design and implement fire protection systems for buildings and facilities.",
                "Conduct fire risk assessments and develop safety plans.",
                "Ensure compliance with fire safety regulations and standards.",
                "Work with architects and contractors to integrate fire protection systems."
            ],
            "Average Salary (Globally)": "$65,000 - $95,000 annually.",
            "Education Requirements": "Bachelor's degree in Fire Protection Engineering.",
            "Advice": "Master fire safety codes and systems design."
        },
    },



    "Business": {
        "Business Analyst": {
            "Key Responsibilities": [
                "Analyze business processes and recommend improvements.",
                "Gather and interpret data to inform business decisions.",
                "Collaborate with stakeholders to define project goals and requirements.",
                "Create detailed reports and presentations for senior management."
            ],
            "Average Salary (Globally)": "$60,000 - $85,000 annually.",
            "Education Requirements": "Bachelor's degree in Business, Economics, or related field.",
            "Advice": "Strong analytical skills and proficiency in data analysis tools are essential."
        },
        "Marketing Manager": {
            "Key Responsibilities": [
                "Develop and implement marketing strategies to increase brand awareness.",
                "Oversee marketing campaigns and monitor their effectiveness.",
                "Analyze market trends and customer preferences.",
                "Collaborate with product teams to align marketing efforts with product goals."
            ],
            "Average Salary (Globally)": "$70,000 - $110,000 annually.",
            "Education Requirements": "Bachelor's degree in Marketing, Business Administration, or related field.",
            "Advice": "Creativity, communication, and a strong understanding of digital marketing are key."
        },
        "Financial Analyst": {
            "Key Responsibilities": [
                "Analyze financial data and provide insights for business decisions.",
                "Prepare financial models and forecasts.",
                "Evaluate the financial performance of projects and investments.",
                "Advise management on financial planning and budgeting."
            ],
            "Average Salary (Globally)": "$60,000 - $90,000 annually.",
            "Education Requirements": "Bachelor's degree in Finance, Accounting, or related field.",
            "Advice": "Strong analytical skills and attention to detail are critical."
        },
        "Human Resources Manager": {
            "Key Responsibilities": [
                "Manage recruitment, hiring, and employee relations.",
                "Develop and implement HR policies and procedures.",
                "Ensure compliance with labor laws and company regulations.",
                "Oversee employee benefits and performance management systems."
            ],
            "Average Salary (Globally)": "$70,000 - $100,000 annually.",
            "Education Requirements": "Bachelor's degree in Human Resources, Business Administration, or related field.",
            "Advice": "Empathy, strong communication, and conflict resolution skills are important."
        },
        "Operations Manager": {
            "Key Responsibilities": [
                "Oversee daily operations to ensure business efficiency.",
                "Develop and implement operational strategies and improvements.",
                "Manage supply chain and logistics processes.",
                "Ensure quality control and compliance with company standards."
            ],
            "Average Salary (Globally)": "$70,000 - $105,000 annually.",
            "Education Requirements": "Bachelor's degree in Business, Operations Management, or related field.",
            "Advice": "Strong leadership and problem-solving skills are essential."
        },
        "Sales Manager": {
            "Key Responsibilities": [
                "Develop sales strategies to achieve company revenue goals.",
                "Lead and motivate the sales team to meet targets.",
                "Analyze sales performance and adjust strategies accordingly.",
                "Build and maintain relationships with key clients and partners."
            ],
            "Average Salary (Globally)": "$65,000 - $100,000 annually.",
            "Education Requirements": "Bachelor's degree in Sales, Marketing, or Business Administration.",
            "Advice": "Excellent communication and negotiation skills are key."
        },
        "Product Manager": {
            "Key Responsibilities": [
                "Oversee the development and lifecycle of products.",
                "Collaborate with cross-functional teams, including design and engineering.",
                "Conduct market research to identify customer needs.",
                "Define product vision and strategy, ensuring alignment with business goals."
            ],
            "Average Salary (Globally)": "$75,000 - $110,000 annually.",
            "Education Requirements": "Bachelor's degree in Business, Marketing, or related field.",
            "Advice": "Strong project management and leadership skills are essential."
        },
        "Entrepreneur": {
            "Key Responsibilities": [
                "Start and manage your own business ventures.",
                "Identify market opportunities and develop business plans.",
                "Raise capital and manage business finances.",
                "Create and lead teams to execute business ideas."
            ],
            "Average Salary (Globally)": "Varies widely based on business success.",
            "Education Requirements": "Varies; often a Bachelor's degree in Business or related field.",
            "Advice": "Risk-taking, resilience, and a passion for innovation are crucial."
        },
        "Business Development Manager": {
            "Key Responsibilities": [
                "Identify new business opportunities and markets.",
                "Build and maintain relationships with potential partners and clients.",
                "Develop strategic plans for business growth.",
                "Negotiate contracts and close deals."
            ],
            "Average Salary (Globally)": "$70,000 - $100,000 annually.",
            "Education Requirements": "Bachelor's degree in Business, Marketing, or related field.",
            "Advice": "Strong networking and negotiation skills are important."
        },
        "Management Consultant": {
            "Key Responsibilities": [
                "Advise companies on business strategies and improvements.",
                "Analyze business processes and recommend solutions.",
                "Work with senior management to implement changes.",
                "Provide expertise in various industries and functions."
            ],
            "Average Salary (Globally)": "$80,000 - $130,000 annually.",
            "Education Requirements": "Bachelor's degree in Business, Economics, or related field.",
            "Advice": "Problem-solving and analytical skills are essential."
        },
        "Supply Chain Manager": {
            "Key Responsibilities": [
                "Oversee the entire supply chain from procurement to delivery.",
                "Ensure efficient and cost-effective logistics operations.",
                "Monitor supplier performance and negotiate contracts.",
                "Implement strategies for inventory management and cost reduction."
            ],
            "Average Salary (Globally)": "$70,000 - $110,000 annually.",
            "Education Requirements": "Bachelor's degree in Supply Chain Management, Business, or related field.",
            "Advice": "Strong organizational and negotiation skills are key."
        },
        "Brand Manager": {
            "Key Responsibilities": [
                "Develop and execute brand strategies to increase brand visibility.",
                "Monitor brand performance and adjust strategies as needed.",
                "Collaborate with marketing and product teams to ensure brand consistency.",
                "Conduct market research to understand customer preferences."
            ],
            "Average Salary (Globally)": "$70,000 - $95,000 annually.",
            "Education Requirements": "Bachelor's degree in Marketing, Business, or related field.",
            "Advice": "Creativity and a deep understanding of consumer behavior are essential."
        },
        "Event Manager": {
            "Key Responsibilities": [
                "Plan and execute events, including conferences, weddings, and corporate gatherings.",
                "Manage budgets, timelines, and logistics.",
                "Negotiate with vendors and suppliers.",
                "Ensure event goals are met and attendees have a positive experience."
            ],
            "Average Salary (Globally)": "$50,000 - $80,000 annually.",
            "Education Requirements": "Bachelor's degree in Event Management, Business, or related field.",
            "Advice": "Strong organizational and multitasking skills are critical."
        },
        "Customer Success Manager": {
            "Key Responsibilities": [
                "Ensure customer satisfaction and retention by addressing issues.",
                "Work closely with clients to understand their needs and goals.",
                "Provide support and guidance throughout the customer lifecycle.",
                "Develop strategies to improve customer experiences."
            ],
            "Average Salary (Globally)": "$60,000 - $90,000 annually.",
            "Education Requirements": "Bachelor's degree in Business, Marketing, or related field.",
            "Advice": "Excellent communication and problem-solving skills are key."
        },
        "Corporate Strategist": {
            "Key Responsibilities": [
                "Develop long-term strategies to drive business growth.",
                "Analyze market trends and competitive landscapes.",
                "Collaborate with senior leadership to define company direction.",
                "Monitor industry changes and adapt strategies accordingly."
            ],
            "Average Salary (Globally)": "$90,000 - $140,000 annually.",
            "Education Requirements": "Bachelor's degree in Business, Economics, or related field.",
            "Advice": "Strong strategic thinking and analytical skills are essential."
        },
        "Real Estate Manager": {
            "Key Responsibilities": [
                "Oversee real estate transactions, including buying, selling, and leasing properties.",
                "Manage property portfolios and maximize profitability.",
                "Negotiate leases and sales agreements.",
                "Ensure compliance with zoning laws and regulations."
            ],
            "Average Salary (Globally)": "$60,000 - $95,000 annually.",
            "Education Requirements": "Bachelor's degree in Real Estate, Business, or related field.",
            "Advice": "Knowledge of market trends and legal regulations is crucial."
        },
        "Investment Banker": {
            "Key Responsibilities": [
                "Advise clients on financial investments and capital raising.",
                "Analyze financial data and market trends to guide investment decisions.",
                "Assist with mergers, acquisitions, and initial public offerings (IPOs).",
                "Negotiate and structure financial deals."
            ],
            "Average Salary (Globally)": "$100,000 - $150,000 annually.",
            "Education Requirements": "Bachelor's degree in Finance, Economics, or related field.",
            "Advice": "Strong analytical and negotiation skills are essential."
        },
        "Social Media Manager": {
            "Key Responsibilities": [
                "Create and manage social media content and campaigns.",
                "Monitor social media trends and engagement metrics.",
                "Develop strategies to increase followers and brand awareness.",
                "Collaborate with marketing and PR teams to align messaging."
            ],
            "Average Salary (Globally)": "$50,000 - $75,000 annually.",
            "Education Requirements": "Bachelor's degree in Marketing, Communications, or related field.",
            "Advice": "Creativity, communication skills, and an understanding of analytics are key."
        },
        "E-commerce Manager": {
            "Key Responsibilities": [
                "Oversee online sales platforms and digital marketing efforts.",
                "Develop strategies to optimize online sales and customer experience.",
                "Monitor inventory, pricing, and product listings.",
                "Collaborate with logistics and fulfillment teams."
            ],
            "Average Salary (Globally)": "$60,000 - $90,000 annually.",
            "Education Requirements": "Bachelor's degree in Business, Marketing, or related field.",
            "Advice": "Experience with digital marketing and e-commerce platforms is essential."
        },
        "Data Analyst": {
            "Key Responsibilities": [
                "Collect and analyze data to help businesses make informed decisions.",
                "Create data visualizations and reports.",
                "Identify trends and patterns in business operations.",
                "Collaborate with departments to understand data needs."
            ],
            "Average Salary (Globally)": "$55,000 - $80,000 annually.",
            "Education Requirements": "Bachelor's degree in Data Science, Business, or related field.",
            "Advice": "Strong skills in data analysis tools like Excel and SQL are essential."
        },
        "Content Strategist": {
            "Key Responsibilities": [
                "Develop and execute content strategies to support marketing goals.",
                "Collaborate with writers, designers, and marketing teams.",
                "Analyze content performance and adjust strategies.",
                "Ensure content aligns with brand messaging."
            ],
            "Average Salary (Globally)": "$60,000 - $85,000 annually.",
            "Education Requirements": "Bachelor's degree in Marketing, Communications, or related field.",
            "Advice": "Creativity, storytelling, and analytical skills are essential."
        },
        "PR Manager": {
            "Key Responsibilities": [
                "Manage public relations campaigns and media outreach.",
                "Develop and maintain relationships with journalists and media outlets.",
                "Write press releases and coordinate interviews.",
                "Monitor media coverage and manage crises."
            ],
            "Average Salary (Globally)": "$65,000 - $95,000 annually.",
            "Education Requirements": "Bachelor's degree in Public Relations, Communications, or related field.",
            "Advice": "Strong communication and media relations skills are essential."
        },
        "Accountant": {
            "Key Responsibilities": [
                "Prepare financial statements and manage accounts.",
                "Ensure compliance with tax laws and regulations.",
                "Analyze financial data and provide recommendations.",
                "Assist with budgeting and forecasting."
            ],
            "Average Salary (Globally)": "$50,000 - $75,000 annually.",
            "Education Requirements": "Bachelor's degree in Accounting, Finance, or related field.",
            "Advice": "Attention to detail and proficiency in accounting software are crucial."
        },
        "Legal Advisor": {
            "Key Responsibilities": [
                "Provide legal counsel on business transactions and contracts.",
                "Ensure compliance with laws and regulations.",
                "Draft and review contracts and agreements.",
                "Represent the company in legal matters."
            ],
            "Average Salary (Globally)": "$80,000 - $120,000 annually.",
            "Education Requirements": "Juris Doctor (JD) or equivalent legal degree.",
            "Advice": "Strong knowledge of business law and contract negotiation is essential."
        },
        "Compliance Officer": {
            "Key Responsibilities": [
                "Ensure that the company adheres to legal and regulatory requirements.",
                "Develop and implement compliance programs and policies.",
                "Conduct audits and investigations.",
                "Monitor industry regulations and adjust practices as necessary."
            ],
            "Average Salary (Globally)": "$70,000 - $100,000 annually.",
            "Education Requirements": "Bachelor's degree in Law, Business, or related field.",
            "Advice": "Attention to detail and a deep understanding of regulations are essential."
        },
        "Tax Consultant": {
            "Key Responsibilities": [
                "Advise businesses and individuals on tax planning and compliance.",
                "Prepare tax returns and ensure accuracy.",
                "Analyze tax laws and regulations to minimize tax liabilities.",
                "Represent clients in tax-related matters."
            ],
            "Average Salary (Globally)": "$65,000 - $100,000 annually.",
            "Education Requirements": "Bachelor's degree in Accounting, Finance, or related field.",
            "Advice": "A deep understanding of tax laws and strong analytical skills are crucial."
        },
        "Investment Analyst": {
            "Key Responsibilities": [
                "Analyze investment opportunities and market trends.",
                "Prepare reports on financial performance and investment potential.",
                "Assist with portfolio management and risk analysis.",
                "Conduct research on financial instruments and companies."
            ],
            "Average Salary (Globally)": "$70,000 - $110,000 annually.",
            "Education Requirements": "Bachelor's degree in Finance, Economics, or related field.",
            "Advice": "Strong analytical and research skills are essential."
        },
    },

    "Creative Arts": {
        "Graphic Designer": {
            "Key Responsibilities": [
                "Create visual concepts using computer software or by hand.",
                "Develop layouts and designs for websites, advertisements, and other media.",
                "Collaborate with clients and marketing teams to create designs that align with brand goals.",
                "Ensure designs are visually appealing and effective for target audiences."
            ],
            "Average Salary (Globally)": "$50,000 - $75,000 annually.",
            "Education Requirements": "Bachelor's degree in Graphic Design, Fine Arts, or related field.",
            "Advice": "Creativity, attention to detail, and proficiency in design software are key."
        },
        "Illustrator": {
            "Key Responsibilities": [
                "Create original illustrations for books, magazines, advertisements, and more.",
                "Work with clients to understand their vision and deliver designs accordingly.",
                "Use traditional or digital methods to create artwork.",
                "Collaborate with authors, designers, and other creatives to bring ideas to life."
            ],
            "Average Salary (Globally)": "$45,000 - $70,000 annually.",
            "Education Requirements": "Bachelor's degree in Illustration, Fine Arts, or related field.",
            "Advice": "Strong artistic skills and the ability to work with various mediums are essential."
        },
        "Photographer": {
            "Key Responsibilities": [
                "Capture high-quality images for clients in various settings, including portraits, events, and products.",
                "Edit and retouch photos to meet client specifications.",
                "Manage photography equipment and software.",
                "Market photography services and build a client base."
            ],
            "Average Salary (Globally)": "$40,000 - $65,000 annually.",
            "Education Requirements": "Bachelor's degree in Photography, Fine Arts, or related field.",
            "Advice": "Creativity, technical knowledge of cameras, and photo editing skills are key."
        },
        "Fashion Designer": {
            "Key Responsibilities": [
                "Design clothing, accessories, and footwear.",
                "Create patterns and prototypes for garments.",
                "Work with textiles, colors, and materials to develop new fashion lines.",
                "Collaborate with manufacturers and oversee production."
            ],
            "Average Salary (Globally)": "$60,000 - $90,000 annually.",
            "Education Requirements": "Bachelor's degree in Fashion Design or related field.",
            "Advice": "Creativity, trend awareness, and strong design skills are crucial."
        },
        "Art Director": {
            "Key Responsibilities": [
                "Oversee the visual aspects of an art project, including design, color, and layout.",
                "Collaborate with designers, illustrators, and photographers.",
                "Ensure that the visual direction aligns with the project’s goals and brand identity.",
                "Manage the creative process from concept to final output."
            ],
            "Average Salary (Globally)": "$75,000 - $120,000 annually.",
            "Education Requirements": "Bachelor's degree in Art, Design, or related field.",
            "Advice": "Leadership, creativity, and an eye for detail are key."
        },
        "Video Editor": {
            "Key Responsibilities": [
                "Edit raw video footage to create polished, engaging content.",
                "Add sound effects, music, and special effects.",
                "Collaborate with directors and producers to understand project vision.",
                "Ensure videos are visually appealing and meet technical standards."
            ],
            "Average Salary (Globally)": "$45,000 - $70,000 annually.",
            "Education Requirements": "Bachelor's degree in Film, Media Arts, or related field.",
            "Advice": "Attention to detail and proficiency in editing software are essential."
        },
        "Animator": {
            "Key Responsibilities": [
                "Create animated visuals for films, video games, and commercials.",
                "Design characters, backgrounds, and other elements.",
                "Work with directors and other creatives to bring stories to life.",
                "Use software to animate and edit sequences."
            ],
            "Average Salary (Globally)": "$55,000 - $80,000 annually.",
            "Education Requirements": "Bachelor's degree in Animation, Fine Arts, or related field.",
            "Advice": "Creativity, proficiency in animation software, and storytelling skills are key."
        },
        "Interior Designer": {
            "Key Responsibilities": [
                "Design functional and aesthetically pleasing interior spaces.",
                "Select furniture, color schemes, and decor elements.",
                "Work with clients to understand their needs and vision.",
                "Collaborate with contractors and architects to ensure designs are implemented."
            ],
            "Average Salary (Globally)": "$55,000 - $85,000 annually.",
            "Education Requirements": "Bachelor's degree in Interior Design or related field.",
            "Advice": "Creativity, spatial awareness, and strong communication skills are crucial."
        },
        "Set Designer": {
            "Key Responsibilities": [
                "Design and create sets for theater, television, and film productions.",
                "Collaborate with directors to create visual environments that support the story.",
                "Source materials and manage the construction of sets.",
                "Ensure sets are safe and functional for performers and crew."
            ],
            "Average Salary (Globally)": "$45,000 - $70,000 annually.",
            "Education Requirements": "Bachelor's degree in Set Design, Theater Arts, or related field.",
            "Advice": "Strong creativity and problem-solving skills are key."
        },
        "Sound Designer": {
            "Key Responsibilities": [
                "Create sound effects and audio for films, video games, and commercials.",
                "Record, edit, and manipulate audio to match project needs.",
                "Collaborate with directors and editors to ensure sound aligns with visuals.",
                "Ensure high-quality sound and audio levels in final production."
            ],
            "Average Salary (Globally)": "$50,000 - $80,000 annually.",
            "Education Requirements": "Bachelor's degree in Sound Design, Audio Engineering, or related field.",
            "Advice": "Attention to detail and technical proficiency in sound editing are essential."
        },
        "Fine Artist": {
            "Key Responsibilities": [
                "Create original artwork in various media such as painting, sculpture, or printmaking.",
                "Exhibit and sell artwork through galleries, online platforms, or commissions.",
                "Experiment with different techniques and materials.",
                "Promote and market artwork to collectors and clients."
            ],
            "Average Salary (Globally)": "$30,000 - $60,000 annually (can vary widely based on success).",
            "Education Requirements": "Bachelor's degree in Fine Arts or related field.",
            "Advice": "Strong artistic skills and a passion for self-expression are key."
        },
        "Curator": {
            "Key Responsibilities": [
                "Manage and organize art collections for museums, galleries, or cultural institutions.",
                "Research and acquire new pieces for exhibitions.",
                "Plan and install exhibitions and events.",
                "Maintain the care and preservation of art pieces."
            ],
            "Average Salary (Globally)": "$55,000 - $85,000 annually.",
            "Education Requirements": "Bachelor's degree in Art History, Museum Studies, or related field.",
            "Advice": "Strong organizational and research skills are essential."
        },
        "Theater Director": {
            "Key Responsibilities": [
                "Direct live theater productions, overseeing all aspects of performance.",
                "Collaborate with actors, designers, and crew to bring the vision to life.",
                "Guide actors' performances and provide feedback.",
                "Manage rehearsals and ensure the smooth operation of the production."
            ],
            "Average Salary (Globally)": "$50,000 - $80,000 annually.",
            "Education Requirements": "Bachelor's degree in Theater Arts or related field.",
            "Advice": "Leadership, creativity, and an understanding of theater are key."
        },
        "Voice Actor": {
            "Key Responsibilities": [
                "Provide voices for characters in animation, video games, and commercials.",
                "Work with directors to develop character voices and expressions.",
                "Record lines in a professional studio.",
                "Ensure voice acting aligns with the project’s tone and storyline."
            ],
            "Average Salary (Globally)": "$40,000 - $75,000 annually.",
            "Education Requirements": "Training in voice acting, theater, or related field.",
            "Advice": "A unique voice, creativity, and vocal range are essential."
        },
        "Web Designer": {
            "Key Responsibilities": [
                "Design the layout and user interface for websites.",
                "Ensure websites are visually appealing, functional, and user-friendly.",
                "Collaborate with developers to implement designs.",
                "Stay updated on web design trends and technologies."
            ],
            "Average Salary (Globally)": "$50,000 - $75,000 annually.",
            "Education Requirements": "Bachelor's degree in Web Design, Graphic Design, or related field.",
            "Advice": "Strong design and technical skills, as well as knowledge of web development, are key."
        },
        "Makeup Artist": {
            "Key Responsibilities": [
                "Apply makeup for theater, film, television, or personal clients.",
                "Create looks for special events, photoshoots, and performances.",
                "Stay up-to-date with beauty trends and techniques.",
                "Provide consultations and recommendations based on clients' needs."
            ],
            "Average Salary (Globally)": "$40,000 - $60,000 annually.",
            "Education Requirements": "Certification in Makeup Artistry or related field.",
            "Advice": "Creativity, attention to detail, and strong customer service skills are key."
        },
        "Sculptor": {
            "Key Responsibilities": [
                "Create sculptures in various materials, including clay, metal, and stone.",
                "Experiment with different techniques and artistic expressions.",
                "Collaborate with clients or institutions for commissioned works.",
                "Exhibit artwork in galleries or public spaces."
            ],
            "Average Salary (Globally)": "$40,000 - $70,000 annually.",
            "Education Requirements": "Bachelor's degree in Fine Arts or related field.",
            "Advice": "Strong creativity and hands-on skills in various mediums are essential."
        },
        "Choreographer": {
            "Key Responsibilities": [
                "Create and direct dance routines for performances.",
                "Collaborate with dancers, directors, and musicians.",
                "Teach dance movements and techniques to performers.",
                "Rehearse and refine routines for shows and productions."
            ],
            "Average Salary (Globally)": "$45,000 - $75,000 annually.",
            "Education Requirements": "Bachelor's degree in Dance, Theater Arts, or related field.",
            "Advice": "Strong dance technique and leadership skills are key."
        },
        "Sound Engineer": {
            "Key Responsibilities": [
                "Operate audio equipment for live events, film, or music production.",
                "Record, mix, and master audio recordings.",
                "Collaborate with artists, producers, and directors to ensure high-quality sound.",
                "Ensure technical quality of audio in various formats."
            ],
            "Average Salary (Globally)": "$45,000 - $70,000 annually.",
            "Education Requirements": "Bachelor's degree in Sound Engineering, Audio Production, or related field.",
            "Advice": "Technical proficiency in sound equipment and software is essential."
        },
        "Film Director": {
            "Key Responsibilities": [
                "Direct films, overseeing all aspects of production.",
                "Work with actors, screenwriters, and producers to bring the story to life.",
                "Guide the film’s visual and narrative direction.",
                "Ensure the final product aligns with the creative vision."
            ],
            "Average Salary (Globally)": "$70,000 - $120,000 annually.",
            "Education Requirements": "Bachelor's degree in Film Production, Directing, or related field.",
            "Advice": "Leadership, creativity, and storytelling skills are key."
        },
    },

    "Psychology and Therapy": {
        "Clinical Psychologist": {
            "Key Responsibilities": [
                "Assess and diagnose mental health disorders.",
                "Provide therapy and counseling to individuals, couples, and families.",
                "Develop treatment plans and monitor patient progress.",
                "Conduct psychological research and contribute to the field."
            ],
            "Average Salary (Globally)": "$70,000 - $100,000 annually.",
            "Education Requirements": "Doctorate in Clinical Psychology (Ph.D. or Psy.D.).",
            "Advice": "Strong analytical skills and empathy are crucial for success."
        },
        "Counseling Psychologist": {
            "Key Responsibilities": [
                "Provide counseling to individuals and groups.",
                "Assist clients in managing emotional and psychological issues.",
                "Offer support for personal, social, and career development.",
                "Use a variety of therapeutic techniques to address mental health challenges."
            ],
            "Average Salary (Globally)": "$50,000 - $80,000 annually.",
            "Education Requirements": "Master’s or Doctoral degree in Counseling Psychology.",
            "Advice": "Excellent communication and active listening skills are key."
        },
        "Marriage and Family Therapist": {
            "Key Responsibilities": [
                "Provide therapy to couples and families to address relationship issues.",
                "Help clients navigate family dynamics and conflicts.",
                "Offer guidance on communication, conflict resolution, and emotional support.",
                "Develop treatment plans tailored to each family or couple."
            ],
            "Average Salary (Globally)": "$50,000 - $75,000 annually.",
            "Education Requirements": "Master’s degree in Marriage and Family Therapy (MFT).",
            "Advice": "Empathy, patience, and conflict resolution skills are essential."
        },
        "School Psychologist": {
            "Key Responsibilities": [
                "Assess and support the mental health needs of students.",
                "Provide counseling to students dealing with academic, social, or emotional issues.",
                "Collaborate with teachers and parents to support student development.",
                "Conduct assessments and create individualized education plans (IEPs)."
            ],
            "Average Salary (Globally)": "$60,000 - $85,000 annually.",
            "Education Requirements": "Master’s or Doctoral degree in School Psychology.",
            "Advice": "Strong communication skills and a passion for helping children are key."
        },
        "Industrial-Organizational Psychologist": {
            "Key Responsibilities": [
                "Apply psychological principles to workplace issues, such as employee performance and motivation.",
                "Conduct research on organizational behavior and employee satisfaction.",
                "Design and implement programs to improve workplace productivity.",
                "Consult with organizations to improve their overall effectiveness."
            ],
            "Average Salary (Globally)": "$80,000 - $120,000 annually.",
            "Education Requirements": "Master’s or Doctoral degree in Industrial-Organizational Psychology.",
            "Advice": "Strong analytical and problem-solving skills are essential."
        },
        "Forensic Psychologist": {
            "Key Responsibilities": [
                "Apply psychological principles to the legal system.",
                "Evaluate the mental health of individuals involved in criminal cases.",
                "Assist in criminal investigations and provide expert testimony in court.",
                "Work with law enforcement agencies to assess criminal behavior."
            ],
            "Average Salary (Globally)": "$60,000 - $100,000 annually.",
            "Education Requirements": "Doctoral degree in Forensic Psychology.",
            "Advice": "Knowledge of both psychology and law is crucial for success."
        },
        "Health Psychologist": {
            "Key Responsibilities": [
                "Study how psychological factors affect physical health.",
                "Help patients manage chronic illnesses and health conditions.",
                "Develop programs to promote healthy behaviors and prevent disease.",
                "Provide counseling for individuals coping with health-related stress."
            ],
            "Average Salary (Globally)": "$65,000 - $90,000 annually.",
            "Education Requirements": "Doctoral degree in Health Psychology.",
            "Advice": "Understanding of both psychological and medical principles is important."
        },
        "Addiction Counselor": {
            "Key Responsibilities": [
                "Provide therapy and counseling to individuals struggling with substance abuse or addiction.",
                "Help clients understand the psychological and emotional factors contributing to their addiction.",
                "Develop treatment plans and support recovery goals.",
                "Offer group and individual therapy sessions."
            ],
            "Average Salary (Globally)": "$40,000 - $60,000 annually.",
            "Education Requirements": "Master’s degree in Counseling or Psychology.",
            "Advice": "Patience, empathy, and the ability to handle challenging situations are key."
        },
        "Child Psychologist": {
            "Key Responsibilities": [
                "Assess and treat mental health issues in children and adolescents.",
                "Provide therapy to help children cope with emotional or behavioral problems.",
                "Collaborate with parents and educators to support child development.",
                "Conduct psychological assessments and create treatment plans."
            ],
            "Average Salary (Globally)": "$60,000 - $90,000 annually.",
            "Education Requirements": "Doctoral degree in Psychology with a focus on children.",
            "Advice": "Understanding of child development and strong communication with both children and parents is crucial."
        },
        "Neuropsychologist": {
            "Key Responsibilities": [
                "Assess brain function and diagnose cognitive and neurological disorders.",
                "Conduct brain scans and neuropsychological testing.",
                "Provide therapy for individuals with brain injuries, neurological conditions, or cognitive impairments.",
                "Work with medical professionals to develop treatment plans."
            ],
            "Average Salary (Globally)": "$80,000 - $120,000 annually.",
            "Education Requirements": "Doctoral degree in Neuropsychology.",
            "Advice": "A strong understanding of brain function and cognition is essential."
        },
        "Sports Psychologist": {
            "Key Responsibilities": [
                "Help athletes improve performance through mental conditioning and therapy.",
                "Address psychological issues affecting athletic performance, such as stress or anxiety.",
                "Work with coaches and teams to foster positive mental health.",
                "Conduct research on sports psychology and athlete behavior."
            ],
            "Average Salary (Globally)": "$60,000 - $100,000 annually.",
            "Education Requirements": "Master’s or Doctoral degree in Sports Psychology.",
            "Advice": "Understanding both psychology and athletic performance is key."
        },
        "Psychiatrist": {
            "Key Responsibilities": [
                "Diagnose and treat mental health disorders using medical interventions.",
                "Prescribe medications and provide psychotherapy.",
                "Monitor patient progress and adjust treatments as needed.",
                "Collaborate with other healthcare providers to ensure comprehensive care."
            ],
            "Average Salary (Globally)": "$150,000 - $250,000 annually.",
            "Education Requirements": "Medical degree (MD) and specialization in Psychiatry.",
            "Advice": "Strong medical knowledge combined with empathy and understanding of mental health issues is essential."
        },
        "Psychotherapy Counselor": {
            "Key Responsibilities": [
                "Provide individual, couples, and family therapy.",
                "Help clients work through emotional and psychological challenges.",
                "Use different therapeutic techniques such as CBT, psychodynamic therapy, and more.",
                "Work with clients to set goals and monitor progress."
            ],
            "Average Salary (Globally)": "$45,000 - $70,000 annually.",
            "Education Requirements": "Master’s degree in Counseling or Psychology.",
            "Advice": "Good listening skills, empathy, and knowledge of therapeutic techniques are key."
        },
        "Art Therapist": {
            "Key Responsibilities": [
                "Use art-making as a therapeutic tool to help clients express emotions and work through psychological issues.",
                "Work with individuals, groups, and families to explore feelings and promote healing.",
                "Integrate various art forms into therapy, such as drawing, painting, and sculpture.",
                "Develop personalized treatment plans for clients."
            ],
            "Average Salary (Globally)": "$45,000 - $65,000 annually.",
            "Education Requirements": "Master’s degree in Art Therapy.",
            "Advice": "Creativity and the ability to understand non-verbal communication are essential."
        },
        "Music Therapist": {
            "Key Responsibilities": [
                "Use music as a therapeutic tool to help clients manage emotions, reduce stress, and improve mental health.",
                "Provide individual or group therapy sessions using music-based interventions.",
                "Work with clients of all ages to address emotional, psychological, and physical challenges.",
                "Develop personalized music therapy programs."
            ],
            "Average Salary (Globally)": "$50,000 - $75,000 annually.",
            "Education Requirements": "Master’s degree in Music Therapy.",
            "Advice": "A strong background in music and a passion for helping others is key."
        },
        "Dance/Movement Therapist": {
            "Key Responsibilities": [
                "Use dance and movement as therapeutic tools to help clients express emotions and address psychological issues.",
                "Guide clients through movement exercises that promote healing and self-awareness.",
                "Work with individuals or groups to foster physical and emotional well-being.",
                "Develop treatment plans based on clients’ needs."
            ],
            "Average Salary (Globally)": "$45,000 - $65,000 annually.",
            "Education Requirements": "Master’s degree in Dance/Movement Therapy.",
            "Advice": "A background in dance and understanding of psychological principles are essential."
        },
        "Play Therapist": {
            "Key Responsibilities": [
                "Use play-based techniques to help children express feelings and resolve psychological issues.",
                "Work with children in individual or group settings to foster emotional and social development.",
                "Incorporate toys, games, and activities into therapy.",
                "Develop treatment plans tailored to each child’s needs."
            ],
            "Average Salary (Globally)": "$50,000 - $70,000 annually.",
            "Education Requirements": "Master’s degree in Play Therapy or Counseling.",
            "Advice": "Creativity and patience are key when working with children."
        },
        "Therapeutic Foster Parent": {
            "Key Responsibilities": [
                "Provide a safe and supportive home environment for children in foster care.",
                "Work with therapists and social workers to address children’s emotional and psychological needs.",
                "Offer counseling and emotional support to foster children.",
                "Help children navigate difficult life experiences and develop coping strategies."
            ],
            "Average Salary (Globally)": "$30,000 - $50,000 annually.",
            "Education Requirements": "No specific degree required, but training in foster care and therapy is beneficial.",
            "Advice": "Patience, empathy, and the ability to work as part of a team are essential."
        },
        "Behavioral Therapist": {
            "Key Responsibilities": [
                "Provide therapy to individuals with behavioral issues or disorders.",
                "Use techniques like Applied Behavior Analysis (ABA) to address challenges.",
                "Work with clients to develop better coping mechanisms and behaviors.",
                "Monitor progress and adjust treatment plans as necessary."
            ],
            "Average Salary (Globally)": "$50,000 - $70,000 annually.",
            "Education Requirements": "Master’s degree in Psychology or Applied Behavior Analysis.",
            "Advice": "Strong understanding of behavior modification techniques is key."
        },
    },

    "Criminal Justice and Legal Studies": {
        "Criminal Lawyer": {
            "Key Responsibilities": [
                "Represent clients in criminal cases, ensuring a fair trial.",
                "Provide legal advice to clients facing criminal charges.",
                "Research case law, statutes, and evidence to build a defense.",
                "Negotiate settlements or plea deals with prosecutors."
            ],
            "Average Salary (Globally)": "$70,000 - $150,000 annually.",
            "Education Requirements": "Juris Doctor (JD) degree and passing the bar exam.",
            "Advice": "Strong legal knowledge and persuasive communication skills are essential."
        },
        "Prosecutor": {
            "Key Responsibilities": [
                "Represent the government in criminal cases, seeking justice for victims.",
                "Prepare legal documents and present evidence in court.",
                "Interview witnesses and prepare for trial.",
                "Work closely with law enforcement agencies to investigate crimes."
            ],
            "Average Salary (Globally)": "$70,000 - $120,000 annually.",
            "Education Requirements": "Juris Doctor (JD) degree and passing the bar exam.",
            "Advice": "Attention to detail and a strong sense of justice are key."
        },
        "Defense Attorney": {
            "Key Responsibilities": [
                "Defend individuals or organizations accused of criminal conduct.",
                "Prepare defense strategies and present evidence in court.",
                "Advise clients on their legal rights and potential outcomes.",
                "Negotiate plea deals with prosecutors."
            ],
            "Average Salary (Globally)": "$60,000 - $140,000 annually.",
            "Education Requirements": "Juris Doctor (JD) degree and passing the bar exam.",
            "Advice": "Strong advocacy skills and a deep understanding of the law are essential."
        },
        "Judge": {
            "Key Responsibilities": [
                "Preside over legal proceedings in courts of law.",
                "Ensure fair trials by applying the law impartially.",
                "Issue rulings and sentences based on evidence and legal arguments.",
                "Provide instructions to juries and ensure courtroom decorum."
            ],
            "Average Salary (Globally)": "$100,000 - $200,000 annually.",
            "Education Requirements": "Juris Doctor (JD) degree, legal experience, and judicial appointment.",
            "Advice": "Impartiality and deep legal knowledge are crucial for success."
        },
        "Paralegal": {
            "Key Responsibilities": [
                "Assist lawyers in preparing for trials and hearings.",
                "Research legal precedents and statutes.",
                "Draft legal documents such as contracts and briefs.",
                "Manage case files and client records."
            ],
            "Average Salary (Globally)": "$45,000 - $70,000 annually.",
            "Education Requirements": "Associate's or Bachelor's degree in Paralegal Studies.",
            "Advice": "Organizational skills and attention to detail are key."
        },
        "Legal Secretary": {
            "Key Responsibilities": [
                "Provide administrative support to lawyers and legal teams.",
                "Prepare legal documents and correspondence.",
                "Manage schedules and appointments for legal professionals.",
                "File and organize case materials."
            ],
            "Average Salary (Globally)": "$40,000 - $60,000 annually.",
            "Education Requirements": "High school diploma with legal secretary certification or relevant degree.",
            "Advice": "Strong organizational and communication skills are essential."
        },
        "Court Reporter": {
            "Key Responsibilities": [
                "Record verbatim transcripts of court proceedings.",
                "Provide real-time transcription for hearings and trials.",
                "Ensure accurate and complete records of legal proceedings.",
                "Work closely with legal professionals to provide transcripts when needed."
            ],
            "Average Salary (Globally)": "$50,000 - $80,000 annually.",
            "Education Requirements": "Court reporting certificate or degree, plus certification.",
            "Advice": "Attention to detail and fast typing skills are crucial."
        },
        "Private Investigator": {
            "Key Responsibilities": [
                "Conduct investigations for clients, often involving criminal cases or civil disputes.",
                "Gather evidence and perform surveillance.",
                "Interview witnesses and suspects.",
                "Prepare detailed reports for clients or legal professionals."
            ],
            "Average Salary (Globally)": "$50,000 - $90,000 annually.",
            "Education Requirements": "High school diploma with relevant certifications or a degree in Criminal Justice.",
            "Advice": "Discretion, persistence, and problem-solving skills are essential."
        },
        "Forensic Scientist": {
            "Key Responsibilities": [
                "Analyze physical evidence from crime scenes.",
                "Work in labs to perform tests on substances such as blood, DNA, or drugs.",
                "Provide expert testimony in court about the findings.",
                "Collaborate with law enforcement agencies to solve crimes."
            ],
            "Average Salary (Globally)": "$60,000 - $100,000 annually.",
            "Education Requirements": "Bachelor's or Master's degree in Forensic Science or a related field.",
            "Advice": "A strong background in science and attention to detail is essential."
        },
        "Forensic Pathologist": {
            "Key Responsibilities": [
                "Conduct autopsies to determine the cause of death.",
                "Analyze tissue samples and body fluids.",
                "Provide expert testimony in criminal cases.",
                "Work with law enforcement to solve crimes involving death."
            ],
            "Average Salary (Globally)": "$150,000 - $250,000 annually.",
            "Education Requirements": "Medical degree (MD) with specialization in Forensic Pathology.",
            "Advice": "Strong analytical skills and a commitment to solving complex cases are key."
        },
        "Crime Scene Investigator (CSI)": {
            "Key Responsibilities": [
                "Collect evidence from crime scenes, including physical items and digital evidence.",
                "Take photographs and document crime scenes.",
                "Work with forensic scientists to analyze collected evidence.",
                "Write detailed reports for legal use."
            ],
            "Average Salary (Globally)": "$50,000 - $75,000 annually.",
            "Education Requirements": "Bachelor's degree in Criminal Justice or Forensic Science.",
            "Advice": "Attention to detail and strong problem-solving skills are crucial."
        },
        "Criminal Profiler": {
            "Key Responsibilities": [
                "Analyze criminal behavior to develop profiles of suspects.",
                "Work with law enforcement to assist in criminal investigations.",
                "Provide insight into the psychological and behavioral patterns of offenders.",
                "Assist in solving complex criminal cases."
            ],
            "Average Salary (Globally)": "$70,000 - $100,000 annually.",
            "Education Requirements": "Bachelor’s degree in Psychology or Criminal Justice, plus experience in law enforcement.",
            "Advice": "Strong analytical and behavioral assessment skills are key."
        },
        "Bailiff": {
            "Key Responsibilities": [
                "Maintain order in the courtroom.",
                "Escort defendants and witnesses during trials.",
                "Serve legal documents and assist the judge and jury.",
                "Ensure that court proceedings run smoothly."
            ],
            "Average Salary (Globally)": "$35,000 - $55,000 annually.",
            "Education Requirements": "High school diploma, plus on-the-job training or certification.",
            "Advice": "Patience, authority, and attention to detail are key."
        },
        "Probation Officer": {
            "Key Responsibilities": [
                "Monitor individuals on probation to ensure compliance with court orders.",
                "Conduct home visits and drug tests.",
                "Prepare reports for the court on probationers’ progress.",
                "Assist in rehabilitation efforts for offenders."
            ],
            "Average Salary (Globally)": "$50,000 - $70,000 annually.",
            "Education Requirements": "Bachelor's degree in Criminal Justice or a related field.",
            "Advice": "Strong communication and problem-solving skills are essential."
        },
        "Criminal Investigator": {
            "Key Responsibilities": [
                "Investigate criminal activities and gather evidence.",
                "Interview suspects and witnesses.",
                "Analyze evidence to solve cases.",
                "Work closely with other law enforcement officers to close cases."
            ],
            "Average Salary (Globally)": "$60,000 - $100,000 annually.",
            "Education Requirements": "Bachelor's degree in Criminal Justice or Law Enforcement.",
            "Advice": "Attention to detail and strong analytical skills are crucial."
        },
        "Intelligence Analyst": {
            "Key Responsibilities": [
                "Analyze data and intelligence to identify criminal activity.",
                "Work with law enforcement agencies to combat organized crime and terrorism.",
                "Prepare reports and presentations for law enforcement leaders.",
                "Monitor trends and threats in criminal activities."
            ],
            "Average Salary (Globally)": "$60,000 - $90,000 annually.",
            "Education Requirements": "Bachelor’s degree in Criminal Justice, Intelligence, or a related field.",
            "Advice": "Analytical thinking and the ability to work under pressure are essential."
        },
        "Legal Consultant": {
            "Key Responsibilities": [
                "Provide expert advice on legal matters to clients or businesses.",
                "Analyze legal documents and contracts.",
                "Offer strategic advice on legal risks and solutions.",
                "Assist in compliance with regulations and laws."
            ],
            "Average Salary (Globally)": "$80,000 - $150,000 annually.",
            "Education Requirements": "Juris Doctor (JD) degree and relevant experience.",
            "Advice": "A deep understanding of legal principles and excellent communication skills are essential."
        },
        "Civil Rights Lawyer": {
            "Key Responsibilities": [
                "Advocate for individuals whose civil rights have been violated.",
                "Represent clients in cases related to discrimination, police brutality, and human rights.",
                "Research and prepare legal documents and court cases.",
                "Provide legal counsel on civil rights issues."
            ],
            "Average Salary (Globally)": "$70,000 - $130,000 annually.",
            "Education Requirements": "Juris Doctor (JD) degree and passing the bar exam.",
            "Advice": "A passion for justice and advocacy is key."
        },
        "Environmental Lawyer": {
            "Key Responsibilities": [
                "Advocate for environmental protection laws and policies.",
                "Represent clients in environmental disputes, such as pollution cases.",
                "Research environmental laws and regulations.",
                "Provide legal counsel on environmental issues."
            ],
            "Average Salary (Globally)": "$75,000 - $120,000 annually.",
            "Education Requirements": "Juris Doctor (JD) degree with specialization in environmental law.",
            "Advice": "A passion for environmental issues and legal expertise are crucial."
        },
        "Corporate Lawyer": {
            "Key Responsibilities": [
                "Provide legal advice to businesses on corporate governance and transactions.",
                "Draft contracts, mergers, and acquisitions documents.",
                "Represent clients in corporate disputes and negotiations.",
                "Ensure compliance with business laws and regulations."
            ],
            "Average Salary (Globally)": "$100,000 - $250,000 annually.",
            "Education Requirements": "Juris Doctor (JD) degree with specialization in corporate law.",
            "Advice": "Strong business acumen and legal expertise are essential."
        },
        "Family Lawyer": {
            "Key Responsibilities": [
                "Advise clients on family law matters, including divorce and child custody.",
                "Represent clients in family law court cases.",
                "Negotiate settlements and resolve family disputes.",
                "Draft legal documents related to family matters."
            ],
            "Average Salary (Globally)": "$60,000 - $110,000 annually.",
            "Education Requirements": "Juris Doctor (JD) degree with specialization in family law.",
            "Advice": "Empathy and strong negotiation skills are key."
        },
    },
}









# Display career options and details based on the user's interest
if career_area in career_details:
    careers = career_details[career_area]
    career_choice = st.selectbox("Choose a career to explore:", list(careers.keys()))
    selected_career = careers[career_choice]
    
    st.subheader(career_choice)
    st.write("### Key Responsibilities:")
    for responsibility in selected_career["Key Responsibilities"]:
        st.write(f"- {responsibility}")
    st.write(f"### Average Salary (Globally): {selected_career['Average Salary (Globally)']}")
    st.write(f"### Education Requirements: {selected_career['Education Requirements']}")
    st.write(f"### Advice: {selected_career['Advice']}")
