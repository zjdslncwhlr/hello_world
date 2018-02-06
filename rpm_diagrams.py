#Importing necessary packages to make the program run
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.patches as mpatches

#reading in dataframes from the computer using panadas
df = pd.read_csv("/Users/zephan/Dropbox/SRMP_shared/IRTF_SpeX (SRMP) - Feb28.tsv", sep="\t", comment="#", header=0)
df1 = pd.read_csv("/Users/zephan/Dropbox/SRMP_shared/IRTF_SpeX (SRMP) - Dec_1224.tsv", sep="\t", comment="#", header=0)
df2 = pd.read_csv("/Users/zephan/Dropbox/SRMP_shared/IRTF_SpeX (SRMP) - SpeX_Jul4.tsv", sep="\t", comment="#", header=0)
column_names = ['RA', 'DEC', 'J', 'K', 'PMRA', 'PMDEC', 'Vtan', 'SpT', "NoTitle"]
df3 = pd.read_csv("/Users/zephan/Dropbox/SRMP_shared/BDKP copy.txt", sep="\s+", header = 0, names = column_names)
df_lspm2 = pd.read_csv('/Users/zephan/Dropbox/SRMP_shared/LSPM2.txt', sep="\s+", comment='#', header=2, names=['RA', 'DEC', 'pm', 'pmRA',
'pmDEC','J', 'K'])
column_names3 = ["Names", "LowGravN", "SpectralType", "pm", "J", "J_error", "H", "H_error", "K", "K_error", "w1", "w1_error", "w2", "w2_error", "w3", "w3_error", "w4", "w4_error"]
df_BDKP3A = pd.read_csv("/Users/zephan/Dropbox/SRMP_shared/BDKP3A.txt", sep="\s+", comment="#", header = None, names = column_names3)
column_names4 = ["Names", "pm", "w1", "w1_error", "w2", "w2_error", "w3", "w3_error", "w4", "w4_error", "J", "J_error", "H", "H_error", "K" ,"K_error"]
df_LSPMWISETable = pd.read_csv("/Users/zephan/Dropbox/SRMP_shared/LSPM-WISE-Table.txt", sep="\s+", comment="#", header = 0, names = column_names4)

df4 = pd.read_csv("/Users/zephan/Dropbox/SRMP_shared/IRTF_SpeX (SRMP) - March04.tsv", sep="\t", comment="#", header = 0)
df5 = pd.read_csv("/Users/zephan/Dropbox/SRMP_shared/IRTF_SpeX (SRMP) - March 05.tsv", sep="\t", comment="#", header=0)
df6 = pd.read_csv("/Users/zephan/Dropbox/SRMP_shared/IRTF_SpeX (SRMP) - March 06.tsv", sep="\t", comment="#", header=0)
df5 = df5.drop(df5.index[5:8])
df6 = df6.drop(df6.index[8:106])
#create  new dataframes whcih only have the needed columns (mag tpm etc)
df_rpm = df[['NAME', 'J', "J_err", 'H', 'H_err', "K", "K_err", 'W1', 'W1_err', 'Total PM b']]
df1_rpm = df1[['NAME', 'J', "J_err", 'H', 'H_err', "K", "K_err", 'W1', 'W1_err', 'Total Proper Motion']]
df2_rpm = df2[['NAME', 'J', "J_err", 'H', 'H_err', "K", "K_err", 'W1', 'W1_err', 'Total Proper Motion']]
df4_rpm = df4[['NAME', 'J', 'J_err', 'H', 'H_err', 'K', 'K_err', 'W1', 'W1_err', "Proper Motion b" ]]
df5_rpm = df5[['NAME', 'J', "J_err", 'H', 'H_err', "K", "K_err", 'W1', 'W1_err', 'Total Proper Motion']]
df6_rpm = df6[['NAME', 'J', "J_err", 'H', 'H_err', "K", "K_err", 'W1', 'W1_err', 'Total Proper Motion']]


#my files had a different column name so I changed the names (don't know why I changed the others tho...
df_rpm.columns = ['NAME', 'J', "J_err", 'H', 'H_err', "K", "K_err", 'W1', 'W1_err', 'Total Proper Motion']
df4_rpm.columns = ['NAME', 'J', "J_err", 'H', 'H_err', "K", "K_err", 'W1', 'W1_err', 'Total Proper Motion']

