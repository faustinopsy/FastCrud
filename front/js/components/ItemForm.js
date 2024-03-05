class ItemForm {
    constructor(fetchService, renderCallback) {
        this.fetchService = fetchService;
        this.renderApp = renderCallback;
    }

    render() {
        return `
            <form id="addItemForm">
                Nome: <input type="text" id="name"><br>
                Descrição: <input type="text" id="description"><br>
                Preço: <input type="number" step="0.01" id="price"><br>
                Em oferta: <input type="checkbox" id="on_offer"><br>
                <button type="submit">Adicionar Item</button>
            </form>
        `;
    }

    afterRender() {
        document.getElementById('addItemForm').addEventListener('submit', (e) => this.addItem(e));
    }
    async addItem(event) {
        event.preventDefault();
        const name = document.getElementById('name').value;
        const description = document.getElementById('description').value;
        const price = document.getElementById('price').value;
        const onOffer = document.getElementById('on_offer').checked;
        if(!name || !description || !price){
            alert('Campos vazios');
        }
        await this.fetchService.fetch('/items/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, description, price, on_offer: onOffer }),
        });

        alert('Item adicionado com sucesso.');
        this.renderApp('itemsList', render);
    }
}
export default ItemForm;