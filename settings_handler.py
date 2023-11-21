from config import * 

class Settings():
    def __init__(self):
        self.source_type = ""
        self.path = ""
        self.sheet = ""
        self.mode = ""
        self.team = ""
    
    def default_config(self):
        self.source_type = 'excel'
        self.path = FILE_PATH
        self.sheet = FILE_SHEET
        self.mode = "Default"
        self.team = TEAMS[0]
    
    # def set_path(self):
    #     pass
    
    # def set_path(self):
    #     pass
    # def set_sheet(self):
    #     pass
    # def set_mode(self):
    #     pass
    # def set_path(self):
    #     pass