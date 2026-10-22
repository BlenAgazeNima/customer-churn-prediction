def churn_rate(df,column):
    summary=df.groupby(column).agg(
        Total_Customers=('Churn Value', 'count'),
        Churn_Count=('Churn Value', 'sum'),
        Churn_rate=('Churn Value', 'mean') 
    )
    summary['Churn_rate']=(summary['Churn_rate']*100).round(2)
    return summary.sort_values('Churn_rate',ascending=False)
