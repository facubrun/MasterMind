import Model from './model.js';
import View from './view.js';

document.addEventListener('DOMContentLoaded', () => {// ejecuta cuando carga el contenido
    const model = new Model();
    const view = new View();

    model.setView(view);
    view.setModel(model);

    view.render();
});