import streamlit as st
import google.generativeai as genai

# Preset API key
API_KEY = "AIzaSyD5KahUkm_sd7WI64t18j-7zn8UVCcExoE"

# Configure and create the Gemini model
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Function to load the prompt from a file
def load_prompt(file_path='prompt.txt'):
    with open(file_path, 'r') as f:
        prompt = f.read()
    return prompt

# Function to get the report from the Gemini model
def get_report_from_gemini(file_content):
    prompt = load_prompt()
    report = model.generate_content(f"""{prompt}\n{file_content}""")
    buffer = ""
    for part in report.parts:
        buffer += part.text
    return buffer

# Streamlit app layout
def main():
    st.title("News Article Analysis with Gemini Model")
    file_content = st.text_area("Enter the news article content:", height=150)
    
    if st.button("Analyze Article"):
        if file_content:
            report = get_report_from_gemini(file_content)
            st.subheader("Analysis Report:")
            st.write(report)
        else:
            st.warning("Please enter some content for the analysis.")

if __name__ == "__main__":
    main()
