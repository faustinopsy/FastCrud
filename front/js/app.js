import FetchService  from './components/FetchService.js';
import UserForm from './components/UserForm.js';
import UpdateUserForm  from './components/UpdateUserForm.js';

class App {
    constructor(apiBaseUrl) {
        this.apiBaseUrl = apiBaseUrl;
        this.appElement = document.getElementById('app');
        this.fetchService = new FetchService(this.apiBaseUrl);
        this.initApp();
    }

    initApp() {
        this.userForm = new UserForm(this.fetchService, () => this.fetchUsers());
        this.updateUserForm = new UpdateUserForm(this.fetchService, () => this.fetchUsers());
        this.appElement.innerHTML = `
        <div class="panel">
            <h1>Gerenciador de Usuários</h1>
            <div id="userForm"></div>
            <button id="fetchUsersButton">Buscar Todos os Usuários</button>
            <div id="usersList"></div>
            <div id="updateUserForm"></div>
        </div>
        `;

        this.render('userForm', this.userForm.render());
        this.render('updateUserForm', this.updateUserForm.render());
        this.userForm.afterRender();
        this.updateUserForm.afterRender();
        this.afterRender();
    }

    async fetchUsers() {
        const response = await fetch(`${this.apiBaseUrl}/usuarios/`);
        const users = await response.json();
        let usersHtml = '<h2>Usuários Disponíveis</h2><div class="panel">';
        users.forEach((user) => {
            usersHtml += `<div class="user" data-id="${user.id}">
                ${user.id} - ${user.name} - ${user.email}
                <button class="delete-button" data-id="${user.id}">Deletar</button></div>`;
        });
        usersHtml += '</div>';
        this.render('usersList', usersHtml);

        users.forEach((user) => {
            document.querySelector(`.delete-button[data-id='${user.id}']`).addEventListener('click', (e) => {
                e.stopPropagation();
                this.updateUserForm.deleteUser(user.id);
            });
            document.querySelector(`.user[data-id='${user.id}']`).addEventListener('click', () => {
                this.openUpdateModal(user);
            });
        });
    }

    fillUpdateForm(user) {
        document.getElementById('updateId').value = user.id;
        document.getElementById('updateName').value = user.name;
        document.getElementById('updateEmail').value = user.email;
        document.getElementById('updatePassword').value = '';
    }

    openUpdateModal(user) {
        this.fillUpdateForm(user);
        const modal = document.getElementById('updateUserModal');
        modal.style.display = 'block';
    }

    render(elementId, html) {
        const element = document.getElementById(elementId);
        if (element) {
            element.innerHTML = html;
        }
    }

    afterRender() {
        document.getElementById('fetchUsersButton').addEventListener('click', () => this.fetchUsers());
    }
}

const apiBaseUrl = 'http://127.0.0.1:8000';
const userManager = new App(apiBaseUrl);