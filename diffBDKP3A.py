import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Read in dataframes
df = pd.read_csv("/Users/zephan/Dropbox/SRMP_shared/IRTF_SpeX (SRMP) - Feb28.tsv", sep="\t", comment="#", header=0)
df1 = pd.read_csv("/Users/zephan/Dropbox/SRMP_shared/IRTF_SpeX (SRMP) - Dec_1224.tsv", sep="\t", comment="#", header=0)
df2 = pd.read_csv("/Users/zephan/Dropbox/SRMP_shared/IRTF_SpeX (SRMP) - SpeX_Jul4.tsv", sep="\t", comment="#", header=0)
column_names3 = ["Names", "LowGravN", "SpectralType", "pm", "J", "J_error", "H", "H_error", "K", "K_error", "w1", "w1_error", "w2", "w2_error", "w3", "w3_error", "w4", "w4_error"]
df_BDKP3A = pd.read_csv("/Users/zephan/Dropbox/SRMP_shared/BDKP3A.txt", sep="\s+", comment="#", header = None, names = column_names3)
column_names4 = ["Names", "pm", "w1", "w1_error", "w2", "w2_error", "w3", "w3_error", "w4", "w4_error", "J", "J_error", "H", "H_error", "K" ,"K_error"]
df_LSPMWISETable = pd.read_csv("/Users/zephan/Dropbox/SRMP_shared/LSPM-WISE-Table.txt", sep="\s+", comment="#", header = 0, names = column_names4)


df_rpm = df[['NAME', 'J', "J_err", 'H', 'H_err', "K", "K_err", 'W1', 'W1_err', 'Total PM b']]

#my file had a different column name so I changed the names (don't know why I changed the others tho...
df1_rpm = df1[['NAME', 'J', "J_err", 'H', 'H_err', "K", "K_err", 'W1', 'W1_err', 'Total Proper Motion']]
df2_rpm = df2[['NAME', 'J', "J_err", 'H', 'H_err', "K", "K_err", 'W1', 'W1_err', 'Total Proper Motion']]
df_rpm.columns = ['NAME', 'J', "J_err", 'H', 'H_err', "K", "K_err", 'W1', 'W1_err', 'Total Proper Motion']

#trying to combine the columns together so all the files are merged into one. We called the combined dataframe "frames"
frames = [df_rpm, df1_rpm, df2_rpm]
result = pd.concat(frames,ignore_index=True)

result["J-K_color"] = result['J']-result["K"]

#plot the rpm of J data
result["rpm_J"] = result["J"] + 5 * np.log10(result["Total Proper Motion"]/1000) + 5
plt.scatter(result["J-K_color"], result["rpm_J"], c="red")
plt.ylabel("Reduced Proper Motion_J")
plt.xlabel('J-K_color')
plt.ylim([22,4])
plt.xlim([0,3])
plt.show()


df_BDKP3A["J-K_color3"] = df_BDKP3A['J']-df_BDKP3A["K"]
df_BDKP3A["rpm_J"] = df_BDKP3A['J']+5*np.log10(df_BDKP3A["pm"])+ 5

##Getting rid of bad points##
df_BDKP3A = df_BDKP3A[df_BDKP3A.J !=-100.00]
df_BDKP3A = df_BDKP3A[df_BDKP3A.K !=-100.00]
df_BDKP3A = df_BDKP3A[df_BDKP3A.pm !=-100.00]
df_BDKP3A = df_BDKP3A[df_BDKP3A.pm != 0]

##Graphing the dataframes individually##
plt.scatter(df_BDKP3A["J-K_color3"], df_BDKP3A["rpm_J"], c="blue")
plt.ylabel("Reduced Proper Motion_J")
plt.xlabel('J-K_color3')
plt.ylim([26,2])
plt.xlim([-1.1,3.5])
plt.show()

df_LSPMWISETable["J-K_color4"] = df_LSPMWISETable['J']-df_LSPMWISETable["K"]
df_LSPMWISETable["rpm_J"] = df_LSPMWISETable["J"] + 5 * np.log10(df_LSPMWISETable["pm"]) + 5
plt.scatter(df_LSPMWISETable["J-K_color4"], df_LSPMWISETable["rpm_J"], c="black")
plt.ylabel("Reduced Proper Motion_J")
plt.xlabel('J-K_color')
plt.ylim([22,-1])
plt.xlim([-0.6,3.5])
plt.show()

##Plotting all databases together##
plt.scatter(df_LSPMWISETable["J-K_color4"], df_LSPMWISETable["rpm_J"], c="black", s=1, label='LSPM WISE')
plt.scatter(df_BDKP3A["J-K_color3"], df_BDKP3A["rpm_J"], c="blue", s=1, label='BDKP3A')
plt.scatter(result["J-K_color"], result["rpm_J"], c="red", label='Our Data')
plt.ylabel("Reduced Proper Motion_J")
plt.xlabel('J-K_color')
##Add in legend and title##
plt.title("Reduced Proper Motion of J")
ax = plt.subplot(111)
ax.legend()
plt.show()
##Invert the graph over the x-axis##
plt.gca().invert_yaxis()
