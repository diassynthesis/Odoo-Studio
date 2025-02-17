/** @odoo-module **/

//import { Component } from "@odoo/owl";
var { Component, mount } = owl; // OWL is globally available

export class DragDrop extends Component {
    static template = "odoo_new_studio.DragDrop";

    setup() {
        this.items = [
            { id: 1, name: "Field 1" },
            { id: 2, name: "Field 2" },
            { id: 3, name: "Field 3" },
        ];
    }

    onDragStart(event, item) {
        event.dataTransfer.setData("text/plain", JSON.stringify(item));
    }

    onDrop(event) {
        event.preventDefault();
        let data = event.dataTransfer.getData("text/plain");
        let item = JSON.parse(data);
        console.log("Dropped Item:", item);
    }
}