#trying to combine the columns together so all the files are merged into one. We called the combined dataframe "frames"
frames = [df_rpm, df1_rpm, df2_rpm, df4_rpm, df5_rpm, df6_rpm]
result = pd.concat(frames,ignore_index=True)

# Reduced Proper Motion Equation, H = m + 5 log(μ) + 5
#Add extra column to dataframe
#find the reduced proper motion using the W1 data
result["rpm_W1"] = result['W1'] + 5 * np.log10(result["Total Proper Motion"]/1000) + 5
result["J-K_color"] = result['J']-result["K"]

#plot the rpm of W1
#result["J_err - K_err"] = result["J_err"] - result["K_err"]
plt.scatter(result["J-K_color"], result["rpm_W1"], c="black")
plt.title("rpm_w1")
plt.ylabel("Reduced Proper Motion_W1")
plt.xlabel('J-K_color')
plt.ylim([22,4])
plt.xlim([0,3])
plt.show()

#plot the rpm of J data
result["rpm_J"] = result["J"] + 5 * np.log10(result["Total Proper Motion"]/1000) + 5
plt.scatter(result["J-K_color"], result["rpm_J"], c="red")
plt.title("rpm_J")
plt.ylabel("Reduced Proper Motion_J")
plt.xlabel('J-K_color')
plt.ylim([22,4])
plt.xlim([0,3])
plt.show()

#calling column names for upcoming dataframe
#column_names = ['RA', 'DEC', 'J', 'K', 'PMRA', 'PMDEC', 'Vtan', 'SpT', "NoTitle"]
#df3 = pd.read_csv("/Users/zephan/Dropbox/SRMP_shared/BDKP copy.txt", sep="\s+", header = 0, names = column_names)

#exact same steps to plot the graph of the total proper motion of the dataframe
df3["J-K_color1"] = df3['J']-df3["K"]
df3["TPM"] = np.sqrt(np.square(df3["PMRA"]) + np.square(df3["PMDEC"]))
df3["rpm_J"] = df3["J"] + 5 * np.log10(df3["TPM"]) + 5

#Find the bad points--the bad points that are wack on the graph
#the 'badpoints' are found by searching the column J-K_color1 for values less thatn 12.5
#This value is foudn by looking at the scatter plot
badpoints=df3[(df3['J-K_color1'] > 12.5)]
#the badpoints have been found, and we dropped them from the dataframe by calling out their individual rows numbers
df3=df3.drop(df3.index[[474,668,759]])



plt.scatter(df3["J-K_color1"], df3["rpm_J"], c="orange")
plt.ylabel("Reduced Proper Motion_J")
plt.xlabel('J-K_color1')
plt.ylim([22,4])
plt.xlim([0,3])
plt.show()



#df_lspm2 = pd.read_csv('/Users/zephan/Dropbox/SRMP_shared/LSPM2.txt', sep="\s+", comment='#', header=2, names=['RA', 'DEC', 'pm', 'pmRA',
#'pmDEC','J', 'K'])

# "    "
df_lspm2["J-K_color2"] = df_lspm2["J"]-df_lspm2["K"]
df_lspm2["rpm_J"] = df_lspm2["J"] + 5 * np.log10(df_lspm2["pm"]) + 5
badpoints1=df_lspm2[(df_lspm2['J-K_color2'] < -15)]
df_lspm2 = df_lspm2[df_lspm2.K !=27.77 ]
plt.scatter(df_lspm2["J-K_color2"], df_lspm2["rpm_J"], c="orange")
plt.ylabel("Reduced Proper Motion_J")
plt.xlabel('J-K_color1')
plt.ylim([-22, -2])
plt.xlim([-2, 6])
plt.show()

plt.scatter(df3["J-K_color1"], df3["rpm_J"], c="green", s=1)
plt.scatter(df_lspm2["J-K_color2"], df_lspm2["rpm_J"], c="green", s=1)
plt.scatter(result["J-K_color"], result["rpm_J"], c="red")

##bringing in new dataframes to compare against

