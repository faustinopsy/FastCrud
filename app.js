class App {
    constructor(apiBaseUrl) {
        this.apiBaseUrl = apiBaseUrl;
        this.appElement = document.getElementById('app');
        this.initApp();
    }

    initApp() {
        this.appElement.innerHTML = `
            <h1>Gerenciador de Itens</h1>
            <div id="itemForm"></div>
            <button id="fetchItemsButton">Buscar Todos os Itens</button>
            <div id="itemsList"></div>
            <div id="updateItemForm"></div>
        `;
        this.render('itemForm', this.getAddItemFormHtml());
        this.render('updateItemForm', this.getUpdateItemFormHtml());
        this.initializeEventListeners();
    }

    getAddItemFormHtml() {
        return `
            <h2>Adicionar Item</h2>
            <form id="addItemForm">
                Nome: <input type="text" id="name"><br>
                Descrição: <input type="text" id="description"><br>
                Preço: <input type="number" step="0.01" id="price"><br>
                Em oferta: <input type="checkbox" id="on_offer"><br>
                <button type="submit">Adicionar Item</button>
            </form>
        `;
    }

    getUpdateItemFormHtml() {
        return `
            <h2>Atualizar/Deletar Item</h2>
            ID para atualizar/deletar: <input type="text" id="updateId"><br>
            Nome: <input type="text" id="updateName"><br>
            Descrição: <input type="text" id="updateDescription"><br>
            Preço: <input type="number" step="0.01" id="updatePrice"><br>
            Em oferta: <input type="checkbox" id="updateOnOffer"><br>
            <button id="updateButton">Atualizar Item</button>
            <button id="deleteButton">Deletar Item</button>
        `;
    }

    render(elementId, html) {
        const element = document.getElementById(elementId);
        if (element) {
            element.innerHTML = html;
        }
    }

    async fetchItems() {
        const response = await fetch(`${this.apiBaseUrl}/items/`);
        const items = await response.json();
        let itemsHtml = '<h2>Itens Disponíveis</h2>';
        items.forEach(item => {
            itemsHtml += `<div>${item.id} - ${item.name} - ${item.description} - $${item.price} - On Offer: ${item.on_offer}
            <button onclick="itemManager.deleteItem('${item.id}')">Deletar</button><br></div>`;
        });
        this.render('itemsList', itemsHtml);
    }

    async addItem(event) {
        event.preventDefault();
        const name = document.getElementById('name').value;
        const description = document.getElementById('description').value;
        const price = document.getElementById('price').value;
        const onOffer = document.getElementById('on_offer').checked;
        
        await fetch(`${this.apiBaseUrl}/items/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, description, price, on_offer: onOffer }),
        });

        alert('Item adicionado com sucesso.');
        this.fetchItems();
    }

    async updateItem() {
        const id = document.getElementById('updateId').value;
        const name = document.getElementById('updateName').value;
        const description = document.getElementById('updateDescription').value;
        const price = document.getElementById('updatePrice').value;
        const onOffer = document.getElementById('updateOnOffer').checked;
        
        await fetch(`${this.apiBaseUrl}/items/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, description, price, on_offer: onOffer }),
        });

        alert('Item atualizado com sucesso.');
        this.fetchItems();
    }

    async deleteItem(id) {
        await fetch(`${this.apiBaseUrl}/items/${id}`, {
            method: 'DELETE',
        });

        alert('Item deletado com sucesso.');
        this.fetchItems();
    }

    initializeEventListeners() {
        document.getElementById('fetchItemsButton').addEventListener('click', () => this.fetchItems());
        document.getElementById('addItemForm').addEventListener('submit', (e) => this.addItem(e));
        document.getElementById('updateButton').addEventListener('click', () => this.updateItem());
        document.getElementById('deleteButton').addEventListener('click', () => this.deleteItem());
    }
}

const apiBaseUrl = 'http://127.0.0.1:8000'; 
const itemManager = new App(apiBaseUrl);
