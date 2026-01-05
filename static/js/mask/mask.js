
document.addEventListener("DOMContentLoaded", function() {
    const rgInput = document.getElementById("rg");
    const cpfInput = document.getElementById("cpf");
    const zipCodeInput = document.getElementById("zip_code");
    const phoneInput = document.getElementById("phone");

    /* CPF mask */
    cpfInput.addEventListener("input", function(e) {
        let value = e.target.value.replace(/\D/g,  "");  /* Remove any caracters non-numeric from the input */

        if (value.length > 11) {
            value = value.slice(0, 11);
        }

        value = value.replace(/(\d{3})(\d)/, "$1.$2");
        value = value.replace(/(\d{3})(\d)/, "$1.$2");
        value = value.replace(/(\d{3})(\d{1,2})$/, "$1-$2");

        e.target.value = value;
    });


    /* RG mask */
    rgInput.addEventListener("input", function(e) {
        let value = e.target.value.replace(/\D/g,  "");  /* Remove any caracters non-numeric from the input */

        if (value.length > 9) {
            value = value.slice(0, 9);
        }

        value = value.replace(/(\d{2})(\d)/, "$1.$2");
        value = value.replace(/(\d{3})(\d)/, "$1.$2");
        value = value.replace(/(\d{3})(\d{1,2})$/, "$1-$2");

        e.target.value = value;
    });

    /* Phone and Guardian Phone */
    phoneInput.addEventListener("input", function(e) {
        let value = e.target.value.replace(/\D/g, "");
        
    });

    /* Cep mask */
    zipCodeInput.addEventListener("input", function(e) {
        let value = e.target.value.replace(/\D/g, ""); // Remove everything that is not a digit

        if (value.length > 8) {
            value = value.slice(0, 8); // Limit 8 digits
        } 

        // Format CEP '73499-899' (5 digits + hyphen + 3 digits)
        if (value.length > 5) {
            value = value.replace(/(\d{5})(\d)/, "$1-$2");
        }

        e.target.value = value;
    });
});

/* (00) 00000-0000 */
