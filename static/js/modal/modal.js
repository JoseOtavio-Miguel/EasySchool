// ============================================
// MODAL SYSTEM - OPEN MODALS
// ============================================
document.querySelectorAll('[data-open-modal]').forEach(button => {
    button.addEventListener('click', e => {
        e.preventDefault();

        const { entity, mode, id, openModal } = button.dataset;
        const modal = document.querySelector(`[data-modal="${openModal}"]`);

        modal.classList.add('active');
        initModalTabs(modal);

        if (entity === 'student') {
            handleStudentModal(modal, mode, id);
        }

        if (entity === 'teacher') {
            handleTeacherModal(modal, mode, id);
        }
    });
});

// ============================================
// HANDLE STUDENT MODAL
// ============================================
function handleStudentModal(modal, mode, id) {
    const form = modal.querySelector('form');
    const modalTitle = modal.querySelector('.simple-modal-header h3');

    console.log('Opening student modal:', { mode, id });

    if (mode === 'edit') {
        // EDIT MODE
        if (modalTitle) modalTitle.textContent = 'Editar Estudante';
        
        const url = `/administrator/students/${id}/json/`;   
        console.log('Fetching from:', url);
        
        fetch(url)
            .then(response => {
                console.log('Response status:', response.status);
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(student => {
                console.log('Student data received:', student);
                
                // Helper function to set field values
                const setFieldValue = (id, value) => {
                    const field = modal.querySelector(`#${id}`);
                    if (field) {
                        field.value = value || '';
                        console.log(`Set ${id}:`, value);
                    } else {
                        console.warn(`Field not found: ${id}`);
                    }
                };
                
                // Fill student_id (hidden field)
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

                console.log('All fields populated successfully');
            })
            .catch(error => {
                console.error('Error loading student:', error);
                alert('Erro ao carregar dados: ' + error.message);
            });
    
    } else {
        // CREATE MODE
        console.log('Create mode - clearing form');
        if (modalTitle) modalTitle.textContent = 'Novo Estudante';
        form.reset();
        const studentIdField = modal.querySelector("#student_id");
        if (studentIdField) studentIdField.value = '';
    }
}

// ============================================
// HANDLE TEACHER MODAL
// ============================================
function handleTeacherModal(modal, mode, id) {
    const form = modal.querySelector('form');
    const modalTitle = modal.querySelector('.simple-modal-header h3');

    console.log('Opening teacher modal:', { mode, id });

    if (mode === "edit") {
        // EDIT MODE
        if (modalTitle) modalTitle.textContent = 'Editar Professor';

        const url = `/administrator/teachers/${id}/json/`;
        console.log('Fetching from:', url);

        fetch(url)
            .then(response => {
                console.log('Response status:', response.status);
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(teacher => {
                console.log('Teacher data received:', teacher);
                
                // Helper function to set field values
                const setFieldValue = (id, value) => {
                    const field = modal.querySelector(`#${id}`);
                    if (field) {
                        field.value = value || '';
                        console.log(`Set ${id}:`, value);
                    } else {
                        console.warn(`Field not found: ${id}`);
                    }
                };

                // Fill teacher_id (hidden field)
                setFieldValue("teacher_id", teacher.id);

                // Personal Data
                setFieldValue("first_name", teacher.first_name);
                setFieldValue("last_name", teacher.last_name);
                setFieldValue("cpf", teacher.cpf);
                setFieldValue("rg", teacher.rg);
                setFieldValue("date_of_birth", teacher.date_of_birth);
                setFieldValue("gender", teacher.gender);

                // Professional Data
                setFieldValue("registration_number", teacher.registration_number);
                setFieldValue("education_level", teacher.education_level);
                setFieldValue("degree", teacher.degree);
                setFieldValue("subjects", teacher.subjects);
                setFieldValue("is_coordinator", teacher.is_coordinator ? '1' : '0');
                setFieldValue("coordinator_area", teacher.coordinator_area); // CORRIGIDO

                // Show/hide coordinator area field
                const coordinatorField = modal.querySelector("#coordinator-area-field");
                if (coordinatorField) {
                    coordinatorField.style.display = teacher.is_coordinator ? 'block' : 'none';
                }

                // Contract Data
                setFieldValue("contract_type", teacher.contract_type);
                setFieldValue("hire_date", teacher.hire_date);
                setFieldValue("workload", teacher.workload);
                setFieldValue("salary", teacher.salary);
                
                // Note: Files (photo, curriculum) cannot be set via JavaScript
                // Show existing files if needed
                if (teacher.photo) {
                    console.log('Teacher has photo:', teacher.photo);
                }
                if (teacher.curriculum) {
                    console.log('Teacher has curriculum:', teacher.curriculum);
                }

                // Contact Data
                setFieldValue("email", teacher.email);
                setFieldValue("phone", teacher.phone);

                // Address Data
                setFieldValue("address", teacher.address);
                setFieldValue("address_number", teacher.address_number);
                setFieldValue("complement", teacher.complement);
                setFieldValue("neighborhood", teacher.neighborhood);
                setFieldValue("zip_code", teacher.zip_code);
                setFieldValue("city", teacher.city);
                setFieldValue("state", teacher.state);

                console.log('All fields populated successfully');
            })
            .catch(error => {
                console.error('Error loading teacher:', error);
                alert('Erro ao carregar dados: ' + error.message);
            });

    } else {
        // CREATE MODE
        console.log('Create mode - clearing form');
        if (modalTitle) modalTitle.textContent = 'Novo Professor';
        form.reset();
        
        const teacherIdField = modal.querySelector("#teacher_id");
        if (teacherIdField) teacherIdField.value = '';
        
        // Hide coordinator area field by default
        const coordinatorField = modal.querySelector("#coordinator-area-field");
        if (coordinatorField) coordinatorField.style.display = 'none';
    }
}

// ============================================
// TOGGLE COORDINATOR AREA FIELD
// ============================================
document.addEventListener('DOMContentLoaded', function() {
    const isCoordinatorSelect = document.getElementById('is_coordinator');
    const coordinatorAreaField = document.getElementById('coordinator-area-field');
    
    if (isCoordinatorSelect && coordinatorAreaField) {
        isCoordinatorSelect.addEventListener('change', function() {
            coordinatorAreaField.style.display = this.value === '1' ? 'block' : 'none';
        });
    }
});


/* CLOSE CLICK OUTSIDE */
document.querySelectorAll('.simple-modal-overlay').forEach(modal => {
    modal.addEventListener('click', e => {
        if (e.target === modal) {
            modal.classList.remove('active');
        }
    });
});
