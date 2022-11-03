import math

import matplotlib.pyplot as plt
import numpy as np

def main():
    #print("Enter filename to start program")
    #fileName = input()
    filename = "input_10.txt"
    file = open(f'./input/{filename}')
    data_sum = []
    data_time = []
    for line in file:
        data_sum.append(float(line[0:line.find('\t')].replace(',', '.')))
        data_time.append(int(line[line.find('\t')+1:line.__len__()]))
    file.close()
    output_file = open('./output/output.txt', 'w')
    scatterplot(data_sum, data_time)
    output(data_sum, data_time, output_file)

def scatterplot(data_sum, data_time):
    average_x = average_sum(data_sum)
    average_y = average_time(data_time)
    m = m_coefficient(data_sum, data_time, average_x, average_y)
    k = k_coefficient(m, average_x, average_y)
    corel = corelation(data_sum, data_time)
    plt.scatter(data_sum, data_time, 15, label="scatterplot")
    plt.xlabel("Amount")
    plt.ylabel("Time")
    plt.xticks(np.arange(0, 10, step=0.5))
    plt.yticks(np.arange(0, 100, step=5))
    Y = []
    for i in range(len(data_sum)):
        Y.append(data_sum[i]*m + k)
    if corel > 0:
        plt.plot(data_sum, Y, label="Line of regression(Trend is positive)", color="red")
    elif corel < 0:
            plt.plot(data_sum, Y, label="Line of regression(Trend is negative)", color="red")
    else:
        plt.plot(data_sum, Y, label="Line of regression(Trend is missing)", color="red")
    plt.legend(loc="best")
    plt.show()

def average_sum(data_sum):
    average = 0
    for index in range(len(data_sum)):
        average += data_sum[index]
    return average/data_sum.__len__()
def average_time(data_time):
    average = 0
    for index in range(len(data_time)):
        average += data_time[index]
    return average/data_time.__len__()

def covariation(data_sum , data_time, average_sum, average_time):
    covariation_result = 0
    for i in range(len(data_sum)):
        covariation_result += (data_sum[i] - average_sum) * (data_time[i] - average_time)
    return covariation_result/len(data_sum)

def deviation(data):
    sum = 0
    for i in range(data.__len__()):
        sum += math.pow(data[i], 2)
    quadratic_average = sum/data.__len__()
    sum = 0
    for i in range(data.__len__()):
        sum += data[i]
    average = math.pow(sum/data.__len__(), 2)
    return quadratic_average - average
def m_coefficient(data_sum, data_time, average_sum, average_time):
    return covariation(data_sum, data_time, average_sum, average_time)/deviation(data_sum)

def k_coefficient(m_coefficient,average_sum, average_time):
    return average_time - average_sum*m_coefficient

def corelation(data_sum, data_time):
    average_x = average_sum(data_sum)
    average_y = average_time(data_time)
    deviation_x = deviation(data_sum)
    deviation_y = deviation(data_time)
    cov = covariation(data_sum, data_time, average_x, average_y)
    return cov / math.sqrt(deviation_x * deviation_y)
def output(data_sum, data_time, output_file):
    average_x = average_sum(data_sum)
    average_y = average_time(data_time)
    cov = covariation(data_sum, data_time, average_x, average_y)
    m = m_coefficient(data_sum, data_time, average_x, average_y)
    k = k_coefficient(m, average_x, average_y)
    corel = corelation(data_sum, data_time)
    output = ""
    output += f'Center of weight G({round(average_x,3)};{average_y})\n'
    output += f'Covariation is {round(cov,3)}\n'
    output += f'Line of regression is y={round(m,3)}x + {round(k,3)}\n'
    output += f'Coefficient of corelation is {round(corel, 3)}\n'
    output_file.write(output)
    output_file.close()
main()


