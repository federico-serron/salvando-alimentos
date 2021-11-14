from data.models import paymethod as pay_model

# CREATE
def create_paymethod(name):
    pay_model.create_paymethod(name)


# LIST
def list_paymethod():
    return pay_model.list_paymethod()


# UPDATE
def update_paymethod(id, name):
    pay_model.update_paymethod(id, name)


# DELETE
def delete_paymethod(id_paymethod):
    pay_model.delete_paymethod(id_paymethod)