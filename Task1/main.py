# main.py

import os
from constants import groq_api_key
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import streamlit as st
import urllib.parse

os.environ["GROQ_API_KEY"] = groq_api_key

# Streamlit interface with improved styling
st.set_page_config(page_title="Academic Email Generator - Coded by Hadiur Rahman Nabil", page_icon="📧", layout="wide")

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-family: 'Helvetica Neue', sans-serif;
        color: #2563EB;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-family: 'Helvetica Neue', sans-serif;
        color: #4B5563;
        text-align: center;
        margin-bottom: 30px;
        font-size: 1.2rem;
    }
    .stButton>button {
        background-color: #2563EB;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 12px 24px;
        width: 100%;
        transition: all 0.3s ease;
        border: none;
        box-shadow: 0 4px 6px rgba(37, 99, 235, 0.2);
    }
    .stButton>button:hover {
        background-color: #1D4ED8;
        box-shadow: 0 6px 8px rgba(37, 99, 235, 0.3);
        transform: translateY(-2px);
    }
    .section-header {
        font-family: 'Helvetica Neue', sans-serif;
        color: #2563EB;
        margin-top: 25px;
        margin-bottom: 15px;
        font-weight: bold;
        font-size: 1.5rem;
        border-left: 4px solid #2563EB;
        padding-left: 10px;
    }
    .stExpander {
        border: 1px solid #E5E7EB;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    .footer {
        text-align: center;
        color: #6B7280;
        font-style: italic;
        margin-top: 40px;
        padding: 20px;
        border-top: 1px solid #E5E7EB;
    }
    .card {
        background-color: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        border: 1px solid #F3F4F6;
        margin-bottom: 20px;
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 8px;
        border: 1px solid #D1D5DB;
        padding: 10px;
    }
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: #2563EB;
        box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2);
    }
    .email-button {
        display: inline-block;
        text-align: center;
        padding: 15px;
        background-color: white;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
        margin: 10px;
        transition: all 0.3s ease;
        text-decoration: none;
        color: #2563EB;
        border: 1px solid #E5E7EB;
    }
    .email-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.12);
    }
    .stAlert {
        background-color: #EFF6FF;
        border-left: 4px solid #2563EB;
        padding: 10px 15px;
        border-radius: 8px;
    }
    body {
        background-color: #F9FAFB;
    }
    .subsection-header {
        color: #2563EB;
        margin-bottom: 15px;
        margin-top: 20px;
        font-weight: 600;
        font-size: 1.2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Header with logo and improved styling
st.markdown('<div style="padding: 20px 0; background-color: white; border-radius: 12px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08); margin-bottom: 30px;">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<h1 class="main-header">✉️ Academic Email Generator</h1>', unsafe_allow_html=True)
    st.markdown('<h3 class="sub-header">Coded by Hadiur Rahman Nabil</h3>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Create a structured prompt template for email generation
prompt_template = ChatPromptTemplate.from_template("""
You are an expert at writing professional cold emails to professors. Create a well-structured, polite, and effective email based on the following information:

Professor's Name: {professor_name}
Professor's Department/Field: {department}
Professor's Research Interests/Publications: {professor_research}
Your Name: {your_name}
Your Background: {background}
Your Resume Details: {resume_details}
Purpose of Contact: {purpose}
Specific Request/Question: {specific_request}

The email should include:
1. A professional greeting
2. Begin with "I hope you are doing well and in good health." (use this exact phrase)
3. A brief introduction of yourself that highlights relevant parts of your resume
4. Why you're contacting this specific professor (reference their specific research work)
5. Make connections between your experience/skills and the professor's research interests
6. Your specific request clearly stated
7. A polite closing
8. Your full name and contact information

Keep the tone respectful, concise, and professional. Make the email highly personalized by referencing specific details from both the professor's work and your resume.
""")

# Initialize Groq LLM with supported model
llm = ChatGroq(temperature=0.7, model_name="llama3-70b-8192")

# Create input form with fields for email generation
st.markdown('<h3 class="section-header">📝 Enter Information for Your Email</h3>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # Professor Information
    st.markdown('<h4 class="subsection-header">Professor Information</h4>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        professor_name = st.text_input("Professor's Name")
        professor_email = st.text_input("Professor's Email Address")
        department = st.text_input("Professor's Department/Field")
    with col2:
        professor_research = st.text_area("Professor's Research Interests/Publications", 
                                        placeholder="Paste relevant content from the professor's website or describe their research interests",
                                        height=120)
    
    # Applicant Information
    st.markdown('<h4 class="subsection-header">Your Information</h4>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        your_name = st.text_input("Your Name")
        background = st.text_area("Your Background (education, relevant experience)", height=80)
    with col2:
        resume_details = st.text_area("Key Points from Your Resume", 
                                     placeholder="List relevant skills, projects, publications, or experiences from your resume",
                                     height=120)
        
    # Purpose and Request
    st.markdown('<h4 class="subsection-header">Purpose & Request</h4>', unsafe_allow_html=True)
    purpose = st.text_input("Purpose of Contact (research opportunity, advice, etc.)")
    specific_request = st.text_area("Specific Request or Question", height=80)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Make the button more prominent
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    submit_button = st.button("✨ Generate Personalized Email")

# Add a spinner for better UX during loading
if submit_button and professor_name and your_name and purpose:
    with st.spinner('Crafting your personalized professional email...'):
        # Create the structured prompt with all input fields
        structured_prompt = prompt_template.format_messages(
            professor_name=professor_name,
            department=department,
            professor_research=professor_research,
            your_name=your_name,
            background=background,
            resume_details=resume_details,
            purpose=purpose,
            specific_request=specific_request
        )
        
        # Get response
        response = llm.invoke(structured_prompt)
        
        # Display in a nice format with card-like container
        st.markdown('<h3 class="section-header">📋 Your Personalized Email</h3>', unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            email_content = response.content
            st.text_area("Copy your email from here:", email_content, height=300)
            
            # Add copy button functionality with better styling
            st.markdown("<p style='text-align: center; color: #4B5563;'><i>Use Ctrl+A to select all text and Ctrl+C to copy</i></p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Add email button if professor email is provided
        if professor_email:
            email_subject = f"Inquiry from {your_name} - {purpose}"
            encoded_subject = urllib.parse.quote(email_subject)
            encoded_body = urllib.parse.quote(email_content[:1500])
            
            st.markdown('<h3 class="section-header">📤 Send Email Options</h3>', unsafe_allow_html=True)
            
            with st.container():
                st.markdown('<div class="card">', unsafe_allow_html=True)
                col1, col2 = st.columns(2)
                with col1:
                    gmail_link = f"https://mail.google.com/mail/?view=cm&fs=1&to={professor_email}&su={encoded_subject}&body={encoded_body}"
                    st.markdown(f"""
                    <a href='{gmail_link}' target='_blank' class="email-button" style="display: block;">
                        <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Gmail_icon_%282020%29.svg/512px-Gmail_icon_%282020%29.svg.png' width='50'>
                        <p style="margin-top: 10px; font-weight: bold;">Open in Gmail</p>
                        <p style="font-size: 0.8rem; color: #6B7280;">Uses Gmail web interface</p>
                    </a>
                    """, unsafe_allow_html=True)
                with col2:
                    mailto_link = f"mailto:{professor_email}?subject={encoded_subject}&body={encoded_body}"
                    st.markdown(f"""
                    <a href='{mailto_link}' class="email-button" style="display: block;">
                        <img src='https://cdn-icons-png.flaticon.com/512/561/561127.png' width='50'>
                        <p style="margin-top: 10px; font-weight: bold;">Open in Default Email App</p>
                        <p style="font-size: 0.8rem; color: #6B7280;">Uses your system's email client</p>
                    </a>
                    """, unsafe_allow_html=True)
                
                st.markdown("""
                <div style="background-color: #EFF6FF; padding: 15px; border-radius: 8px; margin-top: 20px; border-left: 4px solid #2563EB;">
                    <p style="margin: 0; color: #1E40AF;"><strong>Note:</strong> If the full email doesn't appear in your draft, you may need to copy and paste the complete content from above.</p>
                </div>
                """, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
        
        # Add email tips
        st.markdown('<h3 class="section-header">💡 Tips for Success</h3>', unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            with st.expander("Tips for Cold Emailing Professors"):
                st.markdown("""
                - **Be concise**: Professors are busy, keep your email brief and to the point
                - **Show genuine interest**: Mention specific work or papers by the professor
                - **Proofread carefully**: Check for grammar and spelling errors
                - **Follow up respectfully**: Wait at least a week before sending a follow-up
                - **Personalize each email**: Avoid sending the same generic email to multiple professors
                - **Connect your skills to their research**: Explain how your background aligns with their work
                - **Be specific about your request**: Clearly state what you're looking for
                - **Highlight relevant experience**: Focus on skills and experiences most relevant to their research
                """)
            st.markdown('</div>', unsafe_allow_html=True)

# Add a footer with better styling
st.markdown("---")
st.markdown("""
<div class="footer">
    <p>This tool helps generate personalized professional emails to professors.</p>
    <p>Always review and further personalize before sending.</p>
    <p style="margin-top: 15px; font-size: 0.8rem;">© 2023 Hadiur Rahman Nabil</p>
</div>
""", unsafe_allow_html=True)