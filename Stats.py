from threading import Timer

class Stats():

    def __init__(self):

        self.score = 0
        self.earnings = 0
    
    def earsec(self):

        self.score += self.earnings
        self.t = Timer(1, self.earsec)
        self.t.start()
    
    def stop(self):

         self.t.cancel()
