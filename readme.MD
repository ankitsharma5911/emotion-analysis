# 😄 Mood Tracker App

The Mood Tracker is a Streamlit-based web application that allows users to describe how they're feeling in natural language and get AI-generated insights about their mood, mood intensity (on a scale from 1 to 10), and personalized suggestions to improve their emotional well-being.

---

## 🚀 Live Demo

👉 [Click here to use the live app](https://your-live-app-link.com)  
*(Replace with your actual Streamlit or deployment URL)*

---

## 🧠 Powered By

- **LangChain** with Google Gemini 2.5 Pro (`ChatGoogleGenerativeAI`)
- **Pydantic** for structured outputs
- **Streamlit** for interactive UI

---

## ✨ Features

- Enter how you're feeling in your own words.
- Detects:
  - **Mood** (e.g., happy, sad, angry)
  - **Intensity** (on a scale from 1 to 10)
  - **Suggestions** (personalized activities and advice)
- User-friendly chat interface.

---

## 🛠️ Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ankitsharma5911/emotion-analysis.git
    cd emotion-analysis
    ```
    
2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file and add your Google Generative AI key:
    ```env
    GOOGLE_API_KEY=your_google_api_key
    ```

5. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

---

## 📂 Project Structure

