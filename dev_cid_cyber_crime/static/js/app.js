// Global application state
let appState = {
    searchQuery: '',
    isRunning: false,
    selectedTimeRange: 'all',
    results: []
};

// DOM elements
let elements = {};

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    initializeElements();
    initializeEventListeners();
    createFloatingParticles();
    startStatusPolling();
});

function initializeElements() {
    elements = {
        searchInput: document.getElementById('searchInput'),
        startBtn: document.getElementById('startBtn'),
        stopBtn: document.getElementById('stopBtn'),
        refreshBtn: document.getElementById('refreshBtn'),
        screenshotBtn: document.getElementById('screenshotBtn'),
        searchForm: document.getElementById('searchForm'),
        timeRangeGroup: document.getElementById('timeRangeGroup'),
        emptyState: document.getElementById('emptyState'),
        resultsContent: document.getElementById('resultsContent'),
        resultsTitle: document.getElementById('resultsTitle'),
        resultCount: document.getElementById('resultCount'),
        searchQuery: document.getElementById('searchQuery'),
        resultsList: document.getElementById('resultsList'),
        progressContainer: document.getElementById('progressContainer'),
        progressFill: document.getElementById('progressFill'),
        progressText: document.getElementById('progressText'),
        statusMessages: document.getElementById('statusMessages')
    };
}

function initializeEventListeners() {
    // Search form submission
    elements.searchForm.addEventListener('submit', function(e) {
        e.preventDefault();
        handleStart();
    });

    // Button click handlers
    elements.startBtn.addEventListener('click', handleStart);
    elements.stopBtn.addEventListener('click', handleStop);
    elements.refreshBtn.addEventListener('click', handleRefresh);
    elements.screenshotBtn.addEventListener('click', handleScreenshot);

    // Time range radio buttons
    const radioButtons = elements.timeRangeGroup.querySelectorAll('input[type="radio"]');
    radioButtons.forEach(radio => {
        radio.addEventListener('change', function() {
            appState.selectedTimeRange = this.value;
        });
    });

    // Search input changes
    elements.searchInput.addEventListener('input', function() {
        appState.searchQuery = this.value;
    });
}

function createFloatingParticles() {
    const particlesContainer = document.querySelector('.floating-particles');
    const particleCount = 20;

    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.top = Math.random() * 100 + '%';
        particle.style.animationDelay = Math.random() * 3 + 's';
        particle.style.animationDuration = (2 + Math.random() * 3) + 's';
        particlesContainer.appendChild(particle);
    }
}

// Button handlers
async function handleStart() {
    const query = elements.searchInput.value.trim();
    
    if (!query) {
        showStatusMessage('Please enter a search query before starting', 'error');
        return;
    }

    appState.isRunning = true;
    updateButtonStates();
    
    try {
        // Show progress
        showProgress();
        
        const response = await fetch('/api/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                action: 'start',
                query: query,
                timeRange: appState.selectedTimeRange
            })
        });

        const data = await response.json();
        
        if (data.success) {
            showStatusMessage(data.message, 'success');
            showStatusMessage(`Time filter: ${getTimeRangeLabel(appState.selectedTimeRange)}`, 'info');
            
            // Simulate progress
            await simulateProgress();
            
            // Display results
            displayResults(data.results, query, data.resultCount);
        } else {
            showStatusMessage(data.message, 'error');
            appState.isRunning = false;
            updateButtonStates();
            hideProgress();
        }
    } catch (error) {
        console.error('Error starting search:', error);
        showStatusMessage('Error starting search operation', 'error');
        appState.isRunning = false;
        updateButtonStates();
        hideProgress();
    }
}

async function handleStop() {
    try {
        const response = await fetch('/api/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                action: 'stop'
            })
        });

        const data = await response.json();
        
        if (data.success) {
            showStatusMessage(data.message, 'error');
            appState.isRunning = false;
            updateButtonStates();
            hideProgress();
        }
    } catch (error) {
        console.error('Error stopping search:', error);
        showStatusMessage('Error stopping search operation', 'error');
    }
}

async function handleRefresh() {
    try {
        const response = await fetch('/api/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                action: 'refresh'
            })
        });

        const data = await response.json();
        
        if (data.success) {
            showStatusMessage(data.message, 'success');
            
            // Reset UI
            resetInterface();
            
            // Reload page after short delay
            setTimeout(() => {
                window.location.reload();
            }, 500);
        }
    } catch (error) {
        console.error('Error refreshing interface:', error);
        showStatusMessage('Error refreshing interface', 'error');
    }
}

