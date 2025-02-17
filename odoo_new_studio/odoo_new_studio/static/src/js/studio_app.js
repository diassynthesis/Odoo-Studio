/** @odoo-module **/

//import { Component, mount } from "@odoo/owl";
var { Component, mount } = owl; // OWL is globally available
import { DragDrop } from "./components/drag_drop.js";

export class StudioApp extends Component {
    static template = "odoo_new_studio.StudioApp";
    static components = { DragDrop };
}

// Mount the StudioApp
document.addEventListener("DOMContentLoaded", function () {
    mount(StudioApp, document.body);
});
