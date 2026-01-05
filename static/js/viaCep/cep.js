document.addEventListener('DOMContentLoaded', function() {
    // Function to search for ZIP code
    function setupCepAutocomplete() {
        const zipCodeInput = document.getElementById('zip_code');
        const loading = document.getElementById('cep-loading');
        const error = document.getElementById('cep-error');
        
        // Checks if the elements exist (important for modals)
        if (!zipCodeInput) return;
        
        // Remove old listeners to avoid duplication
        const newZipCodeInput = zipCodeInput.cloneNode(true);
        zipCodeInput.parentNode.replaceChild(newZipCodeInput, zipCodeInput);
        
        // Format CEP while typing
        newZipCodeInput.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            
            if (value.length > 5) {
                value = value.slice(0, 5) + '-' + value.slice(5, 8);
            }
            
            e.target.value = value;
        });
        
        // Looks up the ZIP code when it reaches 8 digits
        newZipCodeInput.addEventListener('blur', function() {
            const cep = this.value.replace(/\D/g, '');
            
            if (cep.length !== 8) {
                return;
            }
            
            // show loading
            if (loading) loading.style.display = 'block';
            if (error) error.style.display = 'none';
            
            // Search in ViaCEP API
            fetch(`https://viacep.com.br/ws/${cep}/json/`)
                .then(response => response.json())
                .then(data => {
                    if (loading) loading.style.display = 'none';
                    
                    if (data.erro) {
                        if (error) error.style.display = 'block';
                        return;
                    }
                    
                    // Fills in the fields
                    const addressInput = document.getElementById('address');
                    const neighborhoodInput = document.getElementById('neighborhood');
                    const cityInput = document.getElementById('city');
                    const stateInput = document.getElementById('state');
                    
                    if (addressInput) addressInput.value = data.logradouro || '';
                    if (neighborhoodInput) neighborhoodInput.value = data.bairro || '';
                    if (cityInput) cityInput.value = data.localidade || '';
                    if (stateInput) stateInput.value = data.uf || '';
                    
                    // Focus on the number field
                    const numberInput = document.getElementById('address_number');
                    if (numberInput) numberInput.focus();
                })
                .catch(err => {
                    if (loading) loading.style.display = 'none';
                    if (error) error.style.display = 'block';
                    console.error('Erro ao buscar CEP:', err);
                });
        });
    }
    
    // Initializes when the page loads
    setupCepAutocomplete();
    
    // Re-initialize when the modal is opened (if you have a modal open event)
    const modalTeacher = document.getElementById('modal-teacher');
    if (modalTeacher) {
        // Observes when the modal becomes visible
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.target.classList.contains('active')) {
                    setupCepAutocomplete();
                }
            });
        });
        
        observer.observe(modalTeacher, {
            attributes: true,
            attributeFilter: ['class']
        });
    }
});