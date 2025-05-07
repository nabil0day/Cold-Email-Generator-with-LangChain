# Email Generator

This is a simple web app that helps students and researchers generate professional academic emails to professors using AI.

## How to Use

1. **Clone the repository and install dependencies:**
   ```bash
   git clone https://github.com/nabil0day/Cold-Email-Generator-with-LangChain.git
   cd academic-email-generator
   pip install -r requirements.txt
   ```

2. **Add your Groq API key:**
   Create a file named `constants.py` and add:

   ```python
   groq_api_key = "your-groq-api-key-here"
   ```

3. **Run the Streamlit app:**

   ```bash
   streamlit run main.py
   ```

4. **Fill in the form:**

   * Enter detailed info, your background, and purpose
   * Click **"Generate Personalized Email"**
   * Copy or send the email directly
