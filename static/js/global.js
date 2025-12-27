function openCreateModal(type) {
    const modal = document.getElementById(`modal-${type}`);
    if (modal) modal.classList.add('active');
}

function closeModal(type) {
    const modal = document.getElementById(`modal-${type}`);
    if (modal) modal.classList.remove('active');
}


// Script for Sidebar Map Pages
document.addEventListener('DOMContentLoaded', function() {
    // Mapeamento de URLs para itens do menu
    const menuMapping = {
        '/dashboard/': 'dashboard',
        '/gerenciar-alunos/': 'gerenciar_alunos',
        '/relatorios/': 'relatorios',
        '/cadastrar-estudante/': 'cadastrar_estudante',
        '/cadastrar-professor/': 'cadastrar_professor'
    };
    
    const currentPath = window.location.pathname;
    
    
    document.querySelectorAll('.menu-item').forEach(item => {
        item.classList.remove('active');
    });
    
    
    for (const [path, menuId] of Object.entries(menuMapping)) {
        if (currentPath.startsWith(path)) {
            const menuItem = document.querySelector(`a[href="${path}"]`);
            if (menuItem) {
                menuItem.classList.add('active');
            }
        }
    }
});