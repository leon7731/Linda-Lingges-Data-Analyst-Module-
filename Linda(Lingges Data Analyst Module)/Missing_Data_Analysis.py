import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


class Missing_Data_Analysis:
    def Check_Missing_Data(self, DataFrame):
        """[summary: Shows the Missing values Overview in the Dataset]

        Args:
             DataFrame ([type: Pandas DataFrame])
        """
        # print(f"Checking missing values: \n{DataFrame.isnull()}\n")
        # print(f"Checking non-missing values: \n{DataFrame.notnull()}\n")
        print(
            f"Only want to know if there are any missing values: \n{DataFrame.isnull().values.any()}\n")
        # print(f"Knowing number of non-missing values for each variable: \n{DataFrame.notnull().sum()}\n")
        print(
            f"Knowing how many missing values in the data: \n{DataFrame.isnull().sum().sum()}\n")

    def Overview_Of_Missing_Data(self, DataFrame):
        """[summary: Show OVERVIEW of the Missing Values & Percentage of it for each column]

        Args:
            DataFrame ([type: Pandas DataFrame])
        """
        Number_Of_NaN = DataFrame.isnull().sum()
        Number_Of_NaN = Number_Of_NaN[Number_Of_NaN > 0].sort_values(
            ascending=False)

        Total_Size_of_Dataframe = len(DataFrame)
        Missing_Data_Overview = pd.DataFrame(columns=["Missing Data Columns",
                                                      "Total Missing Data",
                                                      "Percentage of Missing Data (%)"])

        for Column_Name, Column_Value in Number_Of_NaN.iteritems():
            Missing_Data_Overview = pd.concat([Missing_Data_Overview, pd.DataFrame({
                    Missing_Data_Overview.columns[0]: [Column_Name],
                    Missing_Data_Overview.columns[1]: [Column_Value],
                    Missing_Data_Overview.columns[2]: [round((Column_Value/Total_Size_of_Dataframe * 100), 2)]
                    })],ignore_index=True)

        print(Missing_Data_Overview)

    def Show_Only_MissingData_InColumns(self, DataFrame):
        """[summary: Show ONLY Missing Values of each column]

        Args:
            DataFrame ([type: Pandas DataFrame])
        """
        Number_Of_NaN = DataFrame.isnull().sum()
        Number_Of_NaN = Number_Of_NaN[Number_Of_NaN > 0].sort_values(
            ascending=False)

        print(Number_Of_NaN)

    def Show_Percentage_Of_MissingData_InColumns(self, DataFrame):
        """[summary: Show Percentage ONLY Missing Values of each column]

        Args:
            DataFrame ([type: Pandas DataFrame])
        """
        Percent_NaN = 100 * DataFrame.isnull().sum() / len(DataFrame)
        # Round Up the Answer to 2 Places
        Round_Percent_NaN = round(Percent_NaN, 2)
        Percent_NaN = Round_Percent_NaN[Round_Percent_NaN > 0].sort_values(
            ascending=False)

        print(Percent_NaN)

    def Show_Rows_NaN_Values(self, DataFrame):
        print(
            f"Show rows with one or more NaN values in pandas dataframe: \n{DataFrame[DataFrame.isnull().any(axis=1)]}\n")

    def Plot_Total_Only_MissingData_Columns_Matplotlib(self, DataFrame, Width_Of_Plot: int, Height_Of_Plot: int):
        """[summary: Count & Plot Total Missing Values for each Columns with atleast 1 or more NaN]
            [TIPS: For Large Number of Column Dataset use Width_Of_Plot=10, Height_Of_Plot=20]
        Args:
            DataFrame ([type: Pandas DataFrame])
            Width_Of_Plot (int): [description: Width of the Figure Plot]
            Height_Of_Plot (int): [description: Height of the Figure Plot]
        """
        def Get_MissingData_From_Columns():
            Columns_with_NaN = []
            Count_NaN_each_Column = []
            for Column_Name in (DataFrame.columns.values.tolist()):
                if (DataFrame[Column_Name].isnull().values.any()) == True:
                    Columns_with_NaN.append(Column_Name)
                    Count_NaN_each_Column.append(
                        DataFrame[Column_Name].isnull().sum())

            return Columns_with_NaN, Count_NaN_each_Column

        plt.figure(figsize=(Width_Of_Plot, Height_Of_Plot))
        X_Axis, Y_Axis = Get_MissingData_From_Columns()
        plt.barh(X_Axis, Y_Axis)

        for index, value in enumerate(Y_Axis):
            plt.text(value, index, str(value))

        plt.title("Missing Values of each Columns", weight='bold')
        plt.xlabel("Count of Missing Values", weight='bold')
        plt.ylabel("Missing Values Columns", weight='bold')
        plt.show()

    def Plot_Total_Only_MissingData_Columns_Seaborn(self, DataFrame, Width_Of_Plot: int, Height_Of_Plot: int):
        """[summary: Count & Plot Total Missing Values for each Columns with atleast 1 or more NaN]
        [TIPS: For Large Number of Column Dataset use Width_Of_Plot=10, Height_Of_Plot=20]
        Args:
        DataFrame ([type: Pandas DataFrame])
        Width_Of_Plot (int): [description: Width of the Figure Plot]
        Height_Of_Plot (int): [description: Height of the Figure Plot]
        """
        def Get_MissingData_From_Columns():
            Columns_with_NaN = []
            Count_NaN_each_Column = []
            for Column_Name in (DataFrame.columns.values.tolist()):
                if (DataFrame[Column_Name].isnull().values.any()) == True:
                    Columns_with_NaN.append(Column_Name)
                    Count_NaN_each_Column.append(
                        DataFrame[Column_Name].isnull().sum())

            return Columns_with_NaN, Count_NaN_each_Column

        # Define Plot Size
        plt.figure(figsize=(Width_Of_Plot, Height_Of_Plot))

        X_Axis, Y_Axis = Get_MissingData_From_Columns()
        df = pd.DataFrame(
            {"Column Name": X_Axis, "Count of Missing Values": Y_Axis})
        df = df.sort_values(by=["Count of Missing Values"], ascending=False)

        # Create horizontal barplot
        p = sns.barplot(x="Count of Missing Values",
                        y="Column Name", data=df, ci=None)

        # Show values on barplot
        def show_values(axs, orient="v", space=.01):
            def _single(ax):
                if orient == "v":
                    for p in ax.patches:
                        _x = p.get_x() + p.get_width() / 2
                        _y = p.get_y() + p.get_height() + (p.get_height()*0.01)
                        value = '{:.1f}'.format(p.get_height())
                        ax.text(_x, _y, value, ha="center")
                elif orient == "h":
                    for p in ax.patches:
                        _x = p.get_x() + p.get_width() + float(space)
                        _y = p.get_y() + p.get_height() - (p.get_height()*0.5)
                        value = '{:.0f}'.format(p.get_width())
                        ax.text(_x, _y, value, ha="left")

            if isinstance(axs, np.ndarray):
                for idx, ax in np.ndenumerate(axs):
                    _single(ax)
            else:
                _single(axs)

        show_values(p, "h", space=0.05)

        plt.title("Missing Values of each Columns", weight='bold')
        plt.xlabel("Count of Missing Values", weight='bold')
        plt.ylabel("Missing Values Columns", weight='bold')
        plt.show()

    def Find_Relationship_Between_MissingData_And_TargetFeature(self, DataFrame, TargetFeature: str):
        """[summary: If they are many missing values, we need to find the relationship 
                     between missing values and Target Feature]

        Args:
            DataFrame ([type: : Pandas DataFrame])
            TargetFeature ([type: String]): [description: Target Feature]
        """

        # Here we will check the percentage of nan values present in each feature
        # 1 -step make the list of features which has missing values
        features_with_na = [
            features for features in DataFrame.columns if DataFrame[features].isnull().sum() > 1]

        # 2- step print the feature name and the percentage of missing values
        for feature in features_with_na:
            print(feature, np.round(
                DataFrame[feature].isnull().mean(), 4),  ' % missing values')

        for feature in features_with_na:
            data = DataFrame.copy()
            # let's make a variable that indicates 1 if the observation was missing or zero otherwise
            data[feature] = np.where(data[feature].isnull(), 1, 0)
            # let's calculate the mean SalePrice where the information is missing or present
            data.groupby(feature)[TargetFeature].median().plot.bar()
            plt.title(feature)
            plt.show()
