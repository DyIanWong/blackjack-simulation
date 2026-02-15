from game import Game
from scipy.stats import binom


class Hypothesis:
    def __init__(self, null, significance, size):
        self.null = null
        self.significance = significance
        self.size = size
        self.playerwins = 0
        self.pushes = 0
    
        #proportion
        for i in range(self.size):
            game = Game()
            game.play()
            if game.playerwin == True:
                self.playerwins += 1
            elif game.push == True:
                self.pushes += 1

        self.sp = self.playerwins / (self.size - self.pushes)
    
        #p value
        self.p_value = binom.cdf(self.playerwins, self.size - self.pushes, self.null)

    def conclusion(self):
        print("Player wins: ", self.playerwins, "\nSample proportion: ", self.sp,  "\np-value: ", self.p_value)
        if self.p_value < self.significance:
            print("Reject null hypothesis at", self.significance, "significance level")
            print("Conclude that player winrate is below", self.null)
        else:
            print("Fail to reject null hypothesis at", self.significance, "significance level")
            print("No significant evidence that player winrate is below ", self.null)