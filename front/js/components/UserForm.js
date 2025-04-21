export default class UserForm {
    constructor(fetchService, renderCallback) {
        this.fetchService = fetchService;
        this.renderApp = renderCallback;
    }

    render() {
        return `
            <form id="addUserForm">
                Nome: <input type="text" id="nome"><br>
                Email: <input type="email" id="email"><br>
                Senha: <input type="password" id="senha"><br>
                <button type="submit">Adicionar Usuário</button>
            </form>
        `;
    }

    afterRender() {
        document.getElementById('addUserForm').addEventListener('submit', (e) => this.addUser(e));
    }

    async addUser(event) {
        event.preventDefault();
        const nome = document.getElementById('nome').value;
        const email = document.getElementById('email').value;
        const senha = document.getElementById('senha').value;
        if (!nome || !email || !senha) {
            alert('Campos vazios');
            return;
        }
        await this.fetchService.fetch('/usuarios/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ nome, email, senha }),
        });

        alert('Usuário adicionado com sucesso.');
        this.renderApp('usersList', this.render);
    }
}
