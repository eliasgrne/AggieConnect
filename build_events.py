"""Builds aggieconnect_events.csv from public NC A&T pages collected on Oct 4, 2026.
Every row keeps the URL of the public page it came from."""
import csv

A930 = "https://hub.ncat.edu/administration/chancellor/university-relations/announcements/faculty-staff/2026-9-30.php"
A923 = "https://hub.ncat.edu/administration/chancellor/university-relations/announcements/faculty-staff/2026-9-23.php"
A909 = "https://hub.ncat.edu/administration/chancellor/university-relations/announcements/faculty-staff/2026-9-9.php"
CAL = "https://www.ncat.edu/calendar/"
FB = "https://ncataggies.com/sports/football/schedule/2026"
VB = "https://ncataggies.com/sports/womens-volleyball/schedule/2026"
HC = "https://ncat.edu/homecoming/students.php"

# title, date, location, organization, category, description, source_url
R = [
# ---- A&T Announcements, Sept. 30, 2026 edition
("Auditions: E. Gwynn Dancers of N.C. A&T", "2026-09-30", "General Classroom Building A321F", "Department of Visual and Performing Arts", "Arts and Performance", "Love to dance? Looking to explore a variety of dance forms? Come join the E. Gwynn Dancers.", A930),
("Research Impact: Assessing and Tracking Your Research", "2026-10-01", "Virtual", "F.D. Bluford Library", "Research and Library", "Workshop on tracking, analyzing and visualizing the impact of published research and planning a research trajectory.", A930),
("Navigating the Open Access Landscape", "2026-10-06", "Virtual", "F.D. Bluford Library", "Research and Library", "Learn strategies for maximizing the reach and impact of your research, managing article processing charges and avoiding predatory publishers.", A930),
("Unlocking Your Publishing Potential", "2026-10-08", "Virtual", "F.D. Bluford Library", "Research and Library", "Library support for publishing monographs, white papers, journals and other online publications.", A930),
("Decode: Copyright in the Digital Age", "2026-10-15", "Virtual", "F.D. Bluford Library", "Research and Library", "Interactive workshop on copyright, fair use, public domain, open source and digitization.", A930),
("Using ORCID to Establish a Strong Researcher Identity", "2026-10-08", "Zoom", "F.D. Bluford Library", "Research and Library", "Bluford Library workshop. Creating an ORCID iD will help you to create and maintain a strong research identity.", CAL + "2026/09/bluford-library-online-workshops-using-orcid-to-establish-a-strong-researcher-identity.php"),
("Study Abroad Information Session (In Person)", "2026-10-02", "Frye Hall 213", "Office of International Affairs", "Global and International", "All N.C. A&T students interested in studying, interning, volunteering or conducting research abroad are required to attend. Covers program types, destinations, scholarships and application timelines.", A930),
("Study Abroad Information Session (Zoom)", "2026-10-23", "Zoom", "Office of International Affairs", "Global and International", "Overview of program types, destinations, scholarships, application timelines and steps to begin a global experience.", A923),
("4th Annual Divine Nine Project Access Event", "2026-10-06", "Union Square Campus", "Department of Physician Assistant Studies", "Health", "Outreach connecting underrepresented students to the Physician Assistant profession and career opportunities.", A930),
("The Progressive Toastmasters Open House: A New Season of Change", "2026-10-06", "General Classroom Building 116A", "The Progressive Toastmasters", "Career and Professional", "Open house to improve public speaking skills, enhance leadership abilities, network and meet new people.", A930),
("Faculty Technical Speaker Series: Dr. Bruna Heinsfeld", "2026-10-07", "Frye Hall 108", "Office of Honors Research", "Technology and Engineering", "Faculty Technical Speaker Series featuring Dr. Bruna Heinsfeld on emerging technologies.", A930),
("Joanna Arteaga Ferrin: Reclaiming the Latine/x Narrative Through Art, Memory, and Resistance", "2026-10-08", "Dudley Building 202", "Department of Visual and Performing Arts and Center of Excellence for Social Justice", "Culture and Social Justice", "Art historian explores the intersection of social justice and Latin American art histories.", A930),
("Make the Most of Your Benefits: Resources Support Your Success", "2026-10-13", "Deese Ballroom, Student Center", "Department of Human Resources", "Faculty and Staff", "Benefits and resource fair to connect with benefits providers, campus partners and community organizations that support your health, total wellness and financial security.", A930),
("2026 Faculty and Staff Combined Campaign Kickoff", "2026-10-13", "Alumni-Foundation Event Center", "Faculty and Staff Combined Campaign Committee", "Faculty and Staff", "Annual campaign kickoff celebrating the spirit of giving with lunch, prizes and fellowship.", A930),
("N.C. A&T Physician Assistant Studies Virtual Open House", "2026-10-14", "Virtual", "Department of Physician Assistant Studies", "Health", "Information on the PA profession, program requirements and student experiences.", A930),
("GRADS-4C Fall 2026 Speaker Series", "2026-10-15", "Virtual", "Department of Biology", "Health", "Dr. Roshonda Jones discusses connections between diet, the gut microbiome and cognitive health.", A930),
("Center of Excellence for Social Justice Scholar-in-Residence Lecture: Pierce Freelon", "2026-10-15", "General Classroom Building 218", "Center of Excellence for Social Justice", "Culture and Social Justice", "Pierce Freelon presents The Best Way to Predict the Future Is to Create It, on Afrofuturist creativity, storytelling and children's media.", A930),
("Veterans Employment Base Camp Fall Educational Conference", "2026-10-16", "N.C. A&T State University Farm", "Veterans Employment Base Camp and Farmer Veterans Coalition", "Agriculture", "Conference will include marketing for small business, business plans and a farm tour for veteran farmers and ranchers.", A930),
("From Concept to Implementation: Faculty-Led Study Abroad", "2026-10-22", "Virtual", "Office of International Affairs", "Faculty and Staff", "Webinar on developing and leading faculty-led programs with guidance on policies and design.", A930),
("2026 Provost's Faculty Fellows Poster Presentations", "2026-10-23", "Virtual", "Office of the Provost", "Technology and Engineering", "Celebration of AI-enhanced interdisciplinary research across ten innovative research areas.", A930),
("Centennial GHOE Celebration", "2026-10-25", "Campus-wide", "University Events", "Homecoming and Student Life", "Known worldwide as the Greatest Homecoming on Earth, this week-long centennial reunion brings together generations of Aggies to celebrate excellence, heritage and the bond of the Blue and Gold.", A930),
("Aggie Pathways Abroad: From North Carolina to the UK", "2026-10-27", "Student Center, Room 385", "Office of International Affairs", "Global and International", "Dr. Tiffany Holloman shares her journey from N.C. A&T to an international career in the UK.", A930),
("2026 N.C. A&T Honors College Research Conference", "2026-11-05", "Deese Ballroom, Student Center", "Office of Honors Research", "Research and Library", "Conference for students to showcase research, internships, service projects and study abroad experiences.", A930),
# ---- Sept. 23, 2026 edition
("Let's Talk About It: Animal Care and Use Across Campus", "2026-09-23", "Fort IRC Room 410", "Office of Research Compliance and Ethics", "Agriculture", "Conversation exploring animal use across campus and university policies and reporting procedures.", A923),
("Truman Scholarship Information Session", "2026-09-23", "Zoom", "Office of Honors Research", "Scholarships and Money", "Introduction to the Truman Scholarship, a graduate fellowship providing $30,000 for future public service leaders, featuring N.C. A&T's first Truman Scholar.", A923),
("Data Management Planning for Researchers", "2026-09-24", "Virtual", "F.D. Bluford Library", "Research and Library", "Workshop covering the basics of comprehensive data management planning, including storage of and global access to your data, for research grant applicants.", A923),
("Code It, Watch It Go: Edison Robotics Fun", "2026-09-24", "Proctor Hall 314, STEAM Lab", "College of Education STEAM Lab", "Technology and Engineering", "Hands-on event for families with children ages 3 to 12 that introduces learners to robotics through robot programming, obstacle courses and design challenges using Edison Robots.", A923),
("College of Education Aggies Innovate Expo: Driving Innovation", "2026-09-25", "Proctor Hall, 1st Floor", "College of Education", "Technology and Engineering", "Event exploring innovation in teaching, learning and research through Apple technology.", A923),
("Faculty Technical Speaker Series: Quantum Computing", "2026-09-29", "Frye Hall 107", "Office of Honors Research", "Technology and Engineering", "Dr. Raymond Samuel presents on quantum computing and its applications in solving complex computational challenges.", A923),
# ---- Sept. 9, 2026 edition
("Honors Without Borders: From Petra to the Metaverse", "2026-09-10", "Virtual", "Office of Honors Research", "Global and International", "Explore the country of Jordan's unique culture, rich history, cuisine and human centered technological future.", A909),
("COAACH Lunch and Learn: Questions to Ask Your Doctor", "2026-09-11", "2105 Yanceyville St., Greensboro", "COAACH", "Health", "Learn how to ask important questions about diagnosis, treatment, medications, tests and follow-up care.", A909),
("2026 COAACH Annual Brain Health Conference", "2026-09-12", "Alumni-Foundation Event Center", "Center for Outreach in Alzheimer's, Aging and Community Health", "Health", "A New Era of Brain Health: advancing brain health through prevention, early action and innovation, featuring nationally recognized experts and free health screenings.", A909),
("NSF Graduate Research Fellowship Informational Session", "2026-09-14", "Zoom", "Office of Honors Research", "Scholarships and Money", "Learn about the NSF GRFP benefits including a $37,000 annual stipend and a $16,000 cost-of-education allowance.", A909),
("Literature Review Workshop", "2026-09-15", "Online", "F.D. Bluford Library", "Research and Library", "Discuss strategies for conducting a literature review and explore library services for finding research information.", A909),
("Meet Me for Tea: Mingle with Division of Research Staff", "2026-09-15", "Fort IRC Room 410", "Division of Research", "Faculty and Staff", "Short presentations by campus leaders followed by an informal meet and mingle with division team members.", A909),
("From Idea to Submission: Navigating InfoEd with Ease", "2026-09-16", "Fort IRC Room 410", "Office of Sponsored Programs", "Faculty and Staff", "Hands-on training on proposal development and the routing process in InfoEd for sponsored projects.", A909),
("Revising Your Proposal: Strategies for Resubmission", "2026-09-16", "Zoom", "Division of Research", "Faculty and Staff", "Practical guidance for applicants preparing to revise and resubmit to a grant solicitation.", A909),
("Fall 2026 Career Fair", "2026-09-16", "Special Event Center, Greensboro Coliseum Complex", "Career Services", "Career and Professional", "Connect and network with employers for internships, co-ops and full-time career opportunities.", CAL + "2026/05/fall-2026-career-fair.php"),
("Travel Service Training: Emburse Mobile Access", "2026-09-17", "Zoom", "Department of Travel Services", "Faculty and Staff", "Training session on mobile access for travel expense reconciliation.", A909),
("Travel Service Training: Student Travel and Cash Advance", "2026-09-17", "Zoom", "Department of Travel Services", "Faculty and Staff", "Training on student travel procedures and cash advance processes.", A909),
("Money Skills 101: Budgeting and Saving for Success", "2026-09-17", "Virtual", "Extended Campus and JPMorgan Chase", "Scholarships and Money", "Interactive webinar covering budget creation, financial goals, saving habits and expense management.", A909),
("Constitution Day 2026", "2026-09-17", "General Classroom Building 218", "Departments of History and Political Science", "Culture and Social Justice", "Discussions and activities will explore our relationship with the U.S. Constitution.", A909),
("Using Covidence for Systematic and Scoping Reviews", "2026-09-17", "Online", "F.D. Bluford Library", "Research and Library", "Workshop on using the cloud-based Covidence tool for review projects including screening and data abstraction.", A909),
("North Carolina Folk Festival", "2026-09-18", "Downtown Greensboro", "NC Folk Festival", "Arts and Performance", "Free three day music and cultural festival celebrating traditions and stories through live performance, food and art.", A909),
("North Carolina FIRST LEGO League Kickoff", "2026-09-19", "Frye Hall", "College of Engineering", "Technology and Engineering", "Kickoff event for students in grades 4 to 8 to develop creativity, confidence, teamwork and problem-solving through robotics.", A909),
("Digital/E-Portfolios Workshop", "2026-09-22", "Online", "F.D. Bluford Library", "Research and Library", "Overview of e-portfolio types and their use in classroom settings with a focus on the Wix platform.", A909),
("Chi Sigma Iota Spirit Night Fundraiser", "2026-09-22", "Chick-fil-A, 611 Pembroke Road", "Chi Sigma Iota", "Homecoming and Student Life", "Spirit night fundraiser to support graduate counseling students.", A909),
# ---- University calendar (ncat.edu/calendar)
("Graduation Breakfast and Rehearsal", "2026-12-10", "Alumni-Foundation Event Center", "N.C. A&T", "Graduation", "Graduates celebrating their achievements with N.C. A&T administrators, faculty, staff and fellow graduates.", CAL + "2026/12/graduation-breakfast-rehearsal.php"),
("Commencement Fair", "2026-09-14", "", "N.C. A&T", "Graduation", "One-stop shop for commencement attire, cap and gown, regalia, class rings, announcements and more.", CAL + "2026/09/commencement-fair-sept-14.php"),
("Run the World 5K Fundraiser, Department of Counseling", "2026-08-29", "", "Department of Counseling", "Sports and Fitness", "", CAL + "2026/08/run-the-world-5k-fundraiser-department-of-counseling.php"),
("Transdisciplinary Experiential Learning in Food Animal Production Workshop", "2026-08-17", "", "N.C. A&T", "Agriculture", "", CAL + "2026/08/transdisciplinary-experiential-learning-in-food-animal-production-workshop.php"),
("Faculty/Staff Institute 2026", "2026-08-14", "", "N.C. A&T", "Faculty and Staff", "", CAL + "2026/08/faculty-staff-institute-2026.php"),
]

