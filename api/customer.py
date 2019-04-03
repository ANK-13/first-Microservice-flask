from flask_injector import inject
from providers.CouchProvider import CouchProvider
from datetime import datetime

class Customer:
    def __init__(self,id: str,name: str,Org: str,date: datetime):
        self.id = id
        self.name = name
        self.Org = Org
        self.date= date

    def toJson(self):
        return """
            {
                "id": {0},
                "name": {1},
                "Org": {2},
                "date": {3}
            }
        """.format(self.id,self.name,self.Org,self.date)
    
    @inject(data_provider=CouchProvider)
    def get(data_provider: CouchProvider):
        return data_provider.getSampleCustomer()