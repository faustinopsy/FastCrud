export default class UpdateUserForm {
    constructor(fetchService, renderCallback) {
        this.fetchService = fetchService;
        this.renderApp = renderCallback;
    }

    render() {
        return `
        <div id="updateUserModal" class="modal">
        <div class="modal-content"><div class="close"> X </div>
            <h4>Atualizar Usuário</h4>
            <div class="input-field">
                <label for="updateId">ID para atualizar</label>
                <input type="text" id="updateId" class="validate">
            </div>
            <div class="input-field">
                <label for="updateName">Nome</label>
                <input type="text" id="updateName" class="validate">
            </div>
            <div class="input-field">
                <label for="updateEmail">Email</label>
                <input type="email" id="updateEmail" class="validate">
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
        document.getElementById('updateButton').addEventListener('click', () => this.updateUser());
        document.querySelector('.close').addEventListener('click', () => this.closeModal());
    }

    async updateUser() {
        const id = document.getElementById('updateId').value;
        const nome = document.getElementById('updateName').value;
        const email = document.getElementById('updateEmail').value;
        const senha = document.getElementById('updateSenha').value;

        await this.fetchService.fetch(`/usuarios/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ nome, email, senha }),
        });

        alert('Usuário atualizado com sucesso.');
        this.renderApp();
    }

    async deleteUser(id) {
        await this.fetchService.fetch(`/usuarios/${id}`, {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' },
        });

        alert('Usuário deletado com sucesso.');
        this.renderApp();
    }
}
