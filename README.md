# ⚡ Trend Predator: AI-Powered Viral Content Engine

## 🌐 Live Demo
**[https://trendpredictor.streamlit.app/](https://trendpredictor.streamlit.app/)**

## 🚀 Project Overview

**Trend Predator** is a real-time intelligence tool designed for content creators, marketers, and social media managers. It automates the entire workflow of finding viral topics and creating engaging scripts.

In simple terms: **It finds what's hot and writes your next viral Reel for you.**

### ✨ Key Features
* **🕵️ Real-Time Trend Scanning:** Fetches the top trending topics live from Google News India across multiple niches (Tech, Sports, Entertainment, etc.).
* **🧠 AI Script Generation:** Uses **Google's Gemini 2.0 Flash** AI model to instantly generate viral-worthy 30-second Reel scripts (Hook, Value, Call-to-Action) in Hinglish.
* **🔒 Secure Admin Login:** Protected by a password authentication system to prevent unauthorized access.
* **🗄️ Persistent Database:** Stores trending data in a local SQLite database, building a historical record of what went viral.
* **🎨 Modern Dark UI:** A sleek, professional, "Cyberpunk" styled interface built with Streamlit for a premium user experience.

---

## 🛠️ Tech Stack

This project is a full-stack Python application built with modern libraries.

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend & Backend** | [Streamlit](https://streamlit.io/) | The core framework for building the web app, UI, and handling logic. |
| **AI Model** | [Google Gemini API](https://ai.google.dev/) | Powers the intelligent script generation capability. |
| **Data Scraping** | `requests` & `xml.etree` | Fetches and parses real-time RSS feeds from Google News. |
| **Database** | SQLite3 | A lightweight, file-based database to store trend history. |
| **Deployment** | Streamlit Community Cloud | Hosts the live application directly from GitHub. |

---

## ⚙️ How It Works (Architecture)

1.  **User Login:** The user authenticates via a secure password screen.
2.  **Niche Selection:** The user selects a category (e.g., "Tech") from the dashboard.
3.  **Data Scraping:** The `scraper.py` module hits Google News RSS feeds using custom headers to mimic a real browser and fetches the latest headlines.
4.  **Data Storage:** The fetched topics are instantly saved into the SQLite database (`trends.db`) via `db_manager.py`.
5.  **Dashboard Update:** The Streamlit app reads the latest data from the DB and displays it as elegant cards.
6.  **AI Magic:** When the user clicks "Generate Script", the topic is sent to `ai_agent.py`, which prompts the Gemini AI to write a tailored script, which is then displayed on the UI.

---

## 🖥️ Installation & Local Run

Follow these steps to run the project on your local machine.

### Prerequisites
* Python 3.8 or higher installed.
* A Google Cloud account with a **Gemini API Key**.

### Steps

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/trend-predator.git](https://github.com/YOUR_USERNAME/trend-predator.git)
    cd trend-predator
    ```

2.  **Create & Activate Virtual Environment (Optional but recommended)**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Secrets (API Key & Password)**
    Create a new folder named `.streamlit` in the root directory and inside it, create a file named `secrets.toml`. Add your credentials:

    **`.streamlit/secrets.toml`**
    ```toml
    GEMINI_API_KEY = "YOUR_ACTUAL_GEMINI_API_KEY_HERE"
    ADMIN_PASSWORD = "Set_Your_Desired_Password_Here"
    ```

5.  **Run the App**
    ```bash
    streamlit run app.py
    ```
    The app should now open in your browser at `http://localhost:8501`. Use the password you set in `secrets.toml` to log in.

---

## 📁 Project Structure
