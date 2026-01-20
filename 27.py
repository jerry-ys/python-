class ValidString:
    def __init__(self,name,max_length = 0):
        self.name = name.strip()
        self.max_length = max_length
    def __get__(self,instance,owner):
        return instance.__dict__[self.name]
    def __set__(self,instance,value):
        value = value.strip()
        if len(value) > self.max_length:
            raise ValueError
        else:
            instance.__dict__[self.name] = value

class User:
    username = ValidString("username", max_length=20)
    email = ValidString("email", max_length=50)

    def __init__(self, username, email):
        self.username = username
        self.email = email

u = User("   FishC   ", " fishc@ilovefishc.com ")
print(u.username)     # 输出："FishC"
print(u.email)        # 输出："fishc@ilovefishc.com"
u.username = "FishC" * 5  # 应该抛出 ValueError
