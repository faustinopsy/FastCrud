import LogList from './LogList.js';
import LoginForm from './LoginForm.js'

const token = sessionStorage.getItem('token')
const url = `http://127.0.0.1:8000`



const logList = new LogList(url, token);
const loginForm = new LoginForm(url);
if (!token) {
    loginForm.loginForm();
} else {
    logList.iniciar();
}