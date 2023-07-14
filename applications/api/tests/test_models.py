"""
The test dual for models.py
Since this is an abstract model we make it concrete here, some more tricks
needed to actually create the model in the test database.
"""

from django.db import connection, models
from django.test import TestCase

from applications.api.common import admin
from applications.api.common import models as api_models


class TestModel(TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Calling the creation of the model before super creates the transaction.
        """
        class_meta = type("Meta", (object,), {"app_label": "applications.test"})
        cls.model = type(
            "ModelConcrete",
            (api_models.Model,),
            {
                "number": models.IntegerField(default=0),
                "Meta": class_meta,
                "__module__": "",
            },
        )

        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(cls.model)
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        returns = super().tearDownClass()
        with connection.schema_editor() as schema_editor:
            schema_editor.delete_model(cls.model)

        return returns

    def test_01_create(self):
        instance = self.model.objects.create()
        self.assertIsNotNone(instance.rid)
        self.assertIsNotNone(instance.dts_inserted)
        self.assertIsNotNone(instance.dts_modified)
        self.assertIsNone(instance.dts_archived)

    def test_02_query(self):
        instance = self.model.objects.create()
        query = self.model.objects.filter(rid=instance.rid)
        self.assertEqual(query.count(), 1)

    def test_03_modify(self):
        instance = self.model.objects.create()
        modified_old = instance.dts_modified
        instance.save()
        modified_new = instance.dts_modified
        self.assertGreater(modified_new, modified_old)

    def test_04_delete_is_archive(self):
        instance = self.model.objects.create()
        instance.delete()
        self.assertIsNotNone(instance.dts_archived)

        instances_count = self.model.objects.all().count()
        self.assertEqual(instances_count, 0)
        all_instances_count = self.model.objects_with_archived.all()
        self.assertNotEqual(all_instances_count, 0)

    def test_05_delete_no_archive(self):
        instance = self.model.objects.create()
        instance.delete(no_archive=True)
        all_instances_count = self.model.objects_with_archived.all().count()
        self.assertEqual(all_instances_count, 0)

    def test_06_admin_factory(self):
        # pylint: disable=W0212 # testing sub dependencies.
        returns = admin._model_admin_factory(self.model)
        self.assertEqual(type(returns), type(admin.admin.ModelAdmin))
