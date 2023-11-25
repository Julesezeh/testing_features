# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method

rankings = [x for x in range(-8,9) if x != 0]

def calculate(user_ranking,activity_ranking):
    if user_ranking == activity_ranking:
        return 3
    elif activity_ranking == (user_ranking-1):
        return 1
    elif activity_ranking > user_ranking:
        diff = (activity_ranking)-(user_ranking)
        return (10*diff*diff)
    elif (user_ranking-activity_ranking) >=2:
        return 0
    
  
class User():
    def __init__(self,rank=-8,progress=0):
        self.rank = rank
        self.progress = progress
    def rank(self):
        return rankings[self.rank]
    def progress(self):
        return self.progress
    def inc_progress(self,activity_rating):
        progress = calculate(rankings[self.rank],activity_ranking)
        self.progress+=progress
        while self.progress >=100:
            if self.rank<len(rankings)-1:
                self.progress -=100
                self.rank+=1
                
        return 0
    
