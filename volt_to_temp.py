import pandas as pd
import matplotlib.pyplot as plt
import math

def voltage_to_temp(V):
    V_supply = 5.0
    R_pullup = 10e3
    R0 = 10e3
    T0 = 298.15
    B = 3950

    Rt = R_pullup*V/(V_supply-V)
    r_inf = R0*math.exp(-B/T0)
    T = B/(math.log(Rt/r_inf)) - 273

    return T

if __name__ == "__main__":
    f = open('DATALOG_3rd_floor.txt', 'r').read()
    lines = f.split("\n")

    thermistors = []
    time = 0
    labels = ['Time', 'Thermistor 1', 'Thermistor 2']
    # labels = ['Time', 'Avg Temp']

    for line in lines:
        # Read every line of data
        data = line.split(",")
        if (len(data) >= 2):
            # Update time
            time += 1

            # Convert the Arduino output to voltage
            T1_volt = int(data[0])*5/1023
            T2_volt = int(data[1])*5/1023

            # Convert voltage to temperature
            T1_temp = voltage_to_temp(T1_volt)
            T2_temp = voltage_to_temp(T2_volt)

            # Add to list of data that will be used to create DataFrame
            thermistors.append((time, T1_temp, T2_temp))

    # Create dataframe
    df = pd.DataFrame.from_records(thermistors, columns = labels)
    print(df)

    # Plot Dataframe
    plt.figure()
    ax = plt.subplot(111)
    ax.plot(df['Time'], df['Thermistor 1'], '*', label="Thermistor 1")
    ax.plot(df['Time'], df['Thermistor 2'], '*', label="Thermistor 2")
    # ax.plot(df['Time'], df['Avg Temp'], '*', label='Avg Temp')
    plt.xlabel("Time (min)")
    # plt.ylabel("Temperature (deg C)")
    plt.ylabel("Temperature (deg C)")
    ax.legend()
    plt.show()
