import time 

class TTLCache():
    def __init__(self):
        self.dict = {}
    
    def calc_expired(self, timestamp: float, ttl: int) -> bool:
        if time.time() - timestamp <= ttl:
            return False
        else:
            return True
        
    def get(self, key) -> str | None:
        if key in self.dict:
            if self.dict[key]["ttl"]:
                if not self.calc_expired(self.dict[key]["timestamp"], self.dict[key]["ttl"]):
                    return self.dict[key]["val"]
            else:
                return self.dict[key]["val"]
        return None
    
    def set(self, key: str, val: int, ttl: int | None = None) -> None:
        if key not in self.dict:
            self.dict.setdefault(key, 
                {"val" : val, "ttl": ttl, "timestamp" : time.time()} if ttl else {"val" :val})
        
    def delete(self, key: str) -> None:
        del self.dict[key]
    
    def keys(self) -> list[str] | None:
        dict_keys = []
        for key in self.dict.keys():
            if "ttl" in self.dict[key]: 
                if not self.calc_expired(self.dict[key]["timestamp"], self.dict[key]["ttl"]):
                    dict_keys.append(self.dict[key]["val"])
            else:
                dict_keys.append(self.dict[key]["val"])
        return dict_keys if dict_keys else None
        


obj = TTLCache()
obj.set("a", 1, ttl=30)    # "a" expires in 30 seconds
obj.set("b", 2)             # "b" never expires
print(obj.get("a"))                # returns 1 if not expired, None if expired
#obj.delete("a")             # removes key
time.sleep(30)
print(obj.keys())