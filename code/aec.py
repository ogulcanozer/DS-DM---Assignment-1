#_______________________________________________________________________________
# CE888 Project |        aec.py       | Ogulcan Ozer. | Feb. 2019 | UNFINISHED.
#_______________________________________________________________________________

##************************
import tensorflow as tf
import pandas as pd
import numpy as np
import os
##************************

path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','data'))
#-------------------------------------------------------------------------------
# Functions
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Main program.
#-------------------------------------------------------------------------------

data = pd.read_csv(os.path.join(path,'dataset_diabetes\diabetic_data.csv'),
sep=',',error_bad_lines=False, warn_bad_lines=False)

print(data.head())
print(data.describe())
print('-----------------------------------------------------------------------')
data1 = pd.read_csv(os.path.join(path,'UCI HAR Dataset','train',
'X_train.txt'),delim_whitespace=True,error_bad_lines=False, warn_bad_lines=False,
header=None)
label1 = pd.read_csv(os.path.join(path,'UCI HAR Dataset','train',
'y_train.txt'),sep=',',error_bad_lines=False, warn_bad_lines=False)
data1['labels']= label1
print(data1.head())
print(data1.describe())
print('-----------------------------------------------------------------------')
data2 = pd.read_csv(os.path.join(path,'HTRU2\HTRU_2.csv'),
sep=',',error_bad_lines=False, warn_bad_lines=False,header=None)
print(data2.head())
print(data2.describe())

#************ FOR TRAINING **************#
# df_dummies = pd.get_dummies(data)
# print(df_dummies.head())
# df_dummies.drop(['encounter_id', 'patient_nbr'], axis=1, inplace = True)
# print(df_dummies.head())
# print()
# np.savetxt("dummy_out.txt", df_dummies.columns.to_numpy(),fmt="%s")
#************* USE TO SAVE AND DISPLAY THE MODEL *************#
# writer = tf.summary.FileWriter('.')
# writer.add_graph(tf.get_default_graph())
# writer.flush()

#-------------------------------------------------------------------------------
#                               End of aec.py
#-------------------------------------------------------------------------------
