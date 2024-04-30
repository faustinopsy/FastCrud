class HtmlSemantico {
    constructor() {
        
    }

    createElement(tagName, styles, textContent = null) {
        const element = document.createElement(tagName);
        if (styles) {
            Object.entries(styles).forEach(([property, value]) => {
                element.style[property] = value;
            });
        }
        if (textContent) {
            element.textContent = textContent;
        }
        return element;
    }

    dashboardLayout() {
        const header = this.createElement('header', {
            position: 'relative',
            border: 'solid 1px red',
            borderRadius: '20px 20px 0px 0px'
        });
        const h1 = this.createElement('h1', null, 'Dashboard Rotas');
        const logoutButton = this.createElement('button', {
            position: 'absolute',
            top: '-10px',
            right: '-10px',
            margin: '10px',
            borderRadius: '0px 20px 0px 20px',
            borderColor: 'coral',
            cursor: 'pointer'
        }, 'Deslogar');
        logoutButton.id = 'deslogar'
        const main = this.createElement('main', {
            position: 'relative',
            border: 'solid 1px red',
            borderRadius: '20px 20px 0px 0px'
        });
        const article = this.createElement('article', {
            width: '100%',
            maxWidth: '600px',
            margin: '0 auto'
        });
        const detailsSection = this.createElement('section', {
            position: 'relative',
            border: 'solid 1px red',
            borderRadius: '20px 20px 0px 0px'
        });
        const detailhes = this.createElement('details', { cursor: 'pointer' }, 'Ver detalhes');
        const detailsSummary = this.createElement('summary', { cursor: 'pointer' }, 'Ver detalhes');
        const logList = this.createElement('ul');
        logList.id = 'log-list'
        logList.hidden= true
        const totalDiv = this.createElement('div');
        totalDiv.id = 'Total'
        const graphicsSection = this.createElement('section', {
            position: 'relative',
            border: 'solid 1px red',
            borderRadius: '20px 20px 0px 0px'
        });
        const methodChartCanvas = this.createElement('canvas');
        methodChartCanvas.id = 'graficoMethod'
        const pathChartCanvas = this.createElement('canvas');
        pathChartCanvas.id = 'graficoPath'

        detailsSummary.appendChild(logList);
        detailsSummary.appendChild(totalDiv);
        //detailsSection.appendChild(detailsSummary);
        detailhes.appendChild(logList);
        detailhes.appendChild(totalDiv);
        detailsSection.appendChild(detailhes);
        graphicsSection.appendChild(methodChartCanvas);
        graphicsSection.appendChild(pathChartCanvas);
        article.appendChild(detailsSection);
        article.appendChild(graphicsSection);
        main.appendChild(article);
        header.appendChild(h1);
        header.appendChild(logoutButton);
        document.body.appendChild(header);
        document.body.appendChild(main);
    }
}
const html = new HtmlSemantico();
html.dashboardLayout();
