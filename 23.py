class C:
    data = {}
    times = {}
    def create(self,url):
        _ = url[8:].split("/")
        x = ""
        for each in _:
            x += each
            if not self.data.get(x):
                self.data[x] = url
                self.times[x] = 0
                break
            else:
                x += "/"
        return x
    
    def __setitem__(self,short_url,long_url):
        if self.data.get(short_url):
            raise NameError("存在该短链接！")
        else:
            self.data[short_url] = long_url

    def __getitem__(self,short_url):
        if self.data.get(short_url):
            self.times[short_url] += 1
            return self.data[short_url]
        else:
            raise NameError("未找到该链接！")

    def __iter__(self):
        self._keys = list(self.data.keys())
        self.value = 0
        return self
    def __next__(self):
        if self.value == len(self.data):
            raise StopIteration
        short_url = self._keys[self.value]
        long_url = self.data[short_url]
        self.value += 1
        return f"{short_url}->{long_url}"

    
