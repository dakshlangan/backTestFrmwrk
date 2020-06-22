def createEntryRates(df,positionCol='positions',ratesCol = 'rates'):
    """Creates entry rates col for a give dataframe containing cols positions and rates."""
    df['entryRate'] = 0.0
    entryRate = 0.0
    for idx, row in df.iterrows():
        if row[positionCol] == 1.0:
            entryRate = row[ratesCol]
            df.loc[idx,'entryRate'] = entryRate
        elif row[positionCol] == -1.0:
            df.loc[idx,'entryRate'] = entryRate
            entryRate = 0.0
        else:
            df.loc[idx,'entryRate'] = entryRate
    return df