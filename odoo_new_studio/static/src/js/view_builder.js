odoo.define('odoo_new_studio.ViewBuilder', function (require) {
    "use strict";

    var Widget = require('web.Widget');
    var { Component, mount } = owl; // OWL is globally available

    var ViewBuilder = Widget.extend({
        template: 'ViewBuilder',
        events: {
            'dragstart .draggable-field': '_onDragStart',
            'dragover .drop-area': '_onDragOver',
            'drop .drop-area': '_onDrop',
            'click .generate-xml': '_generateXML',
        },

        init: function (parent, modelFields) {
            this._super(parent);
            this.modelFields = modelFields;
            this.viewXML = '';
        },

        _onDragStart: function (event) {
            event.originalEvent.dataTransfer.setData('text', event.target.dataset.field);
        },

        _onDragOver: function (event) {
            event.preventDefault();
        },

        _onDrop: function (event) {
            event.preventDefault();
            var fieldName = event.originalEvent.dataTransfer.getData('text');
            var dropArea = event.target;
            dropArea.innerHTML += `<div class="view-field">${fieldName}</div>`;
        },

        _generateXML: function () {
            let xml = '<form><sheet><group>';
            document.querySelectorAll('.view-field').forEach(field => {
                xml += `<field name="${field.innerText}"/>`;
            });
            xml += '</group></sheet></form>';
            this.viewXML = xml;
            document.querySelector('.xml-preview').innerText = xml;
        },
    });

    return ViewBuilder;
});
