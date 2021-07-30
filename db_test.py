from db_model import DbModel
from pprint import pprint

db_model = DbModel("main")

pprint(db_model.get_test_data())

db_model.end()