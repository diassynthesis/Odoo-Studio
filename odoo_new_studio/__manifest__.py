{
    'name': 'Odoo New Studio',
    'version': '1.0',
    'author': 'Med Said BARA & ChatGPT - diassynthesis@gmail.com',  # Replace with your name or company
    'category': 'Tools',
    'summary': 'Custom Odoo Studio with Drag-and-Drop UI & Automations',
    'depends': ['base', 'web'],
    'data': [
        # Security files first
        'security/studio_security.xml',
        'security/ir.model.access.csv',
        
        # Other data files
        'views/studio_owl_templates.xml',
        'views/studio_root_template.xml',
        #'data/studio_template_data.xml',
        'views/studio_action.xml',
        'views/studio_field_view.xml',
        'views/studio_automation_view.xml',
        'views/studio_access_view.xml',        
        'data/studio_template_data.xml',  # ✅ Load default templates 
        'views/studio_view_builder.xml', 
        'views/studio_view_form.xml', 
        'views/studio_action.xml',
        'views/studio_report.xml',          
        'views/studio_menu.xml',
        'views/studio_main_view.xml',        
        'views/studio_model_view.xml',                             
        'views/studio_action.xml',
        'views/new_app_wizard.xml',       
       #'views/studio_view_builder.xml',
        'views/studio_template_view.xml',
        'data/automation_cron.xml',
        'views/studio_assets.xml',
    ],
    'assets': {
        'web.assets_backend': [
			'odoo_new_studio/static/src/lib/owl/owl.js',  # Include OWL explicitly
            'odoo_new_studio/static/src/js/**/*.js',
            'odoo_new_studio/static/src/css/**/*.css',
            'odoo_new_studio/static/src/xml/**/*.xml',
            'odoo_new_studio/static/src/js/components/*.js',
            
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
