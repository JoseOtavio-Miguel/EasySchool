/* OPEN MODAL */
document.querySelectorAll('[data-open-modal]').forEach(button => {
    button.addEventListener('click', e => {
        e.preventDefault();
        const modalName = button.dataset.openModal;
        const modal = document.querySelector(`[data-modal="${modalName}"]`);
        modal?.classList.add('active');
    });
});

/* CLOSE MODAL (BOTÃO X) */
document.querySelectorAll('[data-close-modal]').forEach(button => {
    button.addEventListener('click', () => {
        button.closest('.simple-modal-overlay')
              .classList.remove('active');
    });
});

/* CLOSE CLICK OUTSIDE */
document.querySelectorAll('.simple-modal-overlay').forEach(modal => {
    modal.addEventListener('click', e => {
        if (e.target === modal) {
            modal.classList.remove('active');
        }
    });
});
