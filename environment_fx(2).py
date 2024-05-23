
import pandas as pd
import numpy as np
import time

def test1(episodes, environment):
    
    start_time = time.time()  
    
    for episode in range(1, episodes+1):
        state = environment.reset()
        done = False
        reward = 0
    
        while not done:
            action = environment.action_space.sample()
            n_state, reward, done, truncated, info = environment.step(action)
            reward
            
        # Extracting the 2nd and 3rd key-value pairs
        keys = list(info.keys())
        values = list(info.values())

        second_key = keys[1]
        second_value = values[1]

        third_key = keys[2]
        third_value = values[2]
        
        fourth_key = keys[4]
        fourth_value = values[4]
        
        print("Episode:{} Reward:{}". format(episode, reward), "\n")
        print(second_key, second_value, "\n")
        print(third_key, third_value,"\n")
        print(fourth_key, fourth_value,"\n")
        
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
        
def test2(episodes, environment):    
    for episode in range(episodes):
        done = False
        obs = environment.reset()
        step = 0
        while not done:
            step += 1
            random_action = environment.action_space.sample()
            obs, reward, done, trun, info = environment.step(random_action)
            
            
            # Extracting the 2nd and 3rd key-value pairs
            keys = list(info.keys())
            values = list(info.values())

            # Getting the 2nd key-value pair
            zeroth_key = keys[0]
            zeroth_value = values[0]
            
            print("STEP:", step)
            print("action", random_action)
            print("observation", obs)
            print(zeroth_key,zeroth_value,first_key,first_value)
            print("\n")
            
def test3(episodes, environment):    
    for episode in range(episodes):
        done = False
        obs = environment.reset()
        step = 0
        print(obs, "\n")
        while not done:
            step += 1
            random_action = environment.action_space.sample()
            obs, reward, done, trun, info = environment.step(random_action)
            
            
            # Extracting the 2nd and 3rd key-value pairs
            keys = list(info.keys())
            values = list(info.values())

            # Getting the 2nd key-value pair
            zeroth_key = keys[0]
            zeroth_value = values[0]

            # Getting the 3rd key-value pair

            sixth_key = keys[3]
            sixth_value = values[3]
            
            print("STEP:", step)
            print("ACT","\n",  random_action)
            print("OBS","\n",  obs)
            print(zeroth_key, zeroth_value, sixth_key, sixth_value)
            print("\n")
            
            
def evaluate1(episodes, environment, model):
    
    for ep in range(episodes):

        obs, _ = environment.reset()  # Unpack the tuple and ignore the info part
        done = False

        while not done:
            action, _ = model.predict(obs)  # Now obs is just the observation array
            obs, reward, done, truncated, info = environment.step(action)
            # Extracting the 2nd and 3rd key-value pairs
            keys = list(info.keys())
            values = list(info.values())

            # Getting the 2nd key-value pair
            first_key = keys[0]
            first_value = values[0]
            
            # Getting the 2nd key-value pair
            second_key = keys[1]
            second_value = values[1]

            # Getting the 3rd key-value pair

            third_key = keys[2]
            third_value = values[2]

      
            
            print("Act:", action, "\n", "Obs:", obs, "\n", "Balance", first_value)
                
        print(second_key, second_value, third_key, third_value, "\n")

    environment.close()
            
        
        
def evaluate2(episodes, environment, model):
    
    mean_irr = 0
    mean_fin_balance = 0
    irr = 0
    fin_balance = 0
    count = 0
    irr_count = 0
    npv = 0

    for ep in range(episodes):

        obs, _ = environment.reset()  # Unpack the tuple and ignore the info part
        done = False

        while not done:
            action, _ = model.predict(obs)  # Now obs is just the observation array
            obs, reward, done, truncated, info = environment.step(action)
            # Extracting the 2nd and 3rd key-value pairs
            keys = list(info.keys())
            values = list(info.values())

            # Getting the 2nd key-value pair
            second_value = values[1]

            # Getting the 3rd key-value pair
    
            third_value = values[2]
            fourth_value = values[4]
        
        fin_balance += second_value
        npv += fourth_value
        count += 1
        
        if not np.isnan(third_value):
            irr += third_value
            irr_count += 1
            
    mean_fin_balance = fin_balance/count
    mean_irr = irr/irr_count
    mean_npv = npv/count

    print(mean_npv, "\n", mean_irr, "\n" )

    environment.close()

def calculate_import_export(PV_production, energy_consumption):
    
    imported = pd.DataFrame(index=energy_consumption.index, columns=energy_consumption.columns)
    exported = pd.DataFrame(index=energy_consumption.index, columns=energy_consumption.columns)
    
    for i in PV_production.index:
        for c in PV_production.columns:
        
            if PV_production.at[i, c] > energy_consumption.at[i, c]:
            
                exported.at[i, c] = PV_production.at[i, c] - energy_consumption.at[i, c]
            
        
            elif PV_production.at[i, c] < energy_consumption.at[i, c]:
            
                imported.at[i, c] = energy_consumption.at[i, c] - PV_production.at[i, c]
    
    exported = exported.fillna(0)
    imported = imported.fillna(0)
    
    return exported, imported



def basepolicy(episodes, environment):
    
    mean_irr = 0
    mean_fin_balance = 0
    irr = 0
    fin_balance = 0
    count = 0
    irr_count = 0
    npv = 0

    for ep in range(episodes):

        obs, _ = environment.reset()  # Unpack the tuple and ignore the info part
        done = False

        while not done:
            
            action = 0
            for i, n in enumerate(obs):
                if i < 8:
                    if n < 0.75:
                        action + 1

            obs, reward, done, truncated, info = environment.step(action)

            # Extracting the 2nd and 3rd key-value pairs
            keys = list(info.keys())
            values = list(info.values())

            # Getting the 2nd key-value pair
            second_value = values[1]

            # Getting the 3rd key-value pair
    
            third_value = values[2]
            fourth_value = values[4]
        
        fin_balance += second_value
        npv += fourth_value
        count += 1
        if not np.isnan(third_value):
            irr += third_value
            irr_count += 1
            
    mean_fin_balance = fin_balance/count
    mean_irr = irr/irr_count
    mean_npv = npv/count

    print(mean_npv, "\n", mean_irr, "\n" )

    environment.close()
