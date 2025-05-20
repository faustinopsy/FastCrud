export default class UpdateUserForm {
    constructor(fetchService, renderCallback) {
        this.fetchService = fetchService;
        this.renderApp = renderCallback;
        this.token = ""
    }

    render() {
        return `
        <div id="updateUserModal" class="modal">
        <div class="modal-content"><div class="close"> X </div>
            <h4>Atualizar Usuário</h4>
            <div class="input-field" hidden>
                <label for="updateId">ID para atualizar</label>
                <input type="text" id="updateId" class="validate">
            </div>
            <div class="input-field">
                <label for="updateNome">Nome</label>
                <input type="text" id="updateNome" class="validate">
            </div>
            <div class="input-field">
                <label for="updateEmail">Email</label>
                <input type="email" id="updateEmail" class="validate">
            </div>
            <div class="input-field">
              <select name="tipo" id="tipo">
                <option value="admin">Admin</option>
                <option value="user">User</option>
            </select>
            </div>
            <div class="input-field">
                <label for="updateSenha">Senha</label>
                <input type="password" id="updateSenha" class="validate">
            </div>
            <div class="modal-footer">
                <button id="updateButton" class="btn">Atualizar Usuário</button>
            </div>
        </div>
    </div>
        `;
    }

    closeModal() {
        const modal = document.getElementById('updateUserModal');
        modal.style.display = 'none';
    }

    afterRender() {
        this.token = localStorage.getItem("token") || "";
        document.getElementById('updateButton').addEventListener('click', () => this.updateUser());
        document.querySelector('.close').addEventListener('click', () => this.closeModal());
    }

    async updateUser() {
        const id = document.getElementById('updateId').value;
        const nome = document.getElementById('updateSenha').value;
        const email = document.getElementById('updateEmail').value;
        const senha = document.getElementById('updateSenha').value;
        const tipo_usuario = document.getElementById('tipo').value;
        const token = localStorage.getItem("token");
        await this.fetchService.fetch(`/usuarios/${email}`, {
            method: 'PUT',
            headers: { 
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ nome, email, senha, tipo_usuario }),
        });

        alert('Usuário atualizado com sucesso.');
        this.renderApp();
    }

    async deleteUser(email) {
        await this.fetchService.fetch(`/usuarios/${email}`, {
            method: 'DELETE',
            headers: { 
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${this.token}` 
            },
        });

        alert('Usuário deletado com sucesso.');
        this.renderApp();
    }
}