#column_names3 = ["Names", "LowGravN", "SpectralType", "pm", "J", "J_error", "H", "H_error", "K", "K_error", "w1", "w1_error", "w2", "w2_error", "w3", "w3_error", "w4", "w4_error"]
#df_BDKP3B = pd.read_csv("/Users/zephan/Dropbox/SRMP_shared/BDKP3B.txt", sep="\s+", comment="#", header = None, names = column_names3)

badpoints4=df_BDKP3A[(df_BDKP3A['pm'] < 0.0000001)]
df_BDKP3A=df_BDKP3A.drop(df_BDKP3A.index[[1199, 1200, 1201, 1202]])

df_BDKP3A["rpm_w1"] = df_BDKP3A['w1']+5*np.log10(df_BDKP3A["pm"])+ 5
df_BDKP3A["J-K_color3"] = df_BDKP3A['J']-df_BDKP3A["K"]

df_BDKP3A = df_BDKP3A[df_BDKP3A.J !=-100.00]
df_BDKP3A = df_BDKP3A[df_BDKP3A.K !=-100.00]
df_BDKP3A = df_BDKP3A[df_BDKP3A.pm !=-100.00]
df_BDKP3A = df_BDKP3A[df_BDKP3A.w1 !=-100.00]
df_BDKP3A = df_BDKP3A[df_BDKP3A.pm != 0]

#plot the rpm of W1
plt.scatter(df_BDKP3A["J-K_color3"], df_BDKP3A["rpm_w1"], c="blue")
plt.ylabel("Reduced Proper Motion_w1")
plt.xlabel('J-K_color3')
plt.ylim([26,2])
plt.xlim([-1.1,3.5])
plt.show()

df_BDKP3A["rpm_J"] = df_BDKP3A['J']+5*np.log10(df_BDKP3A["pm"])+ 5
plt.scatter(df_BDKP3A["J-K_color3"], df_BDKP3A["rpm_J"], c="blue")
plt.ylabel("Reduced Proper Motion_J")
plt.xlabel('J-K_color3')
plt.ylim([26,2])
plt.xlim([-1.1,3.5])
plt.show()
#column_names5 = ["Names", "LowGravN", "SpectralType", "pm", "J", "J_error", "H", "H_error", "K", "K_error", "w1", "w1_error", "w2", "w2_error", "w3", "w3_error", "w4", "w4_error"]
#df_BDKP3B = pd.read_csv("/Users/zephan/Dropbox/SRMP_shared/BDKP3B.txt", sep="\s+", comment="#", header = None, names = column_names5)

#df_BDKP3B=df_BDKP3B[(df_BDKP3B['pm'] > 0)]

#df_BDKP3B["rpm_w1"] = df_BDKP3B['w1']+5*np.log10(df_BDKP3B["pm"])+ 5
#df_BDKP3B = df_BDKP3B[df_BDKP3B.w1 !=-100.000]
#df_BDKP3B["J-K_color3"] = df_BDKP3B['J']-df_BDKP3B["K"]
#plt.scatter(df_BDKP3B["pm"], df_BDKP3B["J"])
#plot the rpm of W1
#plt.scatter(df_BDKP3B["J-K_color3"], df_BDKP3B["rpm_w1"], c="blue")
#plt.ylabel("Reduced Proper Motion_w1")
#plt.xlabel('J-K_color3')
#plt.ylim([26,2])
#plt.xlim([-1.1,3.5])
#plt.show()

#comboBDKP3 = [df_BDKP3A, df_BDKP3B]
#df_BDKP3 = pd.concat(comboBDKP3,ignore_index=True)

#column_names4 = ["Names", "pm", "w1", "w1_error", "w2", "w2_error", "w3", "w3_error", "w4", "w4_error", "J", "J_error", "H", "H_error", "K" ,"K_error"]
#df_LSPMWISETable = pd.read_csv("/Users/zephan/Dropbox/SRMP_shared/LSPM-WISE-Table.txt", sep="\s+", comment="#", header = 0, names = column_names4)

##Finding the unusable points##
badpoints3=df_LSPMWISETable[(df_LSPMWISETable['pm'] < 0)]
df_LSPMWISETable=df_LSPMWISETable.drop(df_LSPMWISETable.index[[30190]])

