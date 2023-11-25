# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method

rankings = [int(x) for x in range(-8, 9) if x != 0]


def calculate(user_ranking, activity_ranking):
    print("user_ranking", user_ranking)

    print("activity_ranking", activity_ranking)
    if user_ranking == activity_ranking:
        return 3
    elif activity_ranking == (user_ranking - 1):
        return 1
    elif activity_ranking > user_ranking:
        if activity_ranking > 0:
            activity_ranking -= 1
        if user_ranking > 0:
            user_ranking -= 1
        diff = (activity_ranking) - (user_ranking)
        return 10 * diff * diff
    return 0


class User:
    def __init__(self, rank=-8, progress=0):
        self.rank = rank
        self.progress = progress

    def inc_progress(self, activity):
        if self.rank > 0:
            self.rank -= 1
        progress = calculate(self.rank, activity)
        #         print ("rankings",rankings[self.rank])
        #         print("progress",progress)
        #         print("activity_ranking",activity_rankinge)
        self.progress += progress
        while self.progress >= 100:
            print(self.progress)
            print(self.rank)
            if self.rank < 9:
                self.progress -= 100
                self.rank += 1
            elif self.rank == -1:
                self.rank += 2
                self.progress -= 100

        if self.rank >= 0:
            self.rank += 1

        print(self.rank)
