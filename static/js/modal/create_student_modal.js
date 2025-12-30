
function nextTab() {
    if (currentTab < totalTabs) {
        const tabNames = ['personal', 'academic', 'contact', 'address'];
        switchTab(tabNames[currentTab]);
    } else {
        // If on last tab, submit form
        submitForm();
    }
}

function prevTab() {
    if (currentTab > 1) {
        const tabNames = ['personal', 'academic', 'contact', 'address'];
        switchTab(tabNames[currentTab - 2]);
    }
}

function updateTabIndicator() {
    document.getElementById('current-tab').textContent = currentTab;
    
    // Update button text on last tab
    const nextBtn = document.querySelector('.btn-next');
    const submitBtn = document.getElementById('submit-btn');
    
    if (currentTab === totalTabs) {
        nextBtn.style.display = 'none';
        submitBtn.style.display = 'block';
    } else {
        nextBtn.style.display = 'block';
        submitBtn.style.display = 'none';
    }
}

function submitForm() {
    // Submit the form
    document.querySelector('form').submit();
}

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    updateTabIndicator();
});