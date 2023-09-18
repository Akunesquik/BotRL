import rlgym

env = rlgym.make()
#arg a mettre pour voir le bot en vitesse normale : tick_skip=1,game_speed=1

while True:
    obs = env.reset()
    done = False

    while not done:
      #Here we sample a random action. If you have an agent, you would get an action from it here.
      action = env.action_space.sample() 
      
      next_obs, reward, done, gameinfo = env.step(action)
      
      obs = next_obs