import pandas as pd
class CustomerData():
    def __init__(self,filename):
        self.filename = filename
    def get_file(self,filename):
        self.filename = pd.read_csv(filename)
        self.name = pd.DataFrame(self.filename)
        return self.filename