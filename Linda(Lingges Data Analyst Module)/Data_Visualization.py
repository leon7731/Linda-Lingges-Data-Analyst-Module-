import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


class Data_Visualization():

    def Pair_Plot(self, DataFrame):
        """[summary: Pair Plots produces a matrix of relationships 
                     between each variable in your data for an instant 
                     examination of our data]

        Args:
            DataFrame ([type: Pandas DataFrame])
        """
        sns.pairplot(DataFrame)
        plt.show()

    def Simple_Scatter_Plot(self, DataFrame, X: str, Y: str):
        """[summary : Simple Scatter Plot with 2 features]

        Args:
            DataFrame ([type: Pandas DataFrame])
            X ([type: String]): [description: X(Dependent Feature)]
            Y ([type: String]): [description: Y(Independent Feature)]
        """
        sns.scatterplot(data=DataFrame, x=X, y=Y)

    def Heat_Map(self, DataFrame, Width_Of_Plot: int, Height_Of_Plot: int):
        """[summary: Heat Map is a two-dimensional representation of data 
                     in which values are represented by colors]

        Args:
            DataFrame ([type: Pandas DataFrame])
        """

        plt.figure(figsize=(Width_Of_Plot, Height_Of_Plot))
        sns.heatmap(DataFrame.corr(), annot=True)
        plt.show()

    def Numerical_Single_Target_Feature_Pair_Plot(self, DataFrame, Target_Feature: str):
        DataFrame_Features = DataFrame.drop([Target_Feature], axis=1)
        DataFrame_Features = DataFrame_Features.select_dtypes(
            include=np.number)
        DataFrame_Features = DataFrame_Features.columns.values.tolist()

        print(f"Target Feature: {Target_Feature}\n")
        print(f"Numerical Feature:\n {DataFrame_Features}")

        sns.pairplot(data=DataFrame,
                     x_vars=DataFrame_Features,
                     y_vars=[Target_Feature])

        plt.show()

    def Numerical_Single_Target_Feature_Vertical_Pair_Plot_Seaborn(self, DataFrame, Target_Feature: str):
        """[summary: Show All Scatter Plot against the Target Feature VERTICALLY]

        Args:
            DataFrame ([type: Pandas DataFrame])
            Target_Feature (type: str)
        """
        Numerical_DataFrame_Features = DataFrame.drop([Target_Feature], axis=1)
        Numerical_DataFrame_Features = Numerical_DataFrame_Features.select_dtypes(
            include=np.number)
        Numerical_DataFrame_Features = Numerical_DataFrame_Features.columns.values.tolist()

        for Column_Name in Numerical_DataFrame_Features:
            # Setting Plot Title
            plt.title(
                f"{Target_Feature.title()} VS {Column_Name.title()}", weight='bold')
            # Setting Plot X Label
            plt.xlabel(f"{Column_Name.title()}", weight='bold')
            plt.ylabel(f"{Target_Feature.title()}",
                       weight='bold')  # Setting Plot Y Label

            plot = sns.scatterplot(data=DataFrame,
                                   x=Column_Name,
                                   y=Target_Feature)
            plt.show()

    # Plotly Express
    def Plotly_SingleValue_Pie_Plot(self,
                                    DataFrame,
                                    Value: str,
                                    Title: str,
                                    Width: int = 500,
                                    Height: int = 500,
                                    Colors: dict = None,
                                    ):

        temp = pd.DataFrame(DataFrame[Value].value_counts())
        temp.index.name = 'val'
        temp.columns = ['count']
        temp = temp.reset_index()

        fig = px.pie(temp,
                     values="count",
                     names="val",
                     width=Width,
                     height=Height,
                     color=Colors,
                     template='plotly_dark')

        # Altering the fig title alignment
        fig.update_layout(title_text=Title, title_x=0.5)
        fig.show()

    def Plotly_Joined_Area_Plot(self,
                                DataFrame,
                                X: str,
                                Y: str,
                                Title: str,
                                Color: str = None
                                ):

        fig = px.area(DataFrame,
                      x=X,
                      y=Y,
                      title=Title,
                      color=Color,
                      template='plotly_dark')

        # Altering the fig title alignment
        fig.update_layout(title_text=Title, title_x=0.5)
        fig.show()

    def Plotly_Splited_Area_Plot(self,
                                 DataFrame,
                                 X: str,
                                 Y: str,
                                 Title: str,
                                 Facet_Col: str,
                                 Color: str = None
                                 ):

        fig = px.area(DataFrame,
                      x=X,
                      y=Y,
                      title=Title,
                      facet_col=Facet_Col,
                      color='Year',
                      template='plotly_dark'
                      )

        # Altering the fig title alignment
        fig.update_layout(title_text=Title, title_x=0.5)
        fig.show()

    def Plotly_Line_Plot(self,
                         DataFrame,
                         X: str,
                         Y: list,
                         Title: str,
                         Color: str = None):

        fig = px.line(DataFrame,
                      x=X,
                      y=Y,
                      title=Title,
                      template='plotly_dark')

        fig.show()
