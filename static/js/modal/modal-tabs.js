/* OPEN MODAL */
document.querySelectorAll('[data-open-modal]').forEach(button => {
    button.addEventListener('click', e => {
        e.preventDefault();
        const modalName = button.dataset.openModal;
        const modal = document.querySelector(`[data-modal="${modalName}"]`);
        
        if (modal) {
            modal.classList.add('active');
            initModalTabs(modal);
        }
    });
});

/* CLOSE MODAL */
document.querySelectorAll('[data-close-modal]').forEach(button => {
    button.addEventListener('click', () => {
        const modal = button.closest('.simple-modal-overlay');
        if (modal) {
            modal.classList.remove('active');
        }
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
    const tabButtons = modal.querySelectorAll('.tab-btn');
    const tabContents = modal.querySelectorAll('.tab-content');
    
    if (!tabButtons.length) return;
    
    // Detectar automaticamente as abas baseado nos botões
    const tabList = Array.from(tabButtons).map(btn => btn.dataset.tab);
    let currentIndex = 0;

    const indicator = modal.querySelector('#current-tab');

    function switchTab(tabName) {
        // Remover active de todas as abas
        tabContents.forEach(tab => tab.classList.remove('active'));
        tabButtons.forEach(btn => btn.classList.remove('active'));

        // Adicionar active na aba selecionada
        const targetTab = modal.querySelector(`#${tabName}-tab`);
        const targetButton = modal.querySelector(`.tab-btn[data-tab="${tabName}"]`);
        
        if (targetTab) targetTab.classList.add('active');
        if (targetButton) targetButton.classList.add('active');

        currentIndex = tabList.indexOf(tabName);
        if (indicator) indicator.textContent = currentIndex + 1;
    }

    // Event listeners para os botões de aba
    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            switchTab(button.dataset.tab);
        });
    });

    // Botão "Próximo"
    const nextButton = modal.querySelector('[data-next-tab]');
    if (nextButton) {
        nextButton.addEventListener('click', () => {
            if (currentIndex < tabList.length - 1) {
                switchTab(tabList[currentIndex + 1]);
            }
        });
    }

    // Botão "Anterior"
    const prevButton = modal.querySelector('[data-prev-tab]');
    if (prevButton) {
        prevButton.addEventListener('click', () => {
            if (currentIndex > 0) {
                switchTab(tabList[currentIndex - 1]);
            }
        });
    }

    // Iniciar na primeira aba
    switchTab(tabList[0]);
}