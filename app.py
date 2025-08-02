import streamlit as st
from resume_generator import generate_resume_docx
from docx import Document
from io import BytesIO

st.set_page_config(page_title="TailorCV – AI Resume & Cover Letter Coach", layout="centered")
st.title("🧵 TailorCV – Build Smarter Resumes & Cover Letters")

option = st.radio("Choose what you want to do:", 
    ["📤 Upload & Improve Resume", 
     "🧱 Build Resume from Scratch",
     "✍️ Generate a Cover Letter"])

# ------------------ Upload Resume (Placeholder) ------------------
if option == "📤 Upload & Improve Resume":
    uploaded_file = st.file_uploader("Upload your resume (.docx or .pdf)", type=["docx", "pdf"])
    jd_text = st.text_area("Paste the Job Description here")

    if uploaded_file and jd_text:
        st.success("Resume and JD uploaded successfully!")

        if st.button("Analyze Resume"):
            st.write("🧠 AI Feedback coming soon...")
            st.write("✍️ Cover Letter generation coming soon...")

# ------------------ Build Resume from Scratch ------------------
elif option == "🧱 Build Resume from Scratch":
    st.subheader("🔹 Contact Info")

    demo_mode = st.checkbox("🧪 Use demo/test data")

    if demo_mode:
        name = "Pratiksha Raturi"
        phone = "9876543210"
        email = "pratiksha.raturi@example.com"
        linkedin = "https://linkedin.com/in/pratiksha-raturi"
        github = "https://github.com/pratiksha-raturi"
        summary = "Final-year B.Tech student in Computer Science with hands-on experience in AI solutions. Built TailorCV and Credit Risk Predictor."
        education = "B.Tech in CSE – UPES – 2021–2025 – 8.3 CGPA\nXII – DPS – 92%\nX – DPS – 94%"
        experience = "AI Intern | RANGR Data | May–Aug 2024\n• Built LLM dashboard with Foundry\n• Created credit scoring pipelines"
        projects = "TailorCV – GPT Resume App\nCredit Risk Predictor – Bayesian ML model"
        skills = "Python, Streamlit, Pandas, Git, Power BI"
        certifications = "IBM GenAI – June 2025\nGoogle DA – April 2025"
        submitted = True
    else:
        with st.form("resume_form"):
            name = st.text_input("Full Name")
            phone = st.text_input("Phone")
            email = st.text_input("Email")
            linkedin = st.text_input("LinkedIn URL")
            github = st.text_input("GitHub URL")
            summary = st.text_area("Professional Summary")
            education = st.text_area("Education")
            experience = st.text_area("Work Experience")
            projects = st.text_area("Projects (Optional)")
            skills = st.text_area("Skills")
            certifications = st.text_area("Certifications (Optional)")
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
        st.download_button("📥 Download Resume (.docx)", data=docx_file, file_name=f"{name.replace(' ', '_')}_Resume.docx")

# ------------------ Generate Cover Letter ------------------
elif option == "✍️ Generate a Cover Letter":
    st.subheader("✍️ Cover Letter Generator")

    demo_mode = st.checkbox("🧪 Use demo/test data")

    if demo_mode:
        your_name = "Pratiksha Raturi"
        your_institution = "UPES Dehradun"
        your_position = "Data Analyst Intern"
        company = "Zomato"
        experience_summary = "Internships exposed me to LLM integrations, pipelines, and resume building projects."
        resume_summary = "Python, ML, Streamlit, Resume AI, Credit Risk modeling"
        best_internship = "AI Intern at RANGR Data using OpenAI + Foundry"
        how_will_help = "Will expand my analytics and visualization depth, aligned with my career goals."
        soft_skills = "Strong communication, empathy-based problem solving, and team-first mindset."
        submitted = True
    else:
        with st.form("cover_form"):
            your_name = st.text_input("Your Name")
            your_institution = st.text_input("College/University")
            your_position = st.text_input("Position You're Applying For")
            company = st.text_input("Company Name")
            experience_summary = st.text_area("Short Summary of Past Experience")
            resume_summary = st.text_area("Resume Summary Highlights")
            best_internship = st.text_area("Your Best Internship")
            how_will_help = st.text_area("How This Opportunity Will Help You")
            soft_skills = st.text_area("Mention Your Soft Skills or Work Style")
            submitted = st.form_submit_button("Generate Cover Letter")

    if submitted:
        doc = Document()
        doc.add_paragraph(your_name)
        doc.add_paragraph(your_institution)
        doc.add_paragraph("Complete Address | Contact Info")
        doc.add_paragraph("")
        doc.add_paragraph("Dear Selection Committee,")

        body = (
            f"I am writing today in application for the position of {your_position} at {company}, India. "
            f"{experience_summary} "
            f"My attached resume outlines {resume_summary}. "
            f"{how_will_help} "
            f"{soft_skills} "
            f"\n\nSincerely,\n{your_name}"
        )
        doc.add_paragraph(body)

        buffer = BytesIO()
        doc.save(buffer)
        buffer.seek(0)

        st.success("✅ Cover Letter generated successfully!")
        st.download_button("📄 Download Cover Letter (.docx)", data=buffer, file_name=f"{your_name.replace(' ', '_')}_CoverLetter.docx")
