/** @odoo-module **/
//import { Component } from "@odoo/owl";
var { Component, mount } = owl; // OWL is globally available

export class DropZone extends Component {
    static template = "odoo_new_studio.DropZone";
    static props = ["onDropField"];

    onDrop(event) {
        event.preventDefault();
        const field = JSON.parse(event.dataTransfer.getData("field"));
        this.props.onDropField(field);
    }

    allowDrop(event) {
        event.preventDefault();
    }
}
