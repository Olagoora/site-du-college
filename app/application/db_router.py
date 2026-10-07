class CollegeDatabaseRouter:
    dynamic_models = {
        "menu",
        "rubrique",
        "navigation",
        "sousnavigation",
        "content",
    }

    def db_for_read(self, model, **hints):
        if model._meta.model_name in self.dynamic_models:
            return "dynamic"

        return "default"

    def db_for_write(self, model, **hints):
        if model._meta.model_name in self.dynamic_models:
            return "dynamic"

        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        model1 = obj1._meta.model_name
        model2 = obj2._meta.model_name

        if model1 in self.dynamic_models and model2 in self.dynamic_models:
            return True

        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name in self.dynamic_models:
            return db == "dynamic"

        return db == "default"