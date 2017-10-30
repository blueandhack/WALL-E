import matplotlib.pyplot as plt
import csv
import numpy as np

#
# fig,ax=plt.subplots()
# y1=[]
# for i in range(50):
#     y1.append(i)
#     ax.cla()
#     ax.bar(y1,label='test',height=y1,width=0.3)
#     ax.legend()
#     plt.pause(0.3)

x = []
y = []

with open('result.csv', 'r') as csv_file:
    plots = csv.reader(csv_file, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

angles_labels = []

for i in range(0, 360, 3):
    angles_labels.append(i)

labels = np.array(angles_labels)

raw_data = {}

for i in range(0, 360, 3):
    raw_data[i] = 0

i = 0

while i < len(x):
    get_y = y[i]
    if(raw_data[x[i]] != 0):
        get_y = (raw_data[x[i]] + y[i])/2
    raw_data[x[i]] = get_y
    i = i+1

dataLenth = len(raw_data)

data = np.array(list(raw_data.values()))



angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
data = np.concatenate((data, [data[0]])) # 闭合
angles = np.concatenate((angles, [angles[0]])) # 闭合

fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, data, 'bo-', linewidth=2)
ax.set_thetagrids(angles * 180/np.pi, labels)
ax.set_title("Distance Plot", va='bottom')
ax.grid(True)
plt.show()
#
# plt.plot(x,y, label='Loaded from file!')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interesting Graph\nCheck it out')
# plt.legend()
# plt.show()
