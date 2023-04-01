import json
class Fichier:
    
    def __init__(self):
        self.types_of_encoding = ["utf8", "cp1252"]
    
    def get_data_files(self,file):
        try:
            with open(file,'r') as contenue:
                data = json.load(contenue)
        except Exception:
            for encoding_type in self.types_of_encoding:
                with open(file, encoding = encoding_type, errors ='replace') as contenue:
                        data = json.load(contenue)
        return data