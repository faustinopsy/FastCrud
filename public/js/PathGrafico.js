export default class PathGrafico {
    constructor() {
        this.graficoPath = ''
        this.createGraficoPath();
    }
    createGraficoPath() {
        const configPath = {
            type: 'bar',
            data: {
                labels: [],
                datasets: [{
                    label: 'Contagem por Rota',
                    data: [],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        };
       
    this.graficoPath = new Chart(document.getElementById('graficoPath'), configPath);
    }
    atualizaGraficoPath() {
        const sortedData = Object.entries(pathTotal).sort((a, b) => b[1] - a[1]);
        const labels = sortedData.map(([path, count]) => path);
        const data = sortedData.map(([path, count]) => count);
        if (this.graficoMethod) {
        this.graficoPath.data.labels = labels;
        this.graficoPath.data.datasets[0].data = data;
        this.graficoPath.update();
        } else {
            console.error('O gráfico não está definido. Certifique-se de inicializá-lo corretamente.');
        }
    }
    renderGrafico(pathTotal) {
        const sortedData = Object.entries(pathTotal).sort((a, b) => b[1] - a[1]);
        const labels = sortedData.map(([path, count]) => path);
        const data = sortedData.map(([path, count]) => count);
        this.graficoPath.data.labels = labels;
        this.graficoPath.data.datasets[0].data = pathTotal;
        this.graficoPath.update();
    }
}


