function openCreateModal(type) {
    const modal = document.getElementById(`modal-${type}`);
    if (modal) modal.classList.add('active');
}

function closeModal(type) {
    const modal = document.getElementById(`modal-${type}`);
    if (modal) modal.classList.remove('active');
}