# ---- Athletics home games (schedule rows turned into one plain sentence each)
for opp, d in [("Morgan State University", "2026-08-29"), ("University of Rhode Island", "2026-09-26"),
               ("University of New Hampshire", "2026-10-10"), ("Chicago State University", "2026-10-17"),
               ("Elon University", "2026-10-31"), ("University at Albany", "2026-11-21")]:
    R.append((f"Aggie Football vs. {opp}", d, "Truist Stadium", "N.C. A&T Athletics", "Sports and Fitness",
              f"N.C. A&T Aggies football home game against {opp} at Truist Stadium.", FB))
for opp, d, gym in [("North Carolina Central University", "2026-09-10", "Corbett Sports Center"),
                    ("UNC Greensboro", "2026-09-11", "Corbett Sports Center"),
                    ("Davidson College", "2026-09-12", "Corbett Sports Center"),
                    ("Wake Forest University", "2026-09-17", "Moore Gymnasium"),
                    ("College of Charleston", "2026-10-02", "Moore Gymnasium"),
                    ("UNC Wilmington", "2026-10-16", "Moore Gymnasium"),
                    ("Towson University", "2026-10-29", "Moore Gymnasium"),
                    ("Elon University", "2026-11-06", "Moore Gymnasium")]:
    R.append((f"Aggie Volleyball vs. {opp}", d, gym, "N.C. A&T Athletics", "Sports and Fitness",
              f"N.C. A&T Aggies women's volleyball home match against {opp} at {gym}.", VB))

