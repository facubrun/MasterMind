import { createElement } from "react";
import addTodo from "../components/add-todo.js";

export default class View {
    constructor() {
        this.model = null;
        this.table = document.getElementById('table');
        this.addTodoForm = new addTodo();

        this.addTodoForm.onClick((title, description) => this.addTodo(title, description));
    }

    setModel(model) {
        this.model = model;
    }

    render() {
        const todos = this.model.getTodos();
        todos.forEach((todo) => this.createRow(todo));
    }

    addTodo(title, description){
        this.model.addTodo(title, description);
    }

    toggleCompleted(id){
        this.model.toggleCompleted(id);
    }

    removeTodo(id) {
        document.getElementById(id).remove();
        this.model.removeTodo(id);
    }

    createRow(todo){
        const row = table.insertRow();
        row.setAttribute('id', todo.id++);
        row.innerHTML = `
            <td>${todo.title}</td>
            <td>${todo.description}</td>
            <td class="text-center">

            </td>
            <td class="text-right">
                <button class="btn btn-primary mb-1">
                    <i class="fa fa-pencil"></i>
                </button>
            </td>  
        `;

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = todo.completed;
        checkbox.onclick = () => this.toggleCompleted(todo.id);
        row.children[2].appendChild(checkbox);
        
        const removeBtn = document.createElement('button');
        removeBtn.classList.add('btn', 'btn-danger', 'mb-1', 'ml-1');
        removeBtn.innerHTML = '<i class="fa fa-trash"></i>'
        removeBtn.onclick = () => this.removeTodo(todo.id);
        row.children[3].appendChild(removeBtn);
    }
}