import math
import matplotlib.pyplot as plt

file = open('./input/input_10.txt')
data = []
for line in file:
    data.append(int(line))
file.close()
data.sort()

output = open('./output/output.txt', 'w')


def percentile(k):
    p_index = float(k/100 * (data.count(data) + 1))
    p_index_rounded = int(p_index)
    p_value = data[p_index_rounded]
    p_result = p_value + (p_index - p_index_rounded) * (data[p_index_rounded + 1] - data[p_index_rounded])
    output.write(str(k) + "th percentile is: " + str(p_result) + "\n")
    return p_result
def deviation():
    sum = 0
    for i in range(data.__len__()):
        sum += math.pow(data[i], 2)
    quadratic_average = sum/data.__len__()
    sum = 0
    for i in range(data.__len__()):
        sum += data[i]
    average = math.pow(sum/data.__len__(), 2)
    deviation = quadratic_average - average
    output.write("Standart deviation is " + str(deviation) + "\n")
    return deviation
def dev_sqrt(deviation):
    output.write("Squeare deviation is " + str(math.sqrt(deviation)) + "\n")
    return math.sqrt(deviation)
def mutate_data():
    mutated_data = list.copy(data)
    for i in range(mutated_data.__len__()):
        mutated_data[i] = mutated_data[i]*0.19 + 81
    output.write(str(mutated_data) + "\n")
    return mutated_data
def branch_leaf():
    table = dict()
    for value in data:
        table[str(value)[0:str(value).__len__()-1]] = ""
    for value in data:
        table[str(value)[0:str(value).__len__()-1]] = table[str(value)[0:str(value).__len__()-1]] + " " + str(value)[str(value).__len__()-1:str(value).__len__()]
    for key in table.keys():
        output.write(str(key + " | " + table[key]) + "\n")
        print(key + " | " + table[key])
def build_diagram():
    fig, ax = plt.subplots()
    boxes = [
        {
            'label': "Box",
            'whislo': data[0],  # Bottom whisker position
            'q1': percentile(25),  # First quartile (25th percentile)
            'med': percentile(50),  # Median         (50th percentile)
            'q3': percentile(75),  # Third quartile (75th percentile)
            'whishi': data[data.__len__()-1],  # Top whisker position
            'fliers': []  # Outliers
        }
    ]
    ax.bxp(boxes, showfliers=False)
    plt.show()
build_diagram()
output.close()
