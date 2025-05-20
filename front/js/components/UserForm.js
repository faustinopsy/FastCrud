export default class UserForm {
    constructor(fetchService, renderCallback) {
        this.fetchService = fetchService;
        this.renderApp = renderCallback;
    }

    render() {
        return `
             <form id="addUserForm">
            <label for="nome">Nome:</label>
            <input type="text" id="nome">
            <label for="email">Email:</label>
            <input type="email" id="email">
            <label for="tipo">Tipo:</label>
           <select name="tipo" id="tipo">
            <option value="admin">Admin</option>
            <option value="user">User</option>
        </select>
        <label for="senha">Senha:</label>
        <input type="password" id="senha">
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
        const tipo_usuario = document.getElementById('tipo').value;
        if (!nome || !email || !senha) {
            alert('Campos vazios');
            return;
        }
        const resultado = await this.fetchService.fetch('/usuarios/', {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json' 
            },
            body: JSON.stringify({ nome, email, senha,tipo_usuario }),
        });
        alert('Usuário adicionado com sucesso.');
        this.renderApp('usersList', this.render);
    }
}
