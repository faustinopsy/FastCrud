class FetchService {
    constructor(apiBaseUrl) {
        this.apiBaseUrl = apiBaseUrl;
    }

    async fetch(url, options = {}) {
        const response = await fetch(`${this.apiBaseUrl}${url}`, options);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    }
}
export default FetchService;