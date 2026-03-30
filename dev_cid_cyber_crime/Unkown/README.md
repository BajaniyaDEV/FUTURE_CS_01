# CID Cyber Crime Dashboard - Python Version

A Python-based cyber crime monitoring dashboard built with Streamlit, featuring the same functionality as the React version.

## Features

- **Cyber-themed UI**: Dark theme with neon blue accents and futuristic styling
- **Official CID Logo**: Displays the official CID Cyber Crime logo
- **Search Functionality**: Search box with query input
- **Time Range Filters**: Filter results by time periods (All, Past Hour, Past 24 Hours, etc.)
- **Control Buttons**: Start, Stop, Refresh, and Screenshot functionality
- **Real-time Progress**: Visual progress indicators for search operations
- **Responsive Layout**: Sidebar filters with main content area

## Installation

1. **Clone or create the project directory:**
```bash
mkdir cid-cyber-dashboard
cd cid-cyber-dashboard
```

2. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

## Usage

1. **Run the Streamlit application:**
```bash
streamlit run app.py
```

2. **Open your web browser and navigate to:**
```
http://localhost:8501
```

3. **Using the Dashboard:**
   - Enter a search query in the search box
   - Select time range filters from the sidebar
   - Click **START** to begin monitoring
   - Use **STOP** to halt operations
   - **REFRESH** to reset the interface
   - **SCREENSHOT** to capture the current state

## Project Structure

```
cid-cyber-dashboard/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Features Explained

### Search Controls
- **Search Box**: Enter keywords or queries to search for
- **START Button**: Initiates the search operation with progress tracking
- **STOP Button**: Halts any running search operations
- **REFRESH Button**: Resets the interface and clears results
- **SCREENSHOT Button**: Captures the current dashboard state

### Filter Sidebar
- **Time Range Filters**: Select from multiple time periods:
  - All (default)
  - Past Hour
  - Past 24 Hours
  - Past Week
  - Past Month
  - Past Year

### Visual Feedback
- Real-time progress bars during search operations
- Success/error message notifications
- System status indicators
- Cyber-themed animations and effects

## Customization

The application uses custom CSS for the cyber theme. You can modify the styling by editing the `load_css()` function in `app.py`:

- **Colors**: Modify the CSS variables in the `:root` section
- **Fonts**: Change the font family imports and references
- **Animations**: Adjust the keyframes and animation properties
- **Layout**: Modify the container styles and spacing

## Technical Details

- **Framework**: Streamlit 1.28.0+
- **Language**: Python 3.7+
- **Styling**: Custom CSS with cyber theme
- **Icons**: Unicode emojis for cross-platform compatibility
- **Images**: Direct URL loading for the CID logo

## Browser Compatibility

The dashboard works best in modern web browsers that support:
- CSS Grid and Flexbox
- CSS Variables
- CSS Animations
- HTML5 features

## Security Note

This is a demonstration dashboard. For production use in cybersecurity environments:
- Implement proper authentication
- Add input validation and sanitization
- Use secure API endpoints
- Follow cybersecurity best practices
- Ensure compliance with data protection regulations