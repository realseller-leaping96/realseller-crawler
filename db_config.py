class DbConfig:
    
    def __init__(self):
        self.dbconfig = {
            "main":{
                "host":"localhost",
                "user":"root",
                "password":"123123",
                "database":"gidseller"
            },
            "sub":{
                "host":"localhost",
                "user":"root",
                "password":"123123",
                "database":"gidseller"
            }
        }
        
    def test(self,db_name):
        return self.dbconfig[db_name]
    