from datetime import datetime
from data.models import rating as rating_model
from data.models import user as auth

def _set_date_time():
    # dd/mm/YY H:M:S
    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

def _rating_exists(id):
    comment = rating_model._rating_exists(id)
    return not len(comment) == 0



# CREATE
def create_rating(id_user, product_id, rating, comment):
    if _user_exists(id_user):
        date = _set_date_time()
        rating_model.create_rating(id_user, product_id, rating, comment, date)
        return True
    else:
        return False


# LIST
def list_ratings():
    return rating_model.list_ratings()


# UPDATE
def update_rating(id_rating, rating, comment):
    if _rating_exists(id_rating):
        date = _set_date_time()
        rating_model.update_rating(id_rating, rating, comment, date)
        return True
    else:
        return False


# DELETE
def delete_rating(id_rating):
    rating_model.delete_rating(id_rating)


#  CHECK IF USER EXISTS
def _user_exists(id):
    result = auth.obtener_usuario(id)
    return not len(result) == 0


# CHECK IF RATING ID EXISTS
def _rating_exists(id_rating):
    result = rating_model._rating_exists(id_rating)
    return not len(result) == 0