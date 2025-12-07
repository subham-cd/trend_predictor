import google.generativeai as genai
import streamlit as st
import time
import os

def get_api_key():
    """
    Ye function API Key dhoondhne ki koshish karega.
    Pehle Cloud Secrets mein, phir Local Secrets mein.
    """
    try:
        # Step 1: Streamlit Secrets check karo (Cloud & Local)
        return st.secrets["GEMINI_API_KEY"]
    except Exception:
        # Step 2: Agar Secrets nahi mile, toh Environment Variable check karo
        return os.getenv("GEMINI_API_KEY")

def generate_script(topic):
    # 1. API Key fetch karo secure tarike se
    api_key = get_api_key()
    
    if not api_key:
        return "Error: API Key missing! Please add GEMINI_API_KEY to secrets.toml"

    try:
        # 2. Configure Gemini
        genai.configure(api_key=api_key)
        
        # Tumhara select kiya hua Model
        model = genai.GenerativeModel('gemini-2.0-flash-exp') 
        
        prompt = f"""
        Act as a famous Indian Tech Influencer.
        Topic: {topic}
        
        Write a viral 30-second Reel script in Hinglish.
        Structure:
        - Hook (0-3s): Catchy line.
        - Explanation (3-20s): Simple explanation.
        - CTA (20-30s): "Follow for more."
        """
        
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        # Agar quota error aaye toh retry logic
        if "429" in str(e):
            time.sleep(2)
            return "Server busy (Rate Limit), trying again... Please wait."
        return f"AI Error: {str(e)}"

if __name__ == "__main__":
    # Local testing ke liye warning
    print("Testing AI Agent...")
    print(generate_script("Virat Kohli"))