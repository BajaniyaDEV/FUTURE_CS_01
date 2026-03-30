#!/usr/bin/env python3
"""
CID Cyber Crime Dashboard Launcher
Simple script to launch the Streamlit dashboard with optimized settings
"""

import subprocess
import sys
import os
from pathlib import Path

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = ['streamlit', 'pillow', 'requests']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n📦 Install missing packages with:")
        print("   pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies are installed")
    return True

def launch_dashboard():
    """Launch the Streamlit dashboard with optimized settings"""
    
    # Check if app.py exists
    if not Path("app.py").exists():
        print("❌ app.py not found in current directory")
        print("   Make sure you're running this script from the project directory")
        return False
    
    # Check dependencies
    if not check_dependencies():
        return False
    
    print("🚀 Launching CID Cyber Crime Dashboard...")
    print("🌐 Dashboard will open in your default web browser")
    print("🔗 URL: http://localhost:8501")
    print("\n⚡ Starting Streamlit server...")
    print("   Press Ctrl+C to stop the server\n")
    
    try:
        # Launch Streamlit with optimized settings
        cmd = [
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port=8501",
            "--server.address=localhost",
            "--browser.gatherUsageStats=false",
            "--server.enableCORS=false",
            "--server.enableXsrfProtection=false"
        ]
        
        subprocess.run(cmd, check=True)
        
    except KeyboardInterrupt:
        print("\n🛑 Dashboard stopped by user")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error launching dashboard: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return False

def main():
    """Main function"""
    print("=" * 50)
    print("🔒 CID CYBER CRIME DASHBOARD")
    print("=" * 50)
    
    # Change to script directory
    script_dir = Path(__file__).parent.absolute()
    os.chdir(script_dir)
    print(f"📂 Working directory: {script_dir}")
    
    # Launch the dashboard
    success = launch_dashboard()
    
    if success:
        print("\n✅ Dashboard session completed successfully")
    else:
        print("\n❌ Dashboard launch failed")
        sys.exit(1)

if __name__ == "__main__":
    main()