##Removing said points##

##df_LSPMWISETable = df_LSPMWISETable[df_LSPMWISETable.w1 != -100.00]

df_LSPMWISETable["rpm_w1"] = df_LSPMWISETable['w1'] + 5 * np.log10(df_LSPMWISETable["pm"]) + 5
df_LSPMWISETable["J-K_color4"] = df_LSPMWISETable['J']-df_LSPMWISETable["K"]

#plot the rpm of W1
plt.scatter(df_LSPMWISETable["J-K_color4"], df_LSPMWISETable["rpm_w1"], c="black")
plt.ylabel("Reduced Proper Motion_w1")
plt.xlabel('J-K_color4')
plt.ylim([22,-1])
plt.xlim([-0.6,3.5])
plt.show()

df_LSPMWISETable["rpm_J"] = df_LSPMWISETable["J"] + 5 * np.log10(df_LSPMWISETable["pm"]) + 5
plt.scatter(df_LSPMWISETable["J-K_color4"], df_LSPMWISETable["rpm_J"], c="black")
plt.ylabel("Reduced Proper Motion_J")
plt.xlabel('J-K_color4')
plt.ylim([22,-1])
plt.xlim([-0.6,3.5])
plt.show()

outliersJ1 = result[(result["rpm_J"]>20)]
outliersJ2 = result[(result["J-K_color"]>2.5)]
outliersJ3 = [outliersJ1, outliersJ2]
outliersJ = pd.concat(outliersJ3,ignore_index=True)

outliersW11 = result[(result["rpm_W1"]>20)]
outliersW12 = result[(result["rpm_W1"]<7.5)]
outliersW13 = result[(result["J-K_color"])>2.25]
outliersW14 = [outliersW11, outliersW12, outliersW13]
outliersW1 = pd.concat(outliersW14,ignore_index=True)

###########################################################################################
plt.scatter(df_LSPMWISETable["J-K_color4"], df_LSPMWISETable["rpm_w1"], c="black", s=1, label='LSPM WISE')
plt.scatter(df_BDKP3A["J-K_color3"], df_BDKP3A["rpm_w1"], c="blue", s=1, label='BDKP3A')
plt.scatter(result["J-K_color"], result["rpm_W1"], c="red", label="Our Data")
plt.scatter(outliersW1["J-K_color"], outliersW1["rpm_W1"], c="yellow", label="Outliers")
plt.ylabel("Reduced Proper Motion_w1")
plt.xlabel('J-K_color')
plt.ylim([25,-1])
plt.xlim([-1,3.5])
##Add in legend and title##
plt.title("Reduced Proper Motion of w1")
ax = plt.subplot(111)
ax.legend()
plt.show()
#plt.gca().invert_yaxis()


##Plotting all databases together for J##
plt.scatter(df_LSPMWISETable["J-K_color4"], df_LSPMWISETable["rpm_J"], c="black", s=1, label='LSPM WISE')
plt.scatter(df_BDKP3A["J-K_color3"], df_BDKP3A["rpm_J"], c="blue", s=1, label='BDKP3A')
plt.scatter(result["J-K_color"], result["rpm_J"], c="red", label='Our Data')
plt.scatter(outliersJ["J-K_color"], outliersJ["rpm_J"], c="yellow", label="Outliers")
plt.ylabel("Reduced Proper Motion_J")
plt.xlabel('J-K_color')
##Add in legend and title##
plt.title("Reduced Proper Motion of J")
ax = plt.subplot(111)
ax.legend()
plt.show()
##Invert the graph over the x-axis##
plt.gca().invert_yaxis()


##Invert the graph over the x-axis##
##plt.gca().invert_yaxis()
##problem with weird points that stick out on the graph
#look up how to find out which ones they are thru python, dataframe,
##did that^^ woo hoo

#Reading in dataframe... "  "
##column_names1 = ["_RAJ2000", "_DEJ200", "pm", "pmRA", "pmDE", "Jmag", "Kmag"]
##df4 = pd.read_csv("/Users/zephan/Dropbox/SRMP_shared/LSPM2 copy.txt", sep="\s+", header = 0, names = column_names1)

#plt.scatter(result["J-K_color"], result["rpm_W1"], c="red")