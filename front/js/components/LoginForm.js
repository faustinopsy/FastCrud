export default class LoginForm {
    constructor(fetchService) {
        this.fetchService = fetchService;
    }

    render() {
        return `
            <form id="loginForm">
                Email: <input type="email" id="loginEmail"><br>
                Senha: <input type="password" id="loginSenha"><br>
                <button type="submit">Login</button>
            </form>
        `;
    }

    afterRender() {
        document.getElementById('loginForm').addEventListener('submit', (e) => this.login(e));
    }

    async login(event) {
        event.preventDefault();
        const email = document.getElementById('loginEmail').value;
        const senha = document.getElementById('loginSenha').value;
        
        if (!email || !senha) {
            alert('Por favor, preencha todos os campos');
            return;
        }

        try {
            const response = await this.fetchService.fetch('/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, senha })
            });
            
            if (response) {
                localStorage.setItem('token', response.token);
                alert('Login realizado com sucesso!');
            } else {
                alert('Erro no login: ' + (response.message || 'Credenciais inválidas'));
            }
        } catch (error) {
            alert('Erro ao tentar fazer login: ' + error.message);
        }
    }
}