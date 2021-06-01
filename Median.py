import csv

with open("height-weight.csv",newline="") as f:
    read = csv.reader(f)
    file_data = list(read)

file_data.pop(0)

#sorting the data to get the weight of people
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

n = len(new_data)
new_data.sort()

#getting the median
#using floor division to get the nearest whole number
#floor division is shown by //
if n % 2 == 0:
    #getting the first number
    median1 = float(new_data[n//2])
    #getting the second number
    median2 = float(new_data[n//2 - 1])
    #getting the mean of those numbers
    median = (median1 + median2)/2
else:
    median = new_data[n//2]
    print(n)
print("Median is: " + str(median))