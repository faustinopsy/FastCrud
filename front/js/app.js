import FetchService from './components/FetchService.js';
import UserForm from './components/UserForm.js';
import UpdateUserForm from './components/UpdateUserForm.js';
import LoginForm from './components/LoginForm.js';
import { decodeJwtPayload } from './utils/jwtUtils.js';
class App {
    constructor(apiBaseUrl) {
        this.apiBaseUrl = apiBaseUrl;
        this.appElement = document.getElementById('app');
        this.fetchService = new FetchService(this.apiBaseUrl);
        this.token = ""
        this.admin = false;
    }

   async initApp() {
        this.token = localStorage.getItem("token") || "";
        if (!this.token) {
            location.hash = '#login';
            this.verificaRota()
            return;
        }
        this.currentDecodedStudent = await decodeJwtPayload(this.token);
        this.admin = this.currentDecodedStudent.tipo_usuario === "admin";
        this.verificaRota()
    }

    verificaRota(){
        window.addEventListener('hashchange', () => this.renderBasedOnHash());
        this.renderBasedOnHash();
    }
    renderBasedOnHash() {
        const hash = location.hash;
        if (hash === '#login') {
            this.renderLogin();
        } else {
            this.renderUserManagement();
        }
    }

    renderLogin() {
        this.appElement.innerHTML = `
            <div class="panel">
                <h1>Login</h1>
                <div id="loginForm"></div>
            </div>
        `;
        this.loginForm = new LoginForm(this.fetchService);
        this.render('loginForm', this.loginForm.render());
        this.loginForm.afterRender();
    }

    renderUserManagement() {
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
        const response = await this.fetchService.fetch(`/usuarios`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${this.token}`
            }
        });
        const users = response;
        let usersHtml = `<h2>Usuários Disponíveis</h2>
                         <table>
                            <thead>
                                <tr>
                                    <th style="text-align: center;">ID</th>
                                    <th style="text-align: center;">Nome</th>
                                    <th style="text-align: center;">Email</th>
                                    <th style="text-align: center;">Ações</th>
                                </tr>
                            </thead>
                            <tbody>`;

        users.forEach((user) => {
            usersHtml += `<tr data-id="${user.id}">
                            <td>${user.id}</td>
                            <td>${user.nome}</td>
                            <td>${user.email}</td>
                            <td style="text-align: center;">`;
            if (this.admin) {
                usersHtml += `<button class="delete-button" data-id="${user.id}">Deletar</button>
                            </td>
                          </tr>`;
            }
        });

        usersHtml += `   </tbody>
                         </table>`;
        this.render('usersList', usersHtml);

        users.forEach((user) => {
            const deleteButton = document.querySelector(`.delete-button[data-id='${user.id}']`);
            if (deleteButton) {
                 deleteButton.addEventListener('click', (e) => {
                    e.stopPropagation();
                    this.updateUserForm.deleteUser(user.email);
                 });
            }

            const userRow = document.querySelector(`tr[data-id='${user.id}']`);
             if (userRow) {
                 userRow.addEventListener('click', () => {
                    this.openUpdateModal(user);
                 });
             }
        });
    }

    fillUpdateForm(user) {
        document.getElementById('updateId').value = user.id;
        document.getElementById('updateNome').value = user.nome;
        document.getElementById('updateEmail').value = user.email;
        document.getElementById('updateSenha').value = '';
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
await userManager.initApp();