import pandas as pd


class Feature_Engineering():

    def Covert_Column_To_DatetimeObject(self, DataFrame, TimeFrameColumnName: str):
        DataFrame[TimeFrameColumnName] = pd.to_datetime(
            DataFrame[TimeFrameColumnName])
        return DataFrame

    def Add_Year_Column(self, DataFrame, NewYearColumnName: str, ColumnName: str):
        DataFrame[NewYearColumnName] = DataFrame[ColumnName].dt.year
        return DataFrame

    def Add_Month_Column(self, DataFrame, MonthColumnName: str, ColumnName: str):
        DataFrame[MonthColumnName] = DataFrame[ColumnName].dt.month
        return DataFrame

    def Add_Date_Column(self, DataFrame, DateColumnName: str, ColumnName: str):
        DataFrame[DateColumnName] = DataFrame[ColumnName].dt.date
        return DataFrame

    def Add_DayOfWeek_Column(self, DataFrame, DayOfWeekColumnName: str, ColumnName: str):
        DataFrame[DayOfWeekColumnName] = DataFrame[ColumnName].dt.day_name()
        return DataFrame
    
    def Add_Time_Column(self, DataFrame, TimeColumnName: str, ColumnName: str):
        DataFrame[TimeColumnName] = DataFrame[ColumnName].dt.time
        return DataFrame
    
    def Add_MovingAverage_Column(self, DataFrame, ColumnName: str):
        DataFrame['MA48'] = DataFrame[ColumnName].rolling(48).mean()
        DataFrame['MA336'] = DataFrame[ColumnName].rolling(336).mean()
        return DataFrame

    def Sort_Datetime_Column_PerDate(self, DataFrame, ColumnName: str):
        DataFrame = DataFrame.sort_values(by=ColumnName)
        return DataFrame
    
  

    def Substitute_Single_Column(self, Dataframe, ColumnName: str, Substitution: dict):
        """_summary_: Substitute the single column with the given substitution.

        Args:
            Dataframe (_type_):
            ColumnName (str)_: 
            Substitution (dict):

        Returns:
            _type_: _description_
        """
        df = Dataframe
        df[ColumnName].replace(Substitution, inplace=True)

        return df

    def Filter_Rows_By_ColumnName(self, Dataframe, ColumnName: str, Value: list):
        df = Dataframe[Dataframe[ColumnName].isin(Value)]
        return df
