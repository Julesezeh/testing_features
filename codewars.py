# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method

def calculate(user_ranking,activity_ranking):
    if user_ranking == activity_ranking:
        return 3
    elif activity_ranking == (user_ranking-1):
        return 1
    elif activity_ranking > user_ranking:
        x = (activity_ranking)-(user_ranking)
        return (10*int(x)*int(x))
    return 0
class User():
    def __init__(self,rank=-8,progress=0):
        self.rank = rank
        self.progress = progress
    def rank(self):
        return ranking_system[self.rank]
    def progress(self):
        return self.progress
    
    def inc_progress(self,value):
        added_progress = calculate(self.rank,value)
        
        self.progress = int(self.progress)+int(added_progress)
        while self.progress>=100:
            
            if self.rank < 9:
                self.rank+=1
                if self.rank == 0:
                    self.rank += 1
                
                
            self.progress=self.progress-100
