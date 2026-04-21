def get_university_info():
    return {
        'overview': [
            '🎓 Guru Gobind Singh Indraprastha University (GGSIPU) is a renowned state university located in Dwarka, Delhi.',
            '🏫 Established: 1998 by the Government of NCT of Delhi.',
            '🌐 Website: http://www.ipu.ac.in',
            '📞 Contact: 011-25302170',
            '🏅 Accredited with NAAC "A++" Grade, UGC recognized.',
            '📜 Motto: "Vidya Vardhanam Upaya" (Education is the means of enhancement).'
        ],
        'facilities': [
            '🏢 Facilities at GGSIPU include:',
            '- Modern classrooms and lecture halls',
            '- Well-equipped laboratories',
            '- Central and departmental libraries with extensive collections',
            '- Sports complex and grounds for cricket, football, basketball, athletics, etc.',
            '- On-campus hostels for students',
            '- Cafeterias and food courts',
            '- Medical and health services',
            '- Wi-Fi enabled campus',
            '- Innovation and entrepreneurship labs (AICTE IDEA Lab)'
        ],
        'admissions': {
            'process': [
                '📝 General Admission Process:',
                '1. Online Application via official portal',
                '2. Document Verification',
                '3. Entrance Test (CET) or Merit List (as per program)',
                '4. Counselling and seat allocation',
                '5. Fee Payment and confirmation',
                '🔗 More info: http://www.ipu.ac.in/admission2025main2.php'
            ],
            'international': [
                '🌍 International Admissions:',
                '- GGSIPU welcomes international students.',
                '- Separate guidelines and eligibility criteria apply.',
                '- Visit the International Affairs section on the university website for details.'
            ]
        },
        'academics': [
            '📚 Academic Schools and Centres:',
            '- School of Information, Communication & Technology',
            '- School of Education',
            '- School of Biotechnology',
            '- School of Chemical Technology',
            '- School of Management Studies',
            '- School of Law & Legal Studies',
            '- School of Environment Management',
            '- School of Basic & Applied Science',
            '- School of Humanities & Social Sciences',
            '- School of Mass Communication',
            '- School of Architecture & Planning',
            '- School of Medicine and Allied Health Sciences',
            '- School of Liberal Arts',
            '🔗 Full list & syllabi: http://www.ipu.ac.in/syll.php'
        ],
        'programs': [
            '🎓 Programs Offered:',
            '- Undergraduate: B.Tech, BBA, BCA, BA, B.Sc, B.Ed, LLB, etc.',
            '- Postgraduate: M.Tech, MBA, MCA, MA, M.Sc, M.Ed, LLM, etc.',
            '- Doctoral: Ph.D. in various disciplines',
            '- Diploma/Certificate: Various short-term and professional courses'
        ],
        'faculty_research': [
            '👩‍🏫 Faculty & Research:',
            '- 100+ faculty members across various departments',
            '- 2,600+ research publications, 9 patents, 27,000+ citations',
            '- Active research and development cell',
            '- Notable faculty: Dr. Satyabrata Mohapatra, Dr. Prakash Chand Sharma, Prof. Gagan Deep Sharma, and more',
            '🔗 Faculty profiles & research: https://ipu.irins.org/'
        ],
        'examinations': [
            '📝 Examinations:',
            '- Conducted by the Examination Department',
            '- Regular updates on datesheets and results',
            '- Online access to exam notices, forms, and results',
            '🔗 Datesheet: http://www.ipu.ac.in/exam_datesheet.php',
            '🔗 Results: http://ggsipu.ac.in/ExamResults/ExamResultsmain.htm',
            '🔗 Notices: http://www.ipu.ac.in/exam_notices.php'
        ],
        'student_life': [
            '🎉 Student Life & Support:',
            '- Student Council and welfare activities',
            '- Sports and cultural events',
            '- Industry linkage and placement cell',
            '- Alumni portal for networking',
            '- NSS & NCC cells for social and national service',
            '- Grievance redressal and support services',
            '🔗 Sports: http://www.ipu.ac.in/sports.php'
        ],
        'administration': [
            '🏛️ Administration:',
            '- Vice Chancellor: Head of the university',
            '- Registrar: Administrative head',
            '- Multiple administrative departments and statutory bodies',
            '- Legal aid and staff development cell',
            '🔗 About administration: http://www.ipu.ac.in/aboutuni.php'
        ],
        'contact': [
            '📞 Contact Information:',
            '- Address: Sector 16C, Dwarka, Delhi - 110078',
            '- Phone: 011-25302170',
            '- Email: info@ipu.ac.in',
            '- Website: http://www.ipu.ac.in'
        ]
    }

def get_response(query):
    query = query.lower()
    info = get_university_info()

    if 'overview' in query:
        return '\n'.join(info['overview'])
    elif 'facilities' in query:
        return '\n'.join(info['facilities'])
    elif 'admission' in query:
        if 'international' in query:
            return '\n'.join(info['admissions']['international'])
        return '\n'.join(info['admissions']['process'])
    elif 'academics' in query or 'school' in query or 'centre' in query:
        return '\n'.join(info['academics'])
    elif 'program' in query or 'course' in query:
        return '\n'.join(info['programs'])
    elif 'faculty' in query or 'research' in query:
        return '\n'.join(info['faculty_research'])
    elif 'exam' in query or 'result' in query or 'datesheet' in query:
        return '\n'.join(info['examinations'])
    elif 'student' in query or 'life' in query or 'hostel' in query or 'sports' in query:
        return '\n'.join(info['student_life'])
    elif 'admin' in query or 'vice chancellor' in query or 'registrar' in query:
        return '\n'.join(info['administration'])
    elif 'contact' in query or 'address' in query or 'phone' in query or 'email' in query:
        return '\n'.join(info['contact'])

    return None