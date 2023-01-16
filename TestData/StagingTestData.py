from apps.utils import Ultilities
utils = Ultilities()


data = {"username": "gabriel.munteanu.be@gmail.com",
        "company_name": "ENGINEERED FOAM PRODUCTS LIMITED"}

data.update(utils.getLocalData())

