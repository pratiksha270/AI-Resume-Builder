import streamlit as st
from resume_generator import generate_resume_docx

st.set_page_config(page_title="RésuMe – AI Resume Coach", layout="centered")
st.title("📝 RésuMe – Your AI Resume & Cover Letter Coach")

option = st.radio("Choose what you want to do:", 
                  ["📤 Upload & Improve Resume", "🧱 Build Resume from Scratch"])

if option == "📤 Upload & Improve Resume":
    uploaded_file = st.file_uploader("Upload your resume (.docx or .pdf)", type=["docx", "pdf"])
    jd_text = st.text_area("Paste the Job Description here")

    if uploaded_file and jd_text:
        st.success("Resume and JD uploaded successfully!")

        if st.button("Analyze Resume"):
            st.write("🧠 AI Feedback coming soon...")  # Placeholder
            st.write("✍️ Cover Letter generation coming soon...")

elif option == "🧱 Build Resume from Scratch":
    st.subheader("🧱 Resume Builder Form")
    with st.form("resume_form"):
        name = st.text_input("Full Name")
        phone = st.text_input("Phone")
        email = st.text_input("Email")
        linkedin = st.text_input("LinkedIn")
        github = st.text_input("GitHub")

        summary = st.text_area("Professional Summary")
        education = st.text_area("Education")
        experience = st.text_area("Work Experience / Projects")
        skills = st.text_area("Skills (comma-separated)")
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
            'skills': skills,
            'certifications': certifications
        }

        docx_file = generate_resume_docx(data)
        st.success("✅ Resume generated successfully!")

        st.download_button("📥 Download Your Resume (.docx)", 
                           data=docx_file, 
                           file_name=f"{name.replace(' ', '_')}_Resume.docx")
