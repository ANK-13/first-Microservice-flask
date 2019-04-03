import datetime as dt

class CouchProvider(object):
    sample = {
            "id": 1,
            "name": "sampleName",
            "Org": "sampleOrg",
            "date": dt.datetime.now()
        }
    def __init__(self):
        self.sample = {
            "id": 1,
            "name": "sampleName",
            "Org": "sampleOrg",
            "date": dt.datetime.now()
        }

    @classmethod
    def getSampleCustomer(self):
        return self.sample