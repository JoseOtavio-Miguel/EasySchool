// Filtros
function filterTable() {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();
    const gradeLevel = document.getElementById('gradeLevelFilter').value;
    const grade = document.getElementById('gradeFilter').value;
    const shift = document.getElementById('shiftFilter').value;
    const status = document.getElementById('statusFilter').value;
    const ageRange = document.getElementById('ageFilter').value;
    
    const rows = document.querySelectorAll('#studentsTable tr[data-student-id]');
    let visibleCount = 0;
    
    rows.forEach(row => {
        const studentName = row.cells[0].textContent.toLowerCase();
        const enrollment = row.cells[1].textContent.toLowerCase();
        const studentGradeLevel = row.dataset.grade;
        const studentShift = row.dataset.shift;
        const studentStatus = row.dataset.status;
        const studentAge = parseInt(row.dataset.age) || 0;
        
        let showRow = true;
        
        // Pesquisa por nome ou matrícula
        if (searchTerm && !studentName.includes(searchTerm) && !enrollment.includes(searchTerm)) {
            showRow = false;
        }
        
        // Filtro por nível escolar
        if (gradeLevel && studentGradeLevel !== gradeLevel) {
            showRow = false;
        }
        
        // Filtro por turno
        if (shift && studentShift !== shift) {
            showRow = false;
        }
        
        // Filtro por status
        if (status && studentStatus !== status) {
            showRow = false;
        }
        
        // Filtro por faixa etária
        if (ageRange) {
            const [min, max] = ageRange === '19+' ? [19, 100] : ageRange.split('-').map(Number);
            if (studentAge < min || studentAge > max) {
                showRow = false;
            }
        }
        
        // Filtro por ano 
        if (grade) {
            const gradeCell = row.cells[3].textContent;
            if (!gradeCell.includes(grade.replace('ANO', 'º').replace('MEDIO', 'º EM'))) {
                showRow = false;
            }
        }
        
        row.style.display = showRow ? '' : 'none';
        if (showRow) visibleCount++;
    });
    
    // Atualizar contador
    document.querySelector('.export-info').textContent = `Mostrando ${visibleCount} de {{ total_students }} registros`;
    
    // Mostrar mensagem se nenhum resultado
    const emptyState = document.querySelector('.empty-state');
    if (visibleCount === 0 && rows.length > 0) {
        if (!emptyState) {
            const tbody = document.getElementById('studentsTable');
            tbody.innerHTML = `
                <tr>
                    <td colspan="10">
                        <div class="empty-state">
                            <div class="empty-icon">🔍</div>
                            <div class="empty-title">Nenhum estudante encontrado</div>
                            <div class="empty-description">
                                Não há estudantes que correspondam aos filtros aplicados.
                            </div>
                            <button class="btn btn-secondary" onclick="resetFilters()">
                                <i class="fas fa-redo"></i> Limpar Filtros
                            </button>
                        </div>
                    </td>
                </tr>
            `;
        }
    }
}

function resetFilters() {
    document.getElementById('searchInput').value = '';
    document.getElementById('gradeLevelFilter').value = '';
    document.getElementById('gradeFilter').value = '';
    document.getElementById('shiftFilter').value = '';
    document.getElementById('statusFilter').value = '';
    document.getElementById('ageFilter').value = '';
    filterTable();
}

