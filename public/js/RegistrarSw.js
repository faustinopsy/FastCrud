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
    }
}