class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file = None
        self.data = []
    
    def __enter__(self):
        try:
            self.file = open(self.filename, 'r', encoding='utf-8')
            lines = self.file.readlines()
            
            if not lines:
                return None

            self.data = [line.strip().split(self.sep) for line in lines]

            expected_len = len(self.data[0])
            for row in self.data:
                if len(row) != expected_len:
                    return None
            return self
        
        except FileNotFoundError:
            return None 
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

    def getdata(self):
        if not self.data:
            return None
        
        start = 1 if self.header else 0
        start += self.skip_top
        end = len(self.data) - self.skip_bottom
        
        return self.data[start:end]

    def getheader(self):
        return self.data[0] if self.header else None

with CsvReader("good.csv", header=True) as file:
    if file:
        print("Header:", file.getheader())
        print("Data:", file.getdata())