# ---- Student homecoming schedule page (these are the 2025 events still posted on the page)
R += [
("Coronation of Mister and Miss A&T", "2025-10-05", "Corbett Sports Center", "Office of Student Activities", "Homecoming and Student Life", "Homecoming coronation ceremony. Formal or semi-formal attire. Open to the public.", HC),
("Homecoming Fall Festival", "2025-10-06", "Truist Stadium Parking Lot", "Office of Student Activities", "Homecoming and Student Life", "Free homecoming festival for A&T students only.", HC),
("Aggie Reunion and Jersey Giveaway", "2025-10-07", "Village Quad", "Office of Student Activities", "Homecoming and Student Life", "Homecoming reunion and jersey giveaway on the quad.", HC),
("Homecoming Fashion Show", "2025-10-07", "Corbett Sports Center", "Office of Student Activities", "Arts and Performance", "Student homecoming fashion show. Ticketed event.", HC),
("Community and Economic Engagement Summit", "2025-10-08", "Elm and Bain, Greensboro", "Strategic Partnerships and Economic Development", "Culture and Social Justice", "Legacy in Motion: Fueling Wealth, Innovation and Transformational Impact. Summit with featured alumni speakers.", HC),
("Homecoming Pep Rally", "2025-10-08", "Corbett Sports Center", "Office of Student Activities", "Homecoming and Student Life", "Free homecoming pep rally for A&T students only.", HC),
("Fall Convocation", "2025-10-09", "Harrison Auditorium", "N.C. A&T", "Homecoming and Student Life", "Campus-wide fall convocation.", HC),
("N.C. A&T Homecoming Step Show", "2025-10-10", "First Horizon Coliseum", "Office of Student Activities", "Arts and Performance", "Homecoming step show. Tickets for current students through ncataggies.com.", HC),
("Greek Plots", "2025-10-11", "Williams Dining Hall Parking Lot", "Office of Student Activities", "Homecoming and Student Life", "Fraternity and sorority plots gathering on homecoming Saturday.", HC),
("Homecoming Parade", "2025-10-11", "Lindsay Street", "Office of Student Activities", "Homecoming and Student Life", "Annual homecoming parade.", HC),
("Aggie Homecoming Hip Hop Concert", "2025-10-11", "First Horizon Coliseum", "Office of Student Activities", "Arts and Performance", "Homecoming hip hop concert with GloRilla, PartyNextDoor, Queen Naija, Fridayy and Big Boogie.", HC),
("N.C. A&T Homecoming Gospel Concert", "2025-10-12", "Steven Tanger Center for the Performing Arts", "Office of Student Activities", "Arts and Performance", "Gospel concert with Fred Hammond, The Clark Sisters and the N.C. A&T Fellowship Gospel Choir.", HC),
]

with open("aggieconnect_events.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["event_id", "title", "date", "location", "organization", "category", "description", "source_url"])
    for i, r in enumerate(R, 1):
        w.writerow([f"E{i:02d}", *r])
print(len(R), "events written")
