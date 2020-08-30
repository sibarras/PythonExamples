#%%
import random, operator, numpy as np, pandas as pd, matplotlib.pyplot as plt

# Data representation
#Create class to handle "cities"
class City:
    # COnstructor with name, and coordinates
    def __init__(self, name:str, x:float, y:float):
        self.name = name
        self.x = x
        self.y = y
    
    # Distance calculator (Get distance to other city)
    def distance(self, city) -> np.float64:
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        # Distance is a numpy float.
        return distance
    
    # Get the repr to the object
    def __repr__(self):
        return f'(Name: {self.name};\tCoordinates: {self.x}, {self.y})'

# panama = City(name='Panama', x=10, y=0)
# chiriqui = City(name='Chiriqui', x=0, y=10)
# pan_chir = panama.distance(chiriqui)
# chir_pan = chiriqui.distance(panama)
# print(type(chir_pan), pan_chir)
# print(chiriqui)

# --------------

# Individual concept:An individual can be seen as a single instance of the problem, for this case it's 
# easy to see that the individual is the sequence of "cities" and the order that they are visited.

# We calculate the fitness using the space between each city and the distance of the last city and the first
# to make a loop. The max distance is worst, so we will make the inverse of the number to use the secuence value.

#Create a fitness class.
class Fitness:
    # Verify if reute is a list or a np.ndarray
    def __init__(self, route:list):
        self.route = route
        self.distance = 0
        self.fitness= 0.0
    
    def routeDistance(self):
        if self.distance == 0:
            pathDistance = 0
            for i in range(0, len(self.route)): # Verify if 0 is needed
                fromCity = self.route[i]
                toCity = None # Verify if this can be outside the loop
                if i + 1 < len(self.route): # use -1 in len() side (Better comprehension)
                    toCity = self.route[i + 1]
                else:
                    toCity = self.route[0]
                pathDistance += fromCity.distance(toCity)
            self.distance = pathDistance
        return self.distance
    
    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness

# --------------------------------- 

# Mutation and breeding.

#Create our initial population

#Route generator
#This method randomizes the order of the cities, this mean that this method creates a random individual.
def createRoute(cityList:list) -> list:
    # take the list and reorder in a random sort
    route = random.sample(cityList, len(cityList))
    return route  # a randomized cityList

#Create first "population" (list of routes)
#This method created a random population of the specified size.

def initialPopulation(popSize:int, cityList:list) -> list:
    population = []
    # Pop size is the number of routes to create or individuals
    for i in range(0, popSize): # verify is zero is needed and i replaced to _
        population.append(createRoute(cityList))
    return population  #each population have routes


#Create the genetic algorithm
#Rank individuals
#This function takes a population and orders it in descending order using the fitness of each individual
def rankRoutes(population:list) -> list:
    fitnessResults = {}  # uses a dictionary to store the results
    for i in range(0,len(population)):
        fitnessResults[i] = Fitness(population[i]).routeFitness()
    sorted_results=sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)
    # i will use this form, but calculate first the time of both
    #sorted_results = sorted(fitnessResults.items(), key=lambda items:items[1], reverse=True)
    return sorted_results  # returns a list of tuples.
# You need a tuple really?


#Create a selection function that will be used to make the list of parent routes
# use pandas to create dataframes
def selection(popRanked:list, eliteSize:int) -> list:
    # selectionResults is a list to append
    selectionResults = []
    df = pd.DataFrame(np.array(popRanked), columns=["Index","Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()
    
    for i in range(0, eliteSize):  # zero needed?
        selectionResults.append(popRanked[i][0])
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100*random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i,3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults

print(ok := np.array([('one', 1),('two', 2),('three', 3),('four', 4),('five', 5)]))
print()
df = pd.DataFrame(ok, columns=['Name', 'Number'])
print(df)
#Create mating pool

def matingPool(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool




#Create a crossover function for two parents to create one child
def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []
    
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])
        

    childP2 = [item for item in parent2 if item not in childP1]
    print(startGene, endGene)

    print(parent1)
    print(parent2)

    print(childP1)
    print(childP2)
    child = childP1 + childP2

    print(child)
    return child

#Create function to run crossover over full mating pool

def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0,eliteSize):
        children.append(matingpool[i])
    
    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool)-i-1])
        children.append(child)
    return children




#Create function to mutate a single route
def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))
            
            city1 = individual[swapped]
            city2 = individual[swapWith]
            
            individual[swapped] = city2
            individual[swapWith] = city1
    return individual



#Create function to run mutation over entire population

def mutatePopulation(population, mutationRate):
    mutatedPop = []
    
    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop



#Put all steps together to create the next generation

def nextGeneration(currentGen, eliteSize, mutationRate):
    popRanked = rankRoutes(currentGen)
    selectionResults = selection(popRanked, eliteSize)
    matingpool = matingPool(currentGen, selectionResults)
    children = breedPopulation(matingpool, eliteSize)
    nextGeneration = mutatePopulation(children, mutationRate)
    return nextGeneration

# ------------------------
#Final step: create the genetic algorithm

def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations):
    pop = initialPopulation(popSize, population)
    progress = [1 / rankRoutes(pop)[0][1]]
    print("Initial distance: " + str(progress[0]))
    
    for i in range(1, generations+1):
        
        pop = nextGeneration(pop, eliteSize, mutationRate)
        progress.append(1 / rankRoutes(pop)[0][1])
        if i%50==0:
          print('Generation '+str(i),"Distance: ",progress[i])
        
        
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    
    plt.plot(progress)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.title('Best Fitness vs Generation')
    plt.tight_layout()
    plt.show()

    
    
    return bestRoute


#Running the genetic algorithm
#Create list of cities

cityList = []

for i in range(0,5):
    cityList.append(City(name = i, x=int(random.random() * 200), y=int(random.random() * 200)))


best_route=geneticAlgorithm(population=cityList, popSize=30, eliteSize=20, mutationRate=0.01, generations=1)
x=[]
y=[]
for i in best_route:
  x.append(i.x)
  y.append(i.y)
x.append(best_route[0].x)
y.append(best_route[0].y)
plt.plot(x, y, '--o')
plt.xlabel('X')
plt.ylabel('Y')
ax=plt.gca()
plt.title('Final Route Layout')
bbox_props = dict(boxstyle="circle,pad=0.3", fc='C0', ec="black", lw=0.5)
for i in range(1,len(cityList)+1):
  ax.text(cityList[i-1].x, cityList[i-1].y, str(i), ha="center", va="center",
            size=8,
            bbox=bbox_props)
plt.tight_layout()
plt.show()