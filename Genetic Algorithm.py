

import random

def intial(num, population_Size):
  length = len(num)
  population = [[round(random.uniform(0, 1)) for i in range(length)] for j in range(population_Size)]
  return population

def Fitness(population, value,weight, Capacity):
  arr_fitness = []
  for i in range(len(population)):# number of chromosomes
    weights = 0
    values = Capacity+1
    while (values > Capacity):
      weights = 0
      values = 0
      accepted_values= []
      for j in range(len(population[i])):#number of genes
        if population[i][j] == 1:
          values += value[j]
          weights += weight[j]
          accepted_values+=[j]
      if values > Capacity:
        population[i][accepted_values[round(random.uniform(0, len(accepted_values)-1))]] = 0
    arr_fitness += [weights]

  return arr_fitness


def newPopulation(population, fitness, mution):
  populationSize = len(population)
  new_Population = []
  new_Population+= [select_first(population, fitness)]

  while(len(new_Population) < populationSize):
    (mating1, mating2) = selection(population, fitness)
    new_Population += [mutate(crossover(mating1, mating2), mution)]

  return new_Population


def select_first(population,fitness):
  st = 0
  for i in range(len(fitness)):
    if fitness[i] > fitness[st]:
      st = i
  return population[st]

def selection(population,fitness):
  size = len(population)
  totalFit = sum(fitness)
  selected_best = round(random.uniform(0,totalFit))
  Sum = 0
  mating1 = []
  fit1 = 0
  for i in range(size):
    Sum += fitness[i]
    if Sum >= selected_best:
      mating1 = population.pop(i)
      fit1 = fitness.pop(i)
      break
  Sum = 0
  selected_best = round(random.uniform(0, sum(fitness)))
  for i in range(len(population)):
    Sum += fitness[i]
    if Sum >= selected_best:
      mating2 = population[i]
      population += [mating1]
      fitness += [fit1]
      return (mating1, mating2)

def crossover(mating1, mating2):
  selected_best = round(random.uniform(0,len(mating1)-1))

  return mating1[:selected_best]+mating2[selected_best:]

def mutate(gene, mutate):
  for i in range(len(gene)):
    selected_best= round(random.uniform(0, mutate))
    if selected_best == 1:
      gene[i] = (1-gene[i])
  return gene
def knapsack(value, weight,capacity, population_Size, mution, GeneCapacity,rate):
  intialization= 0
  population = intial(value, population_Size)
  fitness =Fitness(population, value,weight,capacity)
  while(not test(fitness,rate) and intialization < GeneCapacity):
    intialization += 1
    population = newPopulation(population, fitness, mution)
    fitness = Fitness(population,value,weight,capacity)
  return select_first(population, fitness)
def test(fit, rate):
  maxCount = mode(fit)
  if float(maxCount)/float(len(fit)) >= rate:
    return True
  else:
    return False
def mode(fit):
  values = set(fit)
  maxCount = 0
  for i in values:
    if maxCount < fit.count(i):
      maxCount = fit.count(i)
  return maxCount


testitems=int(input("enter number of test cases"))
for i in range(testitems) :


 chromo_size = []


 num_of_elements=int(input("enter num of pairs"))
 weight = []
 print("enter the values")
 for i in range(0,num_of_elements):
     element=int(input())
     chromo_size.append(element)
 print("enter the weights")
 for i in range(0,num_of_elements):
     element=int(input())
     weight.append(element)

 pop_size = int(input("enter number of items (chromosomes) (pop size)"))
 y = intial(chromo_size, int(pop_size))

 n=0
 best=0
 Best_value=0
 Best_weight=0
 Capacity = int(input("enter capacity"))  # max capcity of the the bag

  # max capcity of the the bag

 fit1 = Fitness(y, chromo_size, weight, Capacity)
 for j in range (len(fit1)):
     if fit1[j]>best:
          best=fit1[j]
          Best_value=chromo_size[j]
          Best_weight=weight[j]

 count_accepted=0

 for i in range(testitems):
      nP=(newPopulation(y,fit1,1))
      fitness=Fitness(nP,chromo_size, weight,Capacity)
      for j in range (len(fitness)):
         # n=0
          if fitness[j]>n:
             best=fitness[j]
             Best_value=chromo_size[j]
             Best_weight=weight[j]
             print("the Best value")
             print(Best_value)
             print("the Best weight")
             print(Best_weight)
             count_accepted+=1
 print("the Best fitness")
 print(best)
 print("number of pairs that accepted is")
 print(count_accepted)

