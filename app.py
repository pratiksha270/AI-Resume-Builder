import streamlit as st
from resume_generator import generate_resume_docx

st.set_page_config(page_title="RésuMe – AI Resume & Cover Letter Coach", layout="centered")
st.title("📝 RésuMe – Your AI Resume & Cover Letter Coach")

option = st.radio("Choose what you want to do:", 
    ["📤 Upload & Improve Resume", 
     "🧱 Build Resume from Scratch",
     "✍️ Generate a Cover Letter"])

# ------------------ Option 1: Upload Resume + JD ------------------
if option == "📤 Upload & Improve Resume":
    uploaded_file = st.file_uploader("Upload your resume (.docx or .pdf)", type=["docx", "pdf"])
    jd_text = st.text_area("Paste the Job Description here")

    if uploaded_file and jd_text:
        st.success("Resume and JD uploaded successfully!")

        if st.button("Analyze Resume"):
            st.write("🧠 AI Feedback coming soon...")
            st.write("✍️ Cover Letter generation coming soon...")

# ------------------ Option 2: Build Resume from Scratch ------------------
elif option == "🧱 Build Resume from Scratch":
    st.subheader("🔹 Contact Info")
    with st.form("resume_form"):
        name = st.text_input("Full Name")
        phone = st.text_input("Phone")
        email = st.text_input("Email")
        linkedin = st.text_input("LinkedIn URL", placeholder="https://www.linkedin.com/in/your-name")
        github = st.text_input("GitHub URL", placeholder="https://github.com/your-username")

        st.subheader("🔹 Professional Summary")
        summary = st.text_area(
            "Write a short summary about yourself",
            placeholder="E.g., A final-year B.Tech student with experience in building AI tools like RésuMe and Credit Risk models...",
            help="Summarize your most notable achievements, experiences, and skills. Keep it concise and impactful."
        )

        st.subheader("🔹 Education")
        education = st.text_area(
            "List your degrees and details",
            placeholder="E.g., B.Tech in Computer Science – UPES Dehradun – 2021–2025 – 8.1 CGPA",
            help="Include degree, institution, year, and GPA or board. List in reverse chronological order if needed."
        )

        st.subheader("🔹 Work Experience")
        experience = st.text_area(
            "Mention your work or internship experience",
            placeholder="E.g.,\nCompany Name | Position Title | March 2022 – Jan 2024\n• Built resume analyzer using OpenAI GPT\n• Improved project performance by 30%",
            help="Focus on achievements and responsibilities. Use action verbs and metrics wherever possible."
        )

        st.subheader("🔹 Projects (Optional)")
        projects = st.text_area(
            "Include personal or academic projects",
            placeholder="E.g.,\nProject Title | Role | Dates\n• Built AI-powered resume builder using Streamlit and GPT\n• Applied CNN model for landslide detection",
            help="Add this if you don't have work experience or to showcase personal achievements."
        )

        st.subheader("🔹 Skills")
        skills = st.text_area(
            "Add your key skills",
            placeholder="E.g., Python, Pandas, scikit-learn, Streamlit, SQL, Power BI",
            help="Use commas to separate technical or soft skills. Match your target job profile."
        )

        st.subheader("🔹 Certifications (Optional)")
        certifications = st.text_area(
            "Include relevant certifications",
            placeholder="E.g., AWS Certified Cloud Practitioner – July 2024",
            help="Only include certifications relevant to the role you’re applying for."
        )

        submitted = st.form_submit_button("✅ Generate Resume")

    if submitted:
        data = {
            'name': name,
            'phone': phone,
            'email': email,
            'linkedin': linkedin,
            'github': github,
            'summary': summary,
            'education': education,
            'experience': experience,
            'projects': projects,
            'skills': skills,
            'certifications': certifications
        }

        docx_file = generate_resume_docx(data)
        st.success("✅ Resume generated successfully!")
        st.download_button("📥 Download Your Resume (.docx)", data=docx_file, file_name=f"{name.replace(' ', '_')}_Resume.docx")

# ------------------ Option 3: Generate Cover Letter ------------------
elif option == "✍️ Generate a Cover Letter":
    st.subheader("✍️ Cover Letter Generator")
    st.markdown("Fill in the following fields. Your cover letter will be auto-generated in the format you shared.")

    with st.form("cover_form"):
        your_name = st.text_input("Your Name")
        your_institution = st.text_input("College/University")
        your_position = st.text_input("Position You're Applying For")
        company = st.text_input("Company Name")
        experience_summary = st.text_area("Short Summary of Past Experience")
        resume_summary = st.text_area("Resume Summary Highlights (skills, strengths)")
        best_internship = st.text_area("Your Best Internship (short 1-2 lines)")
        how_will_help = st.text_area("How This Opportunity Will Help You")
        soft_skills = st.text_area("Mention Your Soft Skills or Work Style")
        submitted = st.form_submit_button("Generate Cover Letter")

    if submitted:
        st.success("✅ Cover Letter Generated!")
        st.markdown(f"""
**{your_name}**  
{your_institution}  
Complete Address | Contact Info  

---

**Dear Selection Committee,**

**Purpose:**  
I am writing today in application for the position of **{your_position}** at **{company}**, India. I am confident that exposure to community building, content creation, and research methodologies have endowed me with the abilities and skills that will be an asset to the organization. Furthermore, my professional experiences in the past have sharpened my abilities to contextualize problems and look at them from an overarching perspective. {experience_summary}

As my attached resume outlines, {resume_summary} I wish to intensify my knowledge in analysis methodologies which I can through this position as I want to follow the same path in my lifelong professional trajectory. As a part of my studies, I have inculcated both qualitative and quantitative skills. The practical aspect of the course has exposed me to rich numerical analysis and has given me the ability to contextualize issues using numbers and surveys. The multidisciplinary courses have opened me up to systems thinking and enabled me to view challenges from a holistic perspective – data analytics, ethical marketing, collaboration, and more. I believe such understanding is critical to work at **{company}**, since the organization has projects across varied AI concepts.

Apart from the engaging academic rigor, my summer internship at {best_internship} gave me hands-on market research and strategic programs experience, where I was engaged in benchmarking and analysis.

{how_will_help}

{soft_skills}

Your careful review of my application is deeply appreciated. Thank you for the opportunity and for considering my candidacy.

**Sincerely,**  
**{your_name}**
        """)
