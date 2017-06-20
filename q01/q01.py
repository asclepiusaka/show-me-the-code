import uuid

class generate_N_uuid:
    def __init__(self):
        self.size = 0
        self.lst = []

    def generate_number(self,size):
        self.size = size
        self.lst = [str(uuid.uuid4()) for i in range(self.size)]

    def return_result(self):
        return self.lst

a = generate_N_uuid()
a.generate_number(200)
keys = a.return_result()

with open("record.txt","w") as f:
    for key in keys:
        f.write("%s\n"%key)