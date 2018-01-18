
class AppError:
    def __init__(self, message, code):
        self.message = message
        self.errorCode = code

    def __str__(self):
        return self.errorCode + self.message

    def getErrorDict(self):
        newDict = dict()
        newDict['errorCode'] = self.errorCode
        newDict['message'] = self.message
        return newDict
