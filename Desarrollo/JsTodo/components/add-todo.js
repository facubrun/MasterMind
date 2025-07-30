import Alert from "./alert.js";

export default class addTodo {
    constructor () {
        this.btn = document.getElementById('add');
        this.title = document.getElementById('title');
        this.description = document.getElementById('description');
        this.alert = new Alert();
    }

    onClick(callback) {
        this.btn.onclick = () => {
            if (title.value === '' || description.value === ''){ // === compara tipo ademas del valor
                this.alert.show('Title and description are required');
            } else {
                this.alert.hide();
                callback(this.title.value, this.description.value);
            }
        } 
    }
}