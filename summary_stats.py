def calculate(dataFile, col_num):
    """
    Input Parameters:
        dataFile: The dataset file.
        ithAttre: The ith attribute for which the various properties must be calculated.

    Default value of 0,infinity,-infinity are assigned to all the variables as required. 
    """
    numObj, minValue, maxValue, mean, stdev, Q1, median, Q3, IQR = [0,"inf","-inf",0,0,0,0,0,0]
    #YOUR TASK: Write code to assign the values to the respective variables.
    dataFile = pd.read_csv('data/dataset.csv')
    ithAttre = dataFile.iloc[:, col_num]
    
    for col_num in dataFile:
        numObj = ithAttre.count()
        minValue = ithAttre.min()
        maxValue = ithAttre.max()
        mean = ithAttre.mean()
        stdev = ithAttre.std()
        Q1 = ithAttre.quantile(0.25)
        median = ithAttre.median()
        Q3 = ithAttre.quantile(0.75)
        IQR = Q3 - Q1
        
        return numObj, minValue, maxValue, mean, stdev, Q1, median, Q3, IQR


