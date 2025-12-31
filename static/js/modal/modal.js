document.querySelectorAll('[data-open-modal]').forEach(button => {
    button.addEventListener('click', e => {
        e.preventDefault();

        const modalName = button.dataset.openModal;
        const mode = button.dataset.mode;
        const studentId = button.dataset.studentId;

        console.log('Opening modal:', { modalName, mode, studentId }); // Debug

        const modal = document.querySelector(`[data-modal="${modalName}"]`);
        const form = modal.querySelector('form');
        const modalTitle = modal.querySelector('#modal-title');

        modal.classList.add('active');
        initModalTabs(modal);

        if (mode === 'edit' && studentId) {
            // EDIT MODE
            if (modalTitle) modalTitle.textContent = 'Editar Estudante';
            
            // URL correta baseada no seu urls.py
            // JavaScript
            const url = `/administrator/students/${studentId}/json/`;   
            console.log('Fetching from:', url); // Debug
            
            fetch(url)
                .then(response => {
                    console.log('Response status:', response.status); // Debug
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(student => {
                    console.log('✅ Student data received:', student); // Debug
                    
                    // Função auxiliar
                    const setFieldValue = (id, value) => {
                        const field = document.getElementById(id);
                        if (field) {
                            field.value = value || '';
                            console.log(`Set ${id}:`, value); // Debug
                        } else {
                            console.warn(`⚠️ Field not found: ${id}`);
                        }
                    };
                    
                    // Preencher student_id (IMPORTANTE!)
                    setFieldValue("student_id", student.id);
                    
                    // Personal Data
                    setFieldValue("first_name", student.first_name);
                    setFieldValue("last_name", student.last_name);
                    setFieldValue("cpf", student.cpf);
                    setFieldValue("rg", student.rg);
                    setFieldValue("date_of_birth", student.date_of_birth);
                    setFieldValue("gender", student.gender);

                    // Academic Info
                    setFieldValue("enrollment_number", student.enrollment_number);
                    setFieldValue("grade_level", student.grade_level);
                    setFieldValue("specific_grade", student.specific_grade);
                    setFieldValue("shift", student.shift);

                    // Contact
                    setFieldValue("father_name", student.father_name);
                    setFieldValue("mother_name", student.mother_name);
                    setFieldValue("guardian_name", student.guardian_name);
                    setFieldValue("email", student.email);
                    setFieldValue("phone", student.phone);
                    setFieldValue("guardian_phone", student.guardian_phone);

                    // Address
                    setFieldValue("address", student.address);
                    setFieldValue("address_number", student.address_number);
                    setFieldValue("complement", student.complement);
                    setFieldValue("neighborhood", student.neighborhood);
                    setFieldValue("zip_code", student.zip_code);
                    setFieldValue("city", student.city);
                    setFieldValue("state", student.state);

                    console.log('✅ All fields populated successfully');
                })
                .catch(error => {
                    console.error('❌ Error loading student:', error);
                    alert('Erro ao carregar dados: ' + error.message);
                });
        } else {
            // CREATE MODE
            console.log('Create mode - clearing form');
            if (modalTitle) modalTitle.textContent = 'Novo Estudante';
            form.reset();
            document.getElementById("student_id").value = '';
        }
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
