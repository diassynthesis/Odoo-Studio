odoo.define('odoo_new_studio.main', function(require) {
    "use strict";

    var core = require('web.core');
    var Widget = require('web.Widget');
	var { Component, mount } = owl; // OWL is globally available

    // Import OWL from the static library
    //import { mount, Component } from '../lib/owl/owl.js'; #Odoo does not support ES6 imports (import { ... } from ...;) inside odoo.define

    // OWL Component Definition
    class StudioComponent extends Component {
        static template = "odoo_new_studio.StudioComponentTemplate";
    }

    // Odoo Widget Extension
    var StudioMain = Widget.extend({
        start: function() {
            console.log("Studio Module Loaded");

            // Mount OWL Component if the root element exists
            const root = document.getElementById("studio-root");
            if (root) {
                mount(StudioComponent, { target: root });
            }
        }
    });

    core.action_registry.add('studio_main_action', StudioMain);
});

