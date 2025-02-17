/** @odoo-module **/

//import { Component, useState } from "@odoo/owl";
var { Component, mount } = owl; // OWL is globally available

export class StudioRoot extends Component {
    setup() {
        this.state = useState({
            activeMenu: "dashboard", // Default active menu
        });
    }

    setActiveMenu(menu) {
        this.state.activeMenu = menu;
    }

    static template = "odoo_new_studio.StudioRoot";
}