async function handleScreenshot() {
    try {
        const response = await fetch('/api/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                action: 'screenshot'
            })
        });

        const data = await response.json();
        
        if (data.success) {
            showStatusMessage(data.message, 'success');
            showStatusMessage(`Saved to: ${data.path}`, 'info');
        }
    } catch (error) {
        console.error('Error taking screenshot:', error);
        showStatusMessage('Error capturing screenshot', 'error');
    }
}

// UI update functions
function updateButtonStates() {
    if (appState.isRunning) {
        elements.startBtn.disabled = true;
        elements.startBtn.style.opacity = '0.6';
        elements.stopBtn.disabled = false;
        elements.stopBtn.style.opacity = '1';
    } else {
        elements.startBtn.disabled = false;
        elements.startBtn.style.opacity = '1';
        elements.stopBtn.disabled = false;
        elements.stopBtn.style.opacity = '1';
    }
}

function showProgress() {
    elements.progressContainer.style.display = 'block';
    elements.emptyState.style.display = 'none';
    elements.resultsContent.style.display = 'none';
}

function hideProgress() {
    elements.progressContainer.style.display = 'none';
}

async function simulateProgress() {
    return new Promise((resolve) => {
        let progress = 0;
        const interval = setInterval(() => {
            progress += Math.random() * 15;
            if (progress >= 100) {
                progress = 100;
                clearInterval(interval);
                resolve();
            }
            
            elements.progressFill.style.width = progress + '%';
            elements.progressText.textContent = `Searching... ${Math.round(progress)}%`;
        }, 100);
    });
}

function displayResults(results, query, count) {
    hideProgress();
    elements.emptyState.style.display = 'none';
    elements.resultsContent.style.display = 'flex';
    
    elements.resultCount.textContent = `${count} results`;
    elements.searchQuery.textContent = `for "${query}"`;
    
    // Clear previous results
    elements.resultsList.innerHTML = '';
    
    // Add results
    results.forEach((result, index) => {
        const resultElement = createResultElement(result, index);
        elements.resultsList.appendChild(resultElement);
    });
    
    appState.results = results;
    appState.isRunning = false;
    updateButtonStates();
}

function createResultElement(result, index) {
    const resultDiv = document.createElement('div');
    resultDiv.className = 'result-item';
    resultDiv.innerHTML = `
        <h3>${result.title}</h3>
        <div class="result-url">${result.url}</div>
        <div class="result-snippet">${result.snippet}</div>
    `;
    
    // Add staggered animation
    resultDiv.style.animation = `slideIn 0.5s ease-out ${index * 0.1}s both`;
    
    return resultDiv;
}

function resetInterface() {
    elements.searchInput.value = '';
    elements.emptyState.style.display = 'flex';
    elements.resultsContent.style.display = 'none';
    elements.progressContainer.style.display = 'none';
    
    // Reset radio to "All"
    document.getElementById('all').checked = true;
    
    appState = {
        searchQuery: '',
        isRunning: false,
        selectedTimeRange: 'all',
        results: []
    };
    
    updateButtonStates();
}

function showStatusMessage(message, type = 'info') {
    const messageDiv = document.createElement('div');
    messageDiv.className = `status-message ${type}`;
    messageDiv.textContent = message;
    
    elements.statusMessages.appendChild(messageDiv);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (messageDiv.parentNode) {
            messageDiv.remove();
        }
    }, 5000);
    
    // Add click to dismiss
    messageDiv.addEventListener('click', () => {
        messageDiv.remove();
    });
}

function getTimeRangeLabel(value) {
    const labels = {
        'all': 'All',
        'hour': 'Past Hour',
        'day': 'Past 24 Hours',
        'week': 'Past Week',
        'month': 'Past Month',
        'year': 'Past Year'
    };
    return labels[value] || value;
}

// Status polling
function startStatusPolling() {
    setInterval(async () => {
        try {
            const response = await fetch('/api/status');
            const status = await response.json();
            
            // Update UI based on server status if needed
            if (status.isRunning !== appState.isRunning) {
                appState.isRunning = status.isRunning;
                updateButtonStates();
            }
        } catch (error) {
            // Silently handle polling errors
            console.debug('Status polling error:', error);
        }
    }, 5000); // Poll every 5 seconds
}

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl+Enter or Cmd+Enter to start search
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        e.preventDefault();
        handleStart();
    }
    
    // Escape to stop search
    if (e.key === 'Escape' && appState.isRunning) {
        e.preventDefault();
        handleStop();
    }
    
    // F5 to refresh (prevent default and use our refresh)
    if (e.key === 'F5') {
        e.preventDefault();
        handleRefresh();
    }
});

// Focus search input on page load
window.addEventListener('load', function() {
    elements.searchInput.focus();
});