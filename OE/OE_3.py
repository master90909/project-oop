class SMA:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        

    def login(self):
        pass
    def post(self):
        pass
class INSTAGRAM(SMA):
    def __init__(self, username, password, num_follw):
        super().__init__(username, password)
        self.num_follw = num_follw
    
    def shr_story(self):
        pass
class TwittA(SMA):
    def __init__(self, username, password, num_twi):
        super().__init__(username, password)
        self.num_twi = num_twi
        

    def tweet(self):
        pass



