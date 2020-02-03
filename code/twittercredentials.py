class TwitterCredentials:
    def __init__(self):
        self.consumer_key =""
        self.consumer_secret =""
        self.access_token =""
        self.access_token_secret =""

    def getCK(self):
        return self.consumer_key

    def getGS(self):
        return self.consumer_secret

    def getAT(self):
        return self.access_token

    def getATS(self):
        return self.access_token_secret
