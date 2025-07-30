export default class Model {
    constructor() {
        this.view = null;
        this.todos = JSON.parse(localStorage.getItem('todos')); //simulated bd
        if(!this.todos || this.todos.lenght < 1) {
            this.todos = [
                {
                    id: 0,
                    title: 'Learn JS',
                    description: 'Watch JS tutorials',
                    completed: false,
                }
            ]
            this.currentId = 1;
        } else {
        this.currentId = this.todos[this.todos.lenght - 1].id + 1;
        }
    }

    setView(view){
        this.view = view;
    }

    save() {
        localStorage.setItem('todos', JSON.stringify(this.todos));
    }

    getTodos() {
        return this.todos;
    }

    findTodo(id) {
        return this.todos.findIndex((todo) => todo.id === id);
    }

    toggleCompleted(id) {
        const index = this.findTodo(id);
        const todo = this.todos[index];
        todo.completed = !todo.completed;
        this.save();
    }

    addTodo(title, description){
        const todo = {
            id: this.currentId++,
            title,
            description,
            completed: false,
        }

        this.todos.push(todo);

        this.save();
        return {...todo}; // a un objeto vacio {} le asigna los valores del todo, creando una copia para que no se modifiquen los datos
    }

    removeTodo(id){
        const index = this.findTodo(id);
        this.todos.splice(index, 1);
        this.save();
    }
}