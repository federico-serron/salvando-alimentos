from data.models import category as category_model


# CREATE
def create_category(name):
    category_model.create_category(name)

# LIST
def list_categories():
    return category_model.list_categories()

# UPDATE
def update_category(id_category, name):
    category_model.update_category(id_category, name)

# DELETE
def delete_category(id_category):
    category_model.delete_category(id_category)