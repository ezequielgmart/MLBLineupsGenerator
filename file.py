# import xlrd
from config import * 
import pandas as pd

# Clase encargada de manejar el contenido proveniente de un archivo XLSX
class File():
              
    def __init__(self, path, sheet):
        self.path = path
        self.sheet = sheet
        self.engine = FILE_ENGINE
        self.handler = pd
    
    def get_data(self):
        try:
            data = self.handler.read_excel(self.path, sheet_name=self.sheet, engine=self.engine)
            return data
        except Exception as e:
            print(f"Error found: {e}")
            
    
        
        
    
              
  
        
