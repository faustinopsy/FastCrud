import MethodGrafico from './MethodGrafico.js'
import PathGrafico from './PathGrafico.js'

export default class LogList {
    constructor(url,token) {
        this.methodGrafico = new MethodGrafico();
        this.pathGrafico = new PathGrafico();
        this.getTotal = 0;
        this.postTotal = 0;
        this.putTotal = 0;
        this.deleteTotal = 0;
        this.lista = document.getElementById("log-list");
        this.divsTotal = document.getElementById("Total");
        this.logDisplay = new Set();
        this.methodTotal = {};
        this.pathTotal = {};
        this.last_log_timestamp = null
        this.eventSourceUrl =  `${url}/logs/acessos/stream?token=${token}`;
        

    }
    iniciar(){
        this.eventSource = new EventSource(this.eventSourceUrl);
        this.eventSource.onmessage = (event) => {
            const log = JSON.parse(event.data);
            //if (!this.logDisplay.has(log.data_ini)) {
            if (this.last_log_timestamp === null || log.data_ini > this.last_log_timestamp) {
                const logItem = document.createElement("li");
                logItem.textContent = `${log.id} - ${log.data_ini} - ${log.method} - ${log.path}`;
                this.lista.appendChild(logItem);
                this.logDisplay.add(log.data_ini);
                this.incrementaContagem(this.methodTotal, log.method);
                this.incrementaContagem(this.pathTotal, log.path);
                this.atualizaDisplay();

                switch(log.method) {
                    case 'GET':
                        this.getTotal++;
                        break;
                    case 'POST':
                        this.postTotal++;
                        break;
                    case 'PUT':
                        this.putTotal++;
                        break;
                    case 'DELETE':
                        this.deleteTotal++;
                        break;
                    default:
                        break;
                }
                
                this.methodGrafico.renderGrafico(this.getTotal, this.postTotal, this.putTotal, this.deleteTotal);
                this.pathGrafico.renderGrafico(this.pathTotal);
                this.last_log_timestamp = log.data_ini;
                

            };
        }

    const desloga = document.getElementById('deslogar')
    desloga.addEventListener("click", this.deslogar.bind());
    }
    deslogar() {
        sessionStorage.removeItem('token')
        location.reload();
    }
    limparDados() {
        this.getTotal = 0;
        this.postTotal = 0;
        this.putTotal = 0;
        this.deleteTotal = 0;
        this.pathTotal = {};
    }

    incrementaContagem(contagem, key) {
        if (!contagem[key]) {
            contagem[key] = 1;
        } else {
            contagem[key]++;
        }
    }

    atualizaDisplay() {
        this.divsTotal.innerHTML = "<h3>Total:</h3>";
        this.divsTotal.innerHTML += "<p><strong>Method Total:</strong></p>";
        for (const [method, count] of Object.entries(this.methodTotal)) {
            this.divsTotal.innerHTML += `<p>${method}: ${count}</p>`;
        }
        this.divsTotal.innerHTML += "<p><strong>Path Total:</strong></p>";
        for (const [path, count] of Object.entries(this.pathTotal)) {
            this.divsTotal.innerHTML += `<p>${path}: ${count}</p>`;
        }
    }
}




