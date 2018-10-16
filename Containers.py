import matplotlib.pyplot
import random
agents = []
#agents.append([0,0])
#agents.append([3,4])
agents.append([random.randint(0,99),random.randint(0,99)])
agents.append([random.randint(0,99),random.randint(0,99)])


print(agents)


answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer)



print(max(agents))


import operator
print(max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])

matplotlib.pyplot.scatter(agents[1][1],agents[1][0],color='red')
matplotlib.pyplot.scatter(agents[0][1],agents[0][0],color='black')


matplotlib.pyplot.show()
