// Toggle Admin Modal in login.html
function toggleAdminModal() {
    const modal = document.getElementById('admin-modal');
    if (modal.classList.contains('hidden')) {
        modal.classList.remove('hidden');
        modal.classList.add('flex');
    } else {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
    }
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('admin-modal');
    if (event.target == modal) {
        toggleAdminModal();
    }
}

// Handle Admin Actions (Schedule/Cancel)
async function updateStatus(id, action) {
    try {
        const res = await fetch('/admin/action', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id, action })
        });
        
        if (res.ok) {
            window.location.reload();
        } else {
            alert('Failed to update status');
        }
    } catch (err) {
        console.error(err);
    }
}
