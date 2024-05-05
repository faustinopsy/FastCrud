export default class LoginForm {
    constructor(url) {
        this.container = document.querySelector('body');
        this.url = url;
    }

    loginForm() {
        
        const modal = document.createElement("div");
        modal.style.position = "fixed";
        modal.style.top = "0";
        modal.style.left = "0";
        modal.style.width = "100%";
        modal.style.height = "100%";
        modal.style.backgroundColor = "rgba(0, 0, 0, 0.5)"; 
        modal.style.backdropFilter= "blur(5px)";
        modal.style.display = "flex";
        modal.style.justifyContent = "center";
        modal.style.alignItems = "center";
        this.container.appendChild(modal);

        const form = document.createElement("form");
        form.style.background = "#fff"; 
        form.style.padding = "20px";
        form.style.borderRadius = "8px";
        form.innerHTML = `
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required><br><br>
            <label for="senha">Senha:</label>
            <input type="password" id="senha" name="senha" required><br><br>
            <button type="submit">Login</button>
        `;
        form.addEventListener("submit", this.logar.bind(this));
        modal.appendChild(form);
    }
    
    async logar(event) {
        event.preventDefault();
        const formData = new FormData(event.target);
        const email = formData.get("email");
        const senha = formData.get("senha");

        try {
            const response = await fetch(`${this.url}/usuarios/login/?email=${encodeURIComponent(email)}&senha=${encodeURIComponent(senha)}`, {
                method: 'POST',
                headers: {
                    'Accept': 'application/json'
                }
            });
            const data = await response.json();
            if (response.ok) {
                sessionStorage.setItem('token', data.token);
                location.reload();
            } else {
                console.error(data.message); 
            }
        } catch (error) {
            console.error("Ocorreu um erro ao realizar o login:", error);
        }
    }
}