// Exportação CSV
function exportToCSV() {
    const rows = [];
    const headers = [];
    
    // Pegar cabeçalhos da tabela
    document.querySelectorAll('.modern-table th').forEach(th => {
        if (th.textContent !== 'Ações') {
            headers.push(`"${th.textContent}"`);
        }
    });
    rows.push(headers.join(','));
    
    // Pegar dados filtrados
    document.querySelectorAll('#studentsTable tr:not([style*="none"])').forEach(row => {
        if (row.querySelector('.empty-state')) return;
        
        const cells = [];
        row.querySelectorAll('td').forEach((cell, index) => {
            // Pular coluna de ações
            if (index !== 9) {
                let text = cell.textContent.trim();
                // Remover ícones e códigos extras
                text = text.replace(/📋|👨‍🎓|✅|🎓|📈|📊|🔍|📭/g, '')
                          .replace(/\n/g, ' ')
                          .replace(/\s+/g, ' ');
                cells.push(`"${text}"`);
            }
        });
        if (cells.length > 0) {
            rows.push(cells.join(','));
        }
    });
    
    const csvContent = rows.join('\n');
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    const url = URL.createObjectURL(blob);
    
    link.setAttribute('href', url);
    link.setAttribute('download', `estudantes_${new Date().toISOString().split('T')[0]}.csv`);
    link.style.visibility = 'hidden';
    
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

function selectFormat(format) {
    document.querySelectorAll('.format-option').forEach(option => {
        option.classList.remove('active');
        if (option.dataset.format === format) {
            option.classList.add('active');
        }
    });
}

function exportData() {
    const format = document.querySelector('.format-option.active').dataset.format;
    
    switch(format) {
        case 'csv':
            exportToCSV();
            break;
        case 'excel':
            exportToExcel();
            break;
        case 'json':
            exportToJSON();
            break;
    }
}

function exportToExcel() {
    // Implementação para Excel
    alert('Exportação para Excel em desenvolvimento');
}

function exportToJSON() {
    const data = [];
    
    document.querySelectorAll('#studentsTable tr:not([style*="none"])').forEach(row => {
        if (row.querySelector('.empty-state')) return;
        
        const student = {
            nome: row.cells[0].querySelector('strong').textContent,
            matricula: row.cells[1].textContent,
            nivel: row.cells[2].textContent,
            ano: row.cells[3].textContent,
            turno: row.cells[4].textContent,
            idade: row.cells[5].textContent,
            status: row.cells[6].textContent,
            email: row.cells[7].textContent,
            telefone: row.cells[8].textContent
        };
        data.push(student);
    });
    
    const jsonContent = JSON.stringify(data, null, 2);
    const blob = new Blob([jsonContent], { type: 'application/json' });
    const link = document.createElement('a');
    
    link.href = URL.createObjectURL(blob);
    link.download = `estudantes_${new Date().toISOString().split('T')[0]}.json`;
    link.click();
}

function copyToClipboard() {
    const rows = [];
    const headers = [];
    
    document.querySelectorAll('.modern-table th').forEach(th => {
        if (th.textContent !== 'Ações') {
            headers.push(th.textContent);
        }
    });
    rows.push(headers.join('\t'));
    
    document.querySelectorAll('#studentsTable tr:not([style*="none"])').forEach(row => {
        if (row.querySelector('.empty-state')) return;
        
        const cells = [];
        row.querySelectorAll('td').forEach((cell, index) => {
            if (index !== 9) {
                cells.push(cell.textContent.trim().replace(/\n/g, ' '));
            }
        });
        if (cells.length > 0) {
            rows.push(cells.join('\t'));
        }
    });
    
    const text = rows.join('\n');
    
    navigator.clipboard.writeText(text).then(() => {
        alert('Dados copiados para a área de transferência!');
    }).catch(err => {
        console.error('Erro ao copiar:', err);
        alert('Erro ao copiar dados');
    });
}

// Ações dos estudantes
function viewStudent(studentId) {
    window.location.href = `/students/${studentId}/`;
}

function editStudent(studentId) {
    window.location.href = `/students/${studentId}/edit/`;
}

function deleteStudent(studentId, studentName) {
    if (confirm(`Tem certeza que deseja excluir o estudante "${studentName}"?\n\nEsta ação não pode ser desfeita.`)) {
        fetch(`/students/${studentId}/delete/`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': '{{ csrf_token }}',
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (response.ok) {
                alert('Estudante excluído com sucesso!');
                location.reload();
            } else {
                alert('Erro ao excluir estudante');
            }
        })
        .catch(error => {
            console.error('Erro:', error);
            alert('Erro ao excluir estudante');
        });
    }
}

// Paginação
function changePage(page) {
    const url = new URL(window.location.href);
    url.searchParams.set('page', page);
    window.location.href = url.toString();
}

// Modal (integrado com a solução anterior)
function openCreateModal() {
    // Usar o modal unificado da solução anterior
    if (typeof openUserModal === 'function') {
        openUserModal('create', 'student');
    } else {
        window.location.href = '/students/create/';
    }
}

// Inicialização
document.addEventListener('DOMContentLoaded', function() {
    // Aplicar filtros iniciais se houver parâmetros na URL
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('search')) {
        document.getElementById('searchInput').value = urlParams.get('search');
    }
    
    // Adicionar atalhos de teclado
    document.addEventListener('keydown', function(e) {
        if (e.ctrlKey && e.key === 'f') {
            e.preventDefault();
            document.getElementById('searchInput').focus();
        }
        if (e.ctrlKey && e.key === 'e') {
            e.preventDefault();
            exportToCSV();
        }
    });
});