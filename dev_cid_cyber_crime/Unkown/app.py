import streamlit as st
import time
import base64
from datetime import datetime, timedelta
import requests
from io import BytesIO
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="CID Cyber Crime",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for cyber theme
def load_css():
    st.markdown("""
    <style>
    /* Import fonts */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&display=swap');
    
    /* Root variables */
    :root {
        --cyber-blue: #00d4ff;
        --cyber-dark: #0a0a0f;
        --cyber-card: #1a1a2e;
        --cyber-border: rgba(0, 212, 255, 0.2);
        --cyber-green: #10b981;
        --cyber-red: #ef4444;
    }
    
    /* Main app styling */
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 100%;
    }
    
    /* Background */
    .stApp {
        background: linear-gradient(135deg, #0a0a0f 0%, #1a1a2e 100%);
        background-attachment: fixed;
        font-family: 'Orbitron', monospace;
    }
    
    /* Cyber grid background */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: 
            linear-gradient(rgba(0, 212, 255, 0.1) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 212, 255, 0.1) 1px, transparent 1px);
        background-size: 50px 50px;
        pointer-events: none;
        z-index: -1;
    }
    
    /* Header styling */
    .header-container {
        background: rgba(26, 26, 46, 0.3);
        border: 1px solid var(--cyber-border);
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.3);
    }
    
    .logo-container {
        display: flex;
        align-items: center;
        gap: 20px;
        margin-bottom: 20px;
    }
    
    .cyber-title {
        color: var(--cyber-blue);
        font-size: 2.5rem;
        font-weight: 700;
        text-shadow: 0 0 10px rgba(0, 212, 255, 0.5);
        margin: 0;
        font-family: 'Orbitron', monospace;
    }
    
    .division-badge {
        background: rgba(16, 185, 129, 0.1);
        color: #10b981;
        border: 1px solid rgba(16, 185, 129, 0.5);
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
        display: inline-block;
        margin-top: 5px;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: rgba(26, 26, 46, 0.3);
        border-right: 1px solid var(--cyber-border);
        backdrop-filter: blur(10px);
    }
    
    .filter-header {
        color: var(--cyber-blue);
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 20px;
        text-align: center;
        font-family: 'Orbitron', monospace;
    }
    
    .filter-card {
        background: rgba(26, 26, 46, 0.5);
        border: 1px solid var(--cyber-border);
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.2);
    }
    
    .filter-title {
        color: var(--cyber-blue);
        font-size: 1rem;
        font-weight: 500;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(45deg, var(--cyber-blue), #0ea5e9);
        color: var(--cyber-dark);
        border: 1px solid var(--cyber-blue);
        border-radius: 8px;
        font-weight: 600;
        font-family: 'Orbitron', monospace;
        transition: all 0.3s ease;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.3);
    }
    
    .stButton > button:hover {
        box-shadow: 0 0 25px rgba(0, 212, 255, 0.6);
        transform: translateY(-2px);
    }
    
    /* Search results area */
    .search-results {
        background: rgba(26, 26, 46, 0.3);
        border: 1px solid var(--cyber-border);
        border-radius: 10px;
        padding: 40px;
        text-align: center;
        backdrop-filter: blur(10px);
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.3);
        min-height: 400px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }
    
    .search-icon {
        width: 80px;
        height: 80px;
        background: rgba(0, 212, 255, 0.2);
        border: 2px solid var(--cyber-blue);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 20px;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { box-shadow: 0 0 10px rgba(0, 212, 255, 0.3); }
        50% { box-shadow: 0 0 30px rgba(0, 212, 255, 0.6); }
    }
    
    .search-title {
        color: var(--cyber-blue);
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 10px;
    }
    
    .search-subtitle {
        color: #94a3b8;
        margin-bottom: 20px;
    }
    
    .ready-badge {
        background: rgba(0, 212, 255, 0.1);
        color: var(--cyber-blue);
        border: 1px solid rgba(0, 212, 255, 0.5);
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.9rem;
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid var(--cyber-border);
        border-radius: 8px;
        color: #e0e6ed;
        font-family: 'Orbitron', monospace;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: var(--cyber-blue);
        box-shadow: 0 0 10px rgba(0, 212, 255, 0.3);
    }
    
    /* Checkbox styling */
    .stCheckbox > label {
        color: #e0e6ed !important;
        font-family: 'Orbitron', monospace;
    }
    
    /* Success/Error messages */
    .success-msg {
        background: rgba(16, 185, 129, 0.1);
        color: #10b981;
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-radius: 8px;
        padding: 10px 15px;
        margin: 10px 0;
    }
    
    .error-msg {
        background: rgba(239, 68, 68, 0.1);
        color: #ef4444;
        border: 1px solid rgba(239, 68, 68, 0.3);
        border-radius: 8px;
        padding: 10px 15px;
        margin: 10px 0;
    }
    
    /* Hide streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def create_header():
    """Create the header with logo, title, search box and control buttons"""
    st.markdown("""
    <div class="header-container">
        <div class="logo-container">
            <img src="https://pbs.twimg.com/profile_images/1579353190239125505/eJQ6CjIk_400x400.jpg" 
                 width="80" height="80" style="border-radius: 10px; box-shadow: 0 0 20px rgba(0, 212, 255, 0.5);">
            <div>
                <h1 class="cyber-title">CID CYBER CRIME</h1>
                <span class="division-badge">DIVISION</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_sidebar():
    """Create the filter sidebar"""
    st.sidebar.markdown('<div class="filter-header">🔍 SEARCH FILTERS</div>', unsafe_allow_html=True)
    
    st.sidebar.markdown("""
    <div class="filter-card">
        <div class="filter-title">⏰ Time Range</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Time range filters
    time_options = {
        "All": True,
        "Past Hour": False,
        "Past 24 Hours": False,
        "Past Week": False,
        "Past Month": False,
        "Past Year": False
    }
    
    selected_times = []
    for option, default in time_options.items():
        if st.sidebar.checkbox(option, value=default, key=f"time_{option}"):
            selected_times.append(option)
    
    return selected_times

def create_control_panel():
    """Create the search box and control buttons"""
    col1, col2, col3, col4, col5, col6 = st.columns([3, 1, 1, 1, 1, 1])
    
    with col1:
        search_query = st.text_input("", placeholder="Enter search query...", key="search_input")
    
    with col2:
        start_clicked = st.button("▶️ START", key="start_btn")
    
    with col3:
        stop_clicked = st.button("⏹️ STOP", key="stop_btn")
    
    with col4:
        refresh_clicked = st.button("🔄 REFRESH", key="refresh_btn")
    
    with col5:
        screenshot_clicked = st.button("📷 SCREENSHOT", key="screenshot_btn")
    
    return search_query, start_clicked, stop_clicked, refresh_clicked, screenshot_clicked

def create_search_results_area():
    """Create the main search results display area"""
    st.markdown("""
    <div class="search-results">
        <div class="search-icon">
            <span style="font-size: 40px; color: var(--cyber-blue);">🔍</span>
        </div>
        <h2 class="search-title">SEARCH RESULTS</h2>
        <p class="search-subtitle">Enter a search query and click START to begin monitoring</p>
        <span class="ready-badge">READY FOR INPUT</span>
    </div>
    """, unsafe_allow_html=True)

def handle_operations(search_query, start_clicked, stop_clicked, refresh_clicked, screenshot_clicked, selected_times):
    """Handle button clicks and operations"""
    
    if start_clicked and search_query:
        st.markdown('<div class="success-msg">🚀 Search started for: "{}"</div>'.format(search_query), unsafe_allow_html=True)
        st.markdown('<div class="success-msg">⏱️ Time filters: {}</div>'.format(", ".join(selected_times)), unsafe_allow_html=True)
        
        # Simulate search progress
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(100):
            progress_bar.progress(i + 1)
            status_text.text(f'Searching... {i+1}%')
            time.sleep(0.02)
        
        status_text.text('Search completed!')
        
        # Display mock results
        st.success("✅ Search completed successfully!")
        st.info(f"🔍 Found 42 results for '{search_query}' in selected time range")
        
    elif start_clicked and not search_query:
        st.markdown('<div class="error-msg">⚠️ Please enter a search query before starting</div>', unsafe_allow_html=True)
    
    if stop_clicked:
        st.markdown('<div class="error-msg">🛑 Search operation stopped</div>', unsafe_allow_html=True)
    
    if refresh_clicked:
        st.markdown('<div class="success-msg">🔄 Interface refreshed</div>', unsafe_allow_html=True)
        st.rerun()
    
    if screenshot_clicked:
        st.markdown('<div class="success-msg">📷 Screenshot captured</div>', unsafe_allow_html=True)
        st.info("Screenshot saved to: /screenshots/cyber_crime_dashboard_{}.png".format(datetime.now().strftime("%Y%m%d_%H%M%S")))

def main():
    """Main application function"""
    # Load custom CSS
    load_css()
    
    # Create header
    create_header()
    
    # Create sidebar with filters
    selected_times = create_sidebar()
    
    # Create main content area
    st.markdown("### 🔍 Search Controls")
    search_query, start_clicked, stop_clicked, refresh_clicked, screenshot_clicked = create_control_panel()
    
    st.markdown("### 📊 Results Dashboard")
    
    # Handle operations
    if any([start_clicked, stop_clicked, refresh_clicked, screenshot_clicked]):
        handle_operations(search_query, start_clicked, stop_clicked, refresh_clicked, screenshot_clicked, selected_times)
    else:
        create_search_results_area()
    
    # Display current status
    with st.expander("🔧 System Status", expanded=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Active Filters", len(selected_times))
        with col2:
            st.metric("Search Status", "Ready" if not start_clicked else "Active")
        with col3:
            st.metric("Last Updated", datetime.now().strftime("%H:%M:%S"))

if __name__ == "__main__":
    main()