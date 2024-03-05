import FetchService  from './components/FetchService.js';
import ItemForm from './components/ItemForm.js';
import UpdateItemForm  from './components/UpdateItemForm.js';

class App {
    constructor(apiBaseUrl) {
        this.apiBaseUrl = apiBaseUrl;
        this.appElement = document.getElementById('app');
        this.fetchService = new FetchService(this.apiBaseUrl);
        this.initApp();
    }

    initApp() {
        this.itemForm = new ItemForm(this.fetchService, () => this.fetchItems());
        this.updateItemForm = new UpdateItemForm(this.fetchService, () => this.fetchItems());
        this.appElement.innerHTML = `
        <div class="panel">
            <h1>Gerenciador de Itens</h1>
            <div id="itemForm"></div>
            <button id="fetchItemsButton">Buscar Todos os Itens</button>
            <div id="itemsList"></div>
            <div id="updateItemForm"></div>
        </div>
        `;

        this.render('itemForm', this.itemForm.render());
        this.render('updateItemForm', this.updateItemForm.render());
        this.itemForm.afterRender();
        this.updateItemForm.afterRender();
        this.afterRender();
    }
    async fetchItems() {
        const response = await fetch(`${this.apiBaseUrl}/items/`);
        const items = await response.json();
        let itemsHtml = '<h2>Itens Disponíveis</h2><div class="panel">';
        items.forEach((item) => {
            itemsHtml += `<div class="item" data-id="${item.id}">
                ${item.id} - ${item.name} - ${item.description} - $${item.price} - On Offer: ${item.on_offer ? 'Yes' : 'No'}
                <button class="delete-button" data-id="${item.id}">Deletar</button></div>`;
        });
        itemsHtml += '</div>';
        this.render('itemsList', itemsHtml);

        items.forEach((item) => {
            document.querySelector(`.delete-button[data-id='${item.id}']`).addEventListener('click', (e) => {
                e.stopPropagation();
                this.updateItemForm.deleteItem(item.id);
            });
            document.querySelector(`.item[data-id='${item.id}']`).addEventListener('click', () => {
                this.openUpdateModal(item);
            });
           
        });
    }
    
    fillUpdateForm(item) {
        document.getElementById('updateId').value = item.id;
        document.getElementById('updateName').value = item.name;
        document.getElementById('updateDescription').value = item.description;
        document.getElementById('updatePrice').value = item.price;
        document.getElementById('updateOnOffer').checked = item.on_offer;
    }
    openUpdateModal(item) {
        this.fillUpdateForm(item);
        const modal = document.getElementById('updateItemModal');
        modal.style.display = 'block';
    }
    
    render(elementId, html) {
        const element = document.getElementById(elementId);
        if (element) {
            element.innerHTML = html;
        }
    }
    afterRender() {
        document.getElementById('fetchItemsButton').addEventListener('click', () => this.fetchItems());
    }

   
}

const apiBaseUrl = 'http://127.0.0.1:8000'; 
const itemManager = new App(apiBaseUrl);
