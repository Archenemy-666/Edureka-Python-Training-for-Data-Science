import pandas as pd 

class Customer_data():
    def __init__(self,filename):
        self.filename = filename
        self.table = None
        self.df = None
        self.name = None
    def namethedf(self,name):
        self.name = name
        return self.name
    def read_data(self,filename):
        self.table = pd.read_csv(self.filename,delimiter=',',header=None)
        self.name = pd.DataFrame(self.table)
    def printdf(self):
        print(self.df)

