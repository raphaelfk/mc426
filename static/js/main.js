document.getElementById('registrationForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = {
        nome: document.getElementById('nome').value,
        cpf: document.getElementById('cpf').value,
        email: document.getElementById('email').value,
        senha: document.getElementById('senha').value,
        atividade: document.getElementById('atividade').value
    };

    try {
        const response = await fetch('/cadastro', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        const data = await response.json();
        const messageDiv = document.getElementById('message');

        if (response.ok) {
            messageDiv.textContent = data.mensagem;
            document.getElementById('registrationForm').reset();
        } else {
            messageDiv.textContent = data.erro;
            messageDiv.style.color = 'red';
            messageDiv.style.backgroundColor = 'red';
        }
        
        messageDiv.classList.remove('hidden');
        
        // Hide message after 5 seconds
        setTimeout(() => {
            messageDiv.classList.add('hidden');
        }, 5000);
    } catch (error) {
        console.error('Error:', error);
        const messageDiv = document.getElementById('message');
        messageDiv.textContent = 'Erro ao processar a requisição. Tente novamente.';
        messageDiv.style.color = 'red';
        messageDiv.style.backgroundColor = 'red';
        messageDiv.classList.remove('hidden');
    }
}); 