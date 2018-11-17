import gym
import numpy as np

class Taxi:

    """
            Actions
            -------

            0. south
            1. north
            2. east
            3. west
            4. pickup
            5. dropoff
    """
    def __init__(self):
        self.locs = [(0,0), (0,4), (4,0), (4,3), (-1, -1)]

    def decode(self, state):
        stateInfo = {'taxiLoc':0, 'passLoc':0, 'passDest':0}
        stateInfo['passDest'] = self.locs[state % 4]
        state = state // 4
        stateInfo['passLoc'] = self.locs[state % 5]
        state = state // 5
        taxiY = state % 5
        state = state // 5
        taxiX = state
        stateInfo['taxiLoc'] = (taxiX, taxiY)
        return stateInfo

    def printInfo(self, env, obs, steps, rewardTotal):
        print()
        env.render()
        print(f'\n{steps}. Total reward: {rewardTotal}. {self.decode(obs)}')
    
    def main(self):
        env = gym.make('Taxi-v2')
        obs = env.reset()
        (steps, rewardTotal, done) = (1, 0, False)
        while not done:
            self.printInfo(env, obs, steps, rewardTotal)
            action = int(input('(0. south; 1. north; 2. east; 3. west; 4. pick up; 5. drop off) > '))
            (obs, rew, done, _) = env.step(action)
            steps += 1
            rewardTotal += rew
    
        self.printInfo(env, obs, steps, rewardTotal)

Taxi().main()