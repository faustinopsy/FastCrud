class FetchService {
    constructor(apiBaseUrl) {
        this.apiBaseUrl = apiBaseUrl;
    }

    async fetch(url, options = {}) {
        let response;

        try {
            response = await fetch(`${this.apiBaseUrl}${url}`, options);
        } catch (networkError) {
            console.error('Erro de rede:', networkError);
            alert('Erro de rede: Verifique sua conexão.');
            return null;
        }

        
        if (!response.ok) {
            let message = '';

            switch (response.status) {
                case 400:
                    message = 'Requisição inválida (400).';
                    break;
                case 401:
                    message = 'Não autorizado (401).';
                    location.hash = '#login'
                    break;
                case 403:
                    message = 'Acesso proibido (403).';
                    break;
                case 404:
                    message = 'Recurso não encontrado (404).';
                    break;
                case 500:
                    message = 'Erro interno do servidor (500).';
                    break;
                default:
                    message = `Erro inesperado (${response.status}).`;
            }

            console.warn('Erro de status:', response.status);
            alert(message);
            return null;
        }

        if (response.status === 204) {
            return null;
        }

        try {
            return await response.json();
        } catch (jsonError) {
            console.error('Erro ao interpretar JSON:', jsonError);
            alert('Erro ao interpretar resposta do servidor.');
            return null;
        }
    }
}

export default FetchService;
