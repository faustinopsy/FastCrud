class UpdateItemForm {
    constructor(fetchService, renderCallback) {
        this.fetchService = fetchService;
        this.renderApp = renderCallback;
    }

    render() {
        return `
        <div id="updateItemModal" class="modal">
        <div class="modal-content"><div class="close"> X </div>
            <h4>Atualizar Item</h4>
            <div class="input-field">
                <label for="updateId">ID para atualizar</label>
                <input type="text" id="updateId" class="validate">
            </div>
            <div class="input-field">
                <label for="updateName">Nome</label>
                <input type="text" id="updateName" class="validate">
            </div>
            <div class="input-field">
                <label for="updateDescription">Descrição</label>
                <input type="text" id="updateDescription" class="validate">
            </div>
            <div class="input-field">
                <label for="updatePrice">Preço</label>
                <input type="number" id="updatePrice" step="0.01" class="validate">
            </div>
            <div class="input-field">
                <label>
                    <label for="updateOnOffer">Oferta</label>
                    <input type="checkbox" id="updateOnOffer" />
                </label>
            </div>
            <div class="modal-footer">
                <button id="updateButton" class="btn">Atualizar Item</button>
            </div>
        </div>
    </div>
    
        `;
    }
    closeModal(){
        const modal = document.getElementById('updateItemModal');
        modal.style.display = 'none';
    }
    afterRender() {   
        document.getElementById('updateButton').addEventListener('click', () => this.updateItem());
        document.querySelector('.close').addEventListener('click', () => this.closeModal());
    }

    async updateItem() {
        const id = document.getElementById('updateId').value;
        const name = document.getElementById('updateName').value;
        const description = document.getElementById('updateDescription').value;
        const price = document.getElementById('updatePrice').value;
        const onOffer = document.getElementById('updateOnOffer').checked;

        await this.fetchService.fetch(`/items/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, description, price, on_offer: onOffer }),
        });
        
        alert('Item atualizado com sucesso.');
        this.renderApp();
    }

    async deleteItem(id) {
        await this.fetchService.fetch(`/items/${id}`, {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' },
        });

        alert('Item deletado com sucesso.');
        this.renderApp();
    }
}
export default UpdateItemForm;