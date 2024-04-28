export default class MethodGrafico {
    constructor() {
        this.graficoMethod = '';
        this.createGraficoMethod();
    }

    createGraficoMethod() {
        const configMethod = {
            type: 'bar',
            data: {
            labels: ['Quantidade de métodos'],
            datasets: [{
                label: 'GET',
                data: [],
                backgroundColor: [
                    'rgba(75, 192, 192, 0.2)'
                ],
                borderColor: [
                    'rgba(75, 192, 192, 1)'
                ],
                borderWidth: 1
            },{
                label: 'POST',
                data: [],
                backgroundColor: [
                    'rgba(255, 206, 86, 0.2)',
                ],
                borderColor: [
                    'rgba(255, 206, 86, 1)',
                ],
                borderWidth: 1
            },
            {
                label: 'PUT',
                data: [],
                backgroundColor: [
                    'rgba(75, 192, 192, 0.2)'
                ],
                borderColor: [
                    'rgba(75, 192, 192, 1)'
                ],
                borderWidth: 1
            },
            {
                label: 'DELETE',
                data: [],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                ],
                borderWidth: 1
            }],
        },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        };
        if (this.graficoMethod) {
            this.graficoMethod.destroy();
            this.graficoMethod = null;
        }
        this.graficoMethod = new Chart(document.getElementById('graficoMethod'), configMethod);
     
    }

    renderGrafico(getTotal, postTotal, putTotal, deleteTotal) {
        if (this.graficoMethod) {
            this.graficoMethod.data.datasets[0].data = [getTotal];
            this.graficoMethod.data.datasets[1].data = [postTotal];
            this.graficoMethod.data.datasets[2].data = [putTotal];
            this.graficoMethod.data.datasets[3].data = [deleteTotal];
            this.graficoMethod.update();
        } else {
            console.error('O gráfico não está definido. Certifique-se de inicializá-lo corretamente.');
        }
    }
}

