from odoo.tests import common

class TestStudio(common.TransactionCase):
    def test_create_model(self):
        model = self.env['studio.model'].create({
            'name': 'Test Model',
            'model_id': 'test.model',
        })
        self.assertEqual(model.name, 'Test Model')
