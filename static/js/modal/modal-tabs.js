/* OPEN MODAL */
document.querySelectorAll('[data-open-modal]').forEach(button => {
    button.addEventListener('click', e => {
        e.preventDefault();
        const modalName = button.dataset.openModal;
        const modal = document.querySelector(`[data-modal="${modalName}"]`);
        modal?.classList.add('active');

        initModalTabs(modal); // inicializa abas do modal aberto
    });
});

/* CLOSE MODAL */
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

/* ===========================
   MODAL TABS 
=========================== */

function initModalTabs(modal) {
    const tabList = ['personal', 'academic', 'contact', 'address'];
    let currentIndex = 0;

    const tabButtons = modal.querySelectorAll('.tab-btn');
    const tabContents = modal.querySelectorAll('.tab-content');
    const indicator = modal.querySelector('[data-current-tab]');

    function switchTab(tabName) {
        tabContents.forEach(tab => tab.classList.remove('active'));
        modal.querySelector(`#${tabName}-tab`)?.classList.add('active');

        tabButtons.forEach(btn => btn.classList.remove('active'));
        modal.querySelector(`.tab-btn[data-tab="${tabName}"]`)
             ?.classList.add('active');

        currentIndex = tabList.indexOf(tabName);
        if (indicator) indicator.textContent = currentIndex + 1;
    }

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            switchTab(button.dataset.tab);
        });
    });

    modal.querySelector('[data-next-tab]')?.addEventListener('click', () => {
        if (currentIndex < tabList.length - 1) {
            switchTab(tabList[currentIndex + 1]);
        }
    });

    modal.querySelector('[data-prev-tab]')?.addEventListener('click', () => {
        if (currentIndex > 0) {
            switchTab(tabList[currentIndex - 1]);
        }
    });

    switchTab(tabList[0]); // inicia na primeira aba
}
