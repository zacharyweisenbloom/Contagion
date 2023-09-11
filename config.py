# Number of timesteps in the simulation
TIMESTEPS = 20
GRID = {
    'Rows': 3,
    'Cols': 3,
}

POPULATION = {
    'N_People':  90,    # Total number of people
    'N_Infected': 2,    # The number of initially infected individuals (for seed)
    'P_AtRisk': 0.3     # Percentage of people at risk    
}

DISEASE = {    
    'P_Transmit': 0.25, # Probability of transmission to a susceptible neighbor
    'T_Recover': 5,     # Time to recover from infection
    'P_Death': 0.001,   # 0.1% chance of dying on a single day
}

# Parameters controlling social interactions
SOCIAL = {
    'Visit_Dist': 5,    # Visit up to n steps away
    'N_Visits': 0.33,   # Number of visits per step, 0.33 is about 1 visit every 3 steps
    'P_Visit': 1.0,     # Visit with probability 1.0
    'N_Neighbors': 8,   # How many neighbors do I visit over time
    'P_Greet': 0.75     # Welcome most visitors
}