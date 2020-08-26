import csv
from clients.models import Client

class ClientService:
    def __init__(self, table_name):
        self.tablename = table_name
    
    def create_client(self):
        with open (self.tablename,  mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(Client.to_dict)