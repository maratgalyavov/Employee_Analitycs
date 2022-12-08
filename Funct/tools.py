def cleanup(df01, df02, df03):
    df01.dropna()
    df02.dropna()
    df03.dropna()
    df01["Age"] = df01["Age"].astype("int64")
    df01["DistanceFromHome"] = df01["DistanceFromHome"].astype("int64")
    df01["MonthlyIncome"] = df01["MonthlyIncome"].astype("int64")
    df02 = df02[(df02["age"] > 14) & (df02["age"] < 100)]
    df03.drop(columns=["Country Name", "Country Code"])
    return df01, df02, df03


def modify(df0):
    return df0.assign(increase=lambda x: x.MonthlyIncome * x.PercentSalaryHike * 0.01)
