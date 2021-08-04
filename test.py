from module.db.db_model import DbModel


db_model = DbModel("main")


# db_model.orm_test()
db_model.create_all_test()

db_model.end()