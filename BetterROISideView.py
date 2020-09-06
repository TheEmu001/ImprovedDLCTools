import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from scipy.signal import find_peaks
from sklearn.preprocessing import normalize, MinMaxScaler

# prevent numpy exponential
# notation on print, default False
np.set_printoptions(suppress=True)

# global variables
y_values_df = pd.DataFrame(columns=['TimeElapsed'])
frame_df = pd.DataFrame(columns=['TimeElapsed'])

# conversion path *must* point to CSV and dataFrame is reading from CSV
path = "/Users/imehndiokho/PycharmProjects/ImprovedDLCTools/Vglut-cre C135 M3+_2DLC_resnet50_EnclosedBehaviorMay27shuffle2_251000.csv"

data_df = pd.read_csv(path, skiprows=3, names=['frameNo','backX', 'backY', 'backLike', 'headX', 'headY', 'headLike',
                                                   'snoutX', 'snoutY', 'snoutLike',
                                                   'LeftEarX', 'LeftEarY', 'LeftEarlikelihood', 'rightearx',
                                                   'righteary',
                                                   'rightearlikelihood', 'leftforepawx', 'leftforepawy',
                                                   'leftforewlikelihood', 'rightforepawx', 'rightforepawy',
                                                   'rightforepawlikelihood', 'lefthindpawx', 'lefthindpawy',
                                                   'lefthindpawlikelihood', 'righthindpawx', 'righthindpawy',
                                                   'righthindpawlikelihood', 'tailbasex', 'tailbasey',
                                                   'taillikelihood'])
data_df['TimeElapsed'] = data_df["frameNo"] / 30

animalName = []
animalName[:] = ' '.join(path.split()[2:3])
fullName = ' '.join(path.split()[:2]) + " " + ''.join(animalName[:2])
short_name = fullName[52:]


# generating plots
plt.plot(data_df['TimeElapsed'], data_df['headY'], color='blue', marker='o', markersize=0.1, linewidth=0.5,
         label='Head Y values')
plt.xlabel('time (seconds)')
plt.ylabel('Head Y coordinate')
animal = []
animal[:] = ' '.join(path.split()[2:3])
# plt.title('Snout Velocity vs. Time for: ' + ' '.join(path.split()[:2]) + " " + ''.join(animal[:3]))
plt.title('Head Y coordinate vs. Time for: ' + short_name)
plt.show()

