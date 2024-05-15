export default class RegistarSW {
  constructor(){
      this.init()
      
  }
  async init(){
      if ('serviceWorker' in navigator) {
          try {
            const registration = await navigator.serviceWorker.register(
              'sw.js',
              {
                scope: './',
              }
            );
            if (registration.installing) {
              console.log('Service worker instalando');
            } else if (registration.waiting) {
              console.log('Service worker instalado');
            } else if (registration.active) {
              console.log('Service worker ativo');
            }
          } catch (error) {
            console.error(`Registration falha em ${error}`);
          }
        }
        await this.render()
        this.afterRender()
  }
  async pushPermission() {
    const permissionResult = await Notification.requestPermission();
    if (permissionResult !== 'granted') {
        console.warn('Permissão de notificação não concedida.');
    }
  }
  async render() {
    const btn = document.createElement('button')
    btn.textContent = "notifique"
    btn.className = "w3-button"
    btn.id = "btnnotifica"

    const notifica = document.createElement('button')
    notifica.textContent ="Autorizar notificações"
    notifica.className = "w3-button"
    notifica.id = "notificationBtn"
    document.body.appendChild(notifica);
    document.body.appendChild(btn);
    
}
afterRender(){
        const btn = document.getElementById('btnnotifica')
        btn.addEventListener('click', () => this.notificarCliente());
        const notificationBtn = document.getElementById('notificationBtn')
        notificationBtn.addEventListener('click', () => this.permitirNotificacao());
}
async notificarCliente() {
  const title = prompt("Quall o Titulo?");
  const img = './img/notifica.webp';
  const text = prompt("Qual a mensagem?");

  if (!("Notification" in window)) {
      alert("This browser does not support desktop notification");
  } else {
      this.permission = Notification.permission;
      if (this.permission === "granted") {
          this.mostrarNotificacao(title, text, img);
      } else if (this.permission !== "denied") {
          this.permission = await Notification.requestPermission();
          console.log(permission);
          if (this.permission === "granted") {
              console.log(this.permission);
              this.mostrarNotificacao(title, text, img);
          }
      }
  }
}

mostrarNotificacao(title, text, img) {
    const options = { body: text, icon: img };
    //const notification = new Notification(title, options);
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.ready.then(registration => {
            registration.showNotification(title, options);
        });
    }
}
permitirNotificacao() {
  if (!Reflect.has(window, 'Notification')) {
    console.log('This browser does not support notifications.');
  } else {
    if (this.checkNotificationPromise()) {
      Notification.requestPermission().then(this.pedirPermissaoNotificar);
    } else {
      Notification.requestPermission(this.pedirPermissaoNotificar);
    }
  }
};
checkNotificationPromise() {
  try {
    Notification.requestPermission().then();
  } catch(e) {
    return false;
  }
  return true;
};
pedirPermissaoNotificar(permission) {
  const notificationBtn = document.getElementById('notificationBtn')
  if (!Reflect.has(Notification, 'permission')) {
    Notification.permission = this.permission;
  }
  if (Notification.permission === 'denied' || Notification.permission === 'default') {
    notificationBtn.style.display = 'block';
  } else {
    notificationBtn.style.display = 'none';
  }
};
}