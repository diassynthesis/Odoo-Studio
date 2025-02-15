/** @odoo-module **/

import { Component, useState } from "@odoo/owl";

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
