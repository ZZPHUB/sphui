import json 

class sph_arg():
    def __init__(self):
        self.json = {"setting":{},"debug":{}}
        self.file_name = ""
    def load(self):
        try:
            fd = open(self.file_name)
            self.json = json.load(fd)
        except Exception as err:
            print(err)

    def write(self):
        try:
            fd = open(self.file_name,'w')
            tmp = json.dumps(self.json,sort_keys=True, indent=4, separators=(',', ': '))
            fd.write(tmp)
            fd.close
        except Exception as err:
            print(err)

    def set_file_name(self,tmp_file_name=str):
        try:
            if(type(tmp_file_name) == type("str type")):
                self.file_name = tmp_file_name
            else:
                raise "file name type error!"
        except Exception as err:
            print(err)

