from flask import Flask, render_template, request, jsonify
import os
import time
from datetime import datetime
import base64
import io

app = Flask(__name__)
app.secret_key = 'cyber_crime_secret_key_2024'

# Global variables to track application state
search_state = {
    'query': '',
    'is_running': False,
    'selected_time_range': 'all',
    'results': [],
    'last_screenshot': None
}

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def handle_search():
    """Handle search operations"""
    global search_state
    
    data = request.get_json()
    action = data.get('action')
    query = data.get('query', '')
    time_range = data.get('timeRange', 'all')
    
    if action == 'start':
        if not query.strip():
            return jsonify({
                'success': False,
                'message': 'Please enter a search query before starting'
            })
        
        search_state['query'] = query
        search_state['is_running'] = True
        search_state['selected_time_range'] = time_range
        
        # Simulate search results
        mock_results = [
            {'title': f'Search result 1 for "{query}"', 'url': 'https://example1.com', 'snippet': 'Mock search result content...'},
            {'title': f'Search result 2 for "{query}"', 'url': 'https://example2.com', 'snippet': 'Another mock result...'},
            {'title': f'Search result 3 for "{query}"', 'url': 'https://example3.com', 'snippet': 'Third search result...'},
        ]
        search_state['results'] = mock_results
        
        return jsonify({
            'success': True,
            'message': f'Search started for: "{query}"',
            'results': mock_results,
            'timeRange': time_range,
            'resultCount': len(mock_results)
        })
    
    elif action == 'stop':
        search_state['is_running'] = False
        return jsonify({
            'success': True,
            'message': 'Search operation stopped'
        })
    
    elif action == 'refresh':
        search_state = {
            'query': '',
            'is_running': False,
            'selected_time_range': 'all',
            'results': [],
            'last_screenshot': None
        }
        return jsonify({
            'success': True,
            'message': 'Interface refreshed'
        })
    
    elif action == 'screenshot':
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f'/screenshots/cyber_crime_dashboard_{timestamp}.png'
        search_state['last_screenshot'] = screenshot_path
        
        return jsonify({
            'success': True,
            'message': 'Screenshot captured',
            'path': screenshot_path
        })
    
    return jsonify({'success': False, 'message': 'Invalid action'})

@app.route('/api/status')
def get_status():
    """Get current application status"""
    return jsonify({
        'query': search_state['query'],
        'isRunning': search_state['is_running'],
        'timeRange': search_state['selected_time_range'],
        'resultCount': len(search_state['results']),
        'results': search_state['results'][:5]  # Return first 5 results
    })

if __name__ == '__main__':
    # Create templates and static directories if they don't exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    os.makedirs('screenshots', exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=5000)