import streamlit as st
import scraper
import ai_agent
import db_manager
import time

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Trend Predator",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# --- NEW: HIDE STREAMLIT STYLE (Toolbar hatane ke liye) ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- 2. DARK MODE CSS (Cyberpunk Style) ---
st.markdown("""
    <style>
    /* 1. Main Dark Background */
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }

    /* 2. Text Coloring */
    h1, h2, h3, h4, h5, h6, p, label {
        color: #FAFAFA !important;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stCaption {
        color: #B0B0B0 !important;
    }

    /* 3. Metrics (Top Boxes) */
    div[data-testid="stMetric"] {
        background-color: #262730;
        border: 1px solid #333;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    div[data-testid="stMetric"] label {
        color: #A0A0A0 !important;
    }
    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        color: #FFFFFF !important;
    }

    /* 4. Card Styling */
    div[data-testid="stVerticalBlock"] > div[style*="flex-direction: column;"] > div[data-testid="stVerticalBlock"] {
        background-color: #1E1E1E;
        border: 1px solid #303030;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    }

    /* 5. Buttons (Neon Gradient) */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #6366F1 0%, #8B5CF6 100%);
        color: white !important;
        border: none;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        box-shadow: 0 0 15px rgba(99, 102, 241, 0.6);
        transform: translateY(-2px);
    }
    
    /* 6. Rank Number Styling */
    .rank-number {
        color: #444;
        font-size: 40px;
        font-weight: bold;
        text-shadow: 0 0 5px rgba(255,255,255,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. HEADER SECTION (With Niche Selection) ---
col1, col2 = st.columns([0.6, 0.4])

with col1:
    st.title("⚡ Trend Predator")
    st.markdown("<h3 style='margin-top: -20px; color: #888 !important;'>Viral Content Intelligence Engine</h3>", unsafe_allow_html=True)

with col2:
    st.write("") # Spacing
    
    # 1. Niche Selector Dropdown
    selected_category = st.selectbox(
        "🎯 Select Your Niche",
        ["General", "Tech", "Business", "Sports", "Entertainment", "Science", "Health"]
    )
    
    # 2. Scan Button (Passes the category to the scraper)
    if st.button(f"🔄 Scan {selected_category} Trends", use_container_width=True):
        with st.status(f"📡 Scanning {selected_category} Sector...", expanded=True) as status:
            
            # Fetch data based on selection
            trends = scraper.get_trending_topics(selected_category)
            
            db_manager.save_trends(trends)
            status.update(label="✅ Scan Complete", state="complete", expanded=False)
            time.sleep(1)
            st.rerun()

st.markdown("---")

# --- 4. DATA DISPLAY LOGIC ---
raw_data = db_manager.get_history()

if not raw_data:
    st.info("👋 System Ready. Select a Niche and click 'Scan' to begin.")
else:
    # Sorting logic: Rank 1 first
    latest_batch = raw_data[:5]
    sorted_data = sorted(latest_batch, key=lambda x: x[1])
    
    # --- METRICS ROW ---
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.metric("Top Trend", sorted_data[0][0])
    with m2: st.metric("Velocity", "High 🔥")
    with m3: st.metric("Source", f"Google {selected_category}")
    with m4: st.metric("Database", f"{len(raw_data)} Items")
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- 5. THE MAIN LIST (CARDS) ---
    st.subheader(f"🚀 Active {selected_category} Trends")
    
    for item in sorted_data:
        topic = item[0]
        rank = item[1]
        timestamp = item[2]
        script_key = f"script_{rank}_{topic}"

        # Card Container
        with st.container():
            c1, c2, c3 = st.columns([0.1, 0.7, 0.2])
            
            with c1:
                st.markdown(f"<div class='rank-number'>#{rank}</div>", unsafe_allow_html=True)
            
            with c2:
                st.markdown(f"<h3 style='margin:0; padding-top:10px;'>{topic}</h3>", unsafe_allow_html=True)
                st.caption(f"🕒 Detected: {timestamp}")
                
                # SCRIPT DISPLAY (Persistent)
                if script_key in st.session_state and st.session_state[script_key]:
                    with st.expander("✨ View Viral Script", expanded=True):
                        st.code(st.session_state[script_key], language="markdown")
            
            with c3:
                st.write("")
                if st.button("✨ Generate", key=f"btn_{rank}", use_container_width=True):
                    with st.spinner("Writing..."):
                        script = ai_agent.generate_script(topic)
                        st.session_state[script_key] = script
                        st.rerun()
            
            st.divider()

# --- FOOTER ---
st.markdown("<div style='text-align: center; margin-top: 50px; color: #555;'>ENGINEERED WITH ❤️ IN PYTHON</div>", unsafe_allow_html=True)