import pandas as pd

class Data_Analysis:

    def Overview_Of_Dataset(self, DataFrame):
        """[summary: Shows the Overview of the Dataset]
        Args:
            DataFrame ([type: Pandas DataFrame])
        """
        print(f"Dimension of the Dataset: \n{DataFrame.shape}\n")
        print(f"Data types for each Column: \n{DataFrame.dtypes}\n")
        print(f"Read the First Five Rows: \n{DataFrame.head()}\n")
        print(f"Read the Last Five Rows: \n{DataFrame.tail()}\n")
        #print(f"Return an Array of Column Names: \n{DataFrame.columns.values}\n")
        print(
            f"Return a List of Column Names: \n{DataFrame.columns.values.tolist()}\n")
