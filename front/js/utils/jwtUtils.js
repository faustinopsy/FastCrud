export function decodeJwtPayload(token) {
    if (!token || typeof token !== 'string') {
        console.error('decodeJwtPayload: Token inválido ou não fornecido.');
        return null;
    }
    try {
        const parts = token.split('.');
        if (parts.length !== 3) {
            throw new Error('Token JWT não possui o formato esperado (três partes).');
        }
        const base64Url = parts[1];
        const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
        const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
            return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
        }).join(''));
        
        return JSON.parse(jsonPayload);
    } catch (e) {
        console.error("Falha ao decodificar o payload do JWT:", e);
        return null;
    }
}