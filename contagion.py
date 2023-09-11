"""Simple cellular automata model of contagion"""

import config     # edit config.py any parameters as desired
import model
import views

import logging

# Set up logging (use as you did in Lab3 instead of debug print() statements)
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class Controller:
    def __init__(self):
        pass
    
    def run(self):
        
        population = model.Population(config.GRID['Rows'], 
                                      config.GRID['Cols'],
                                      num_people=config.POPULATION['N_People'])
        view = views.TextView(delay=0.5)    # make the delay smaller for faster output
        
        # Have the view monitor model events    
        population.add_observer(view)

        # Initial view, before simulation starts
        view.update()
        
        log.info("Seeding")
        population.seed(num_sick = config.POPULATION['N_Infected'])
        
        view.update()
        
        # Evolve the population for the specified number of steps
        log.info("Running")

        for time_step in range(config.TIMESTEPS):
            log.info(f"Step {time_step}")
            population.step()
            
            # Reset the view's contents to the current state
            view.clear()
            view.add_info(str(population))
            view.update()
            
            # Advance time
            population.tick()

        
if __name__ == "__main__":
    Controller().run()