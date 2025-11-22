# Gemini Text Summarizer

A simple yet powerful text summarization application built with [Streamlit](https://streamlit.io/) and Google's [Gemini 2.5 Flash](https://deepmind.google/technologies/gemini/) model.


## Demo


[![Watch the Demo](assets/thumbnail.png)](https://github.com/Dinu-Sreekumar/Text-summarizer/blob/main/assets/demo.mp4)


## Features

- **Text Summarization**: Paste any text to get a concise summary.
- **Customizable Settings**: Adjust summary length (Short, Medium, Long) and creativity (Temperature).
- **Modern UI**: Clean and responsive interface.

## Prerequisites
- Python 3.8 or higher
- A Google Cloud Project with the Gemini API enabled (or an API key from Google AI Studio).

## Installation

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repository-url>
   cd "Text Summarizer"
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

⚠️ **IMPORTANT**: You must configure your API key for the application to work.

1. Create a file named `.env` in the root directory of the project.
2. Add the following line to the file, replacing `YOUR_API_KEY_HERE` with your actual Gemini API key:

   ```env
   GEMINI_API_KEY=YOUR_API_KEY_HERE
   ```

   > **Note**: Do not share your `.env` file or commit it to version control.

## Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

The app will open in your default web browser. Paste your text, adjust the settings if needed, and click **Summarize**!
