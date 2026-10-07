class CollegeDatabaseRouter:
    """
    Route les modèles liés à la structure dynamique
    vers college_dynamic.
    Tout le reste va vers college_content.
    """

    dynamic_models = {
        "menu",
        "rubrique",
        "navigation",
        "sousnavigation",
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
        db1 = self.db_for_read(obj1.__class__)
        db2 = self.db_for_read(obj2.__class__)

        if db1 == db2:
            return True

        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name in self.dynamic_models:
            return db == "dynamic"

        return db == "default"