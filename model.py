from file import * 

class Model():
    
    def __init__(self, source_type, file_path, file_sheet):
        if source_type == 'excel':
            self.source_type = source_type
            self.file_path = file_path
            self.file_sheet = file_sheet
            self.file = File(self.file_path, self.file_sheet)
            self.data_set = self.get_data_from_excel(file_path, file_sheet)
        elif source_type != 'excel':
           print('No source type valid selected') 
        pass
   
    def get_data_from_excel(self, file_path, file_sheet):
        
        try:
            file = File(file_path, file_sheet)
            data = file.get_data()
            return data
        except Exception as e:
            print(e)