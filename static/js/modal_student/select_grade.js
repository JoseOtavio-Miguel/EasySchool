const gradeLevelSelect = document.getElementById('grade_level');
const specificGradeSelect = document.getElementById('specific_grade');

const gradeOptions = {
    INFANTIL: [
        { value: 'PRE_ESCOLA', text: 'Pré-Escola' }
    ],
    FUNDAMENTAL1: [
        { value: '1ANO', text: '1º Ano' },
        { value: '2ANO', text: '2º Ano' },
        { value: '3ANO', text: '3º Ano' },
        { value: '4ANO', text: '4º Ano' },
        { value: '5ANO', text: '5º Ano' },
    ],
    FUNDAMENTAL2: [
        { value: '6ANO', text: '6º Ano' },
        { value: '7ANO', text: '7º Ano' },
        { value: '8ANO', text: '8º Ano' },
        { value: '9ANO', text: '9º Ano' },
    ],
    MEDIO: [
        { value: '1MEDIO', text: '1º Ano EM' },
        { value: '2MEDIO', text: '2º Ano EM' },
        { value: '3MEDIO', text: '3º Ano EM' },
    ],
    SUPERIOR: [
        { value: 'GRADUACAO', text: 'Graduação' },
        { value: 'POS', text: 'Pós-Graduação' },
    ]
};

gradeLevelSelect.addEventListener('change', function () {
    const selectedLevel = this.value;

    specificGradeSelect.innerHTML = '<option value="">Selecione</option>';

    if(!gradeOptions[selectedLevel]) return;

    gradeOptions[selectedLevel].forEach(option => {
        const opt = document.createElement('option');
        opt.value = option.value;
        opt.textContent = option.text;
        specificGradeSelect.appendChild(opt);
    });
});