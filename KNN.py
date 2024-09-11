def run_knn(s_length, s_width, p_length, p_width, k):
    from sklearn.datasets import load_iris
    import math as m 
    import numpy as np

    iris = load_iris()

    data = iris.data.tolist()                                       #data = [[propeties flower 1], [properties flower 2]]
    target = iris.target.tolist()                                   # 0:Setosa, 1:Versicolor, 2:Virginica
    species = {0:"setosa", 1:"versicolor", 2:"virginica"}

    #Counters
    setosa = 0
    versicolor = 0
    virginica = 0


    #Data to classify
    unknown_iris = [s_length, s_width, p_length, p_width]

    # Merging data and target
    merged_data = []
    for index, properties in enumerate(data):
        properties.append(species[target[index]])
        merged_data.append(properties)

    #Calculating distances
    distance = []
    for flower in merged_data:
        calculation = 0
        for index, property in enumerate(flower[:4]):
            calculation += (m.pow((unknown_iris[index]-property),2))
            distance_species = [m.sqrt(calculation), flower[4]]
            distance.append(distance_species)



    #Sorting the list in ascending order 
    distance.sort()


    #Counting the species of the k nearest neighbours
    setosa = sum(x.count("setosa") for x in distance[:k])
    versicolor = sum(x.count("versicolor") for x in distance[:k])
    virginica = sum(x.count("virginica") for x in distance[:k])

    if setosa > versicolor and setosa > virginica:
        result = f"The sample is most likely a setosa. {setosa} out of {k} nearest neighbours account for this result."
    elif versicolor > setosa and versicolor > virginica:
        result =f"The sample is most likely a versicolor. {versicolor} out of {k} nearest neighbours account for this result."
    elif virginica > setosa and virginica > versicolor:
        result = f"The sample is most likely a virginica. {virginica} out of {k} nearest neighbours account for this result."
    else: 
        result = "There seems to be a tie. It would be adviced to choose another value for k."
    return result



        

        




