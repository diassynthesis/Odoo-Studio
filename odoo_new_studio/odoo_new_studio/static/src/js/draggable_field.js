/** @odoo-module **/
//import { Component } from "@odoo/owl";
var { Component, mount } = owl; // OWL is globally available

export class DraggableField extends Component {
    static template = "odoo_new_studio.DraggableField";
    static props = ["field"];

    onDragStart(event) {
        event.dataTransfer.setData("field", JSON.stringify(this.props.field));
    }
}
