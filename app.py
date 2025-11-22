import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Gemini Text Summarizer",
    page_icon="📝",
    layout="centered"
)

# --- Sidebar Settings ---
with st.sidebar:
    st.header("Settings")
    st.markdown("Configure the summarization parameters.")
    
    # Slider for summary length (approximate token count or descriptive)
    summary_length = st.select_slider(
        "Summary Length",
        options=["Short", "Medium", "Long"],
        value="Medium"
    )
    
    # Slider for creativity (Temperature)
    temperature = st.slider(
        "Creativity (Temperature)",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Higher values mean more creative/random output. Lower values mean more deterministic output."
    )
    
    st.markdown("---")
    st.markdown("Powered by **Gemini 2.5 Flash**")

# --- Main Content ---
st.title("📝 AI Text Summarizer")
st.markdown("Paste your text below to get a concise summary using Google's Gemini 2.5 Flash model.")

# Text Input
text_input = st.text_area("Enter text to summarize:", height=200, placeholder="Paste your article, report, or notes here...")

# API Key Validation
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("⚠️ API Key not found! Please set `GEMINI_API_KEY` in your `.env` file.")
    st.stop()

# Initialize Gemini Client
# We use the updated google-genai SDK
try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"Failed to initialize Gemini Client: {e}")
    st.stop()

def get_summary(text, length_preference, temp):
    """
    Sends text to Gemini 2.5 Flash for summarization.
    """
    try:
        # Construct a prompt based on settings
        length_prompt = ""
        if length_preference == "Short":
            length_prompt = "Keep the summary very concise, around 2-3 sentences."
        elif length_preference == "Medium":
            length_prompt = "Provide a standard summary, capturing key points in a few paragraphs."
        else: # Long
            length_prompt = "Provide a detailed summary, covering all main sections and nuances."

        prompt = f"""
        Please summarize the following text.
        {length_prompt}
        
        Text:
        {text}
        """

        # Call the API
        # Using the specific model: gemini-2.5-flash
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=temp
            )
        )
        
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Summarize Button
if st.button("Summarize", type="primary"):
    if not text_input.strip():
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Generating summary..."):
            summary = get_summary(text_input, summary_length, temperature)
            
            if summary.startswith("Error:"):
                st.error(summary)
            else:
                st.success("Summary Generated!")
                st.markdown("### Summary")
                st.markdown(summary)
