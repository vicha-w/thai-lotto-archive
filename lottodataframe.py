import os, glob
import pandas as pd

def get_lotto_df():
    files = glob.glob('./lottonumbers/*.txt')
    files = sorted(files)
    rows = []

    need_dtypes = [
        'FIRST',
        'TWO',
        'THREE',
        'THREE_FIRST',
        'THREE_LAST',
    ]
    for file in files:
        
        date = os.path.basename(file).replace('.txt', '')
        
        with open(file, 'r') as f:
            lines = [l.strip() for l in f.readlines()]

        row = {'date': date}
        for line in lines[1:]:
            data = line.split()
            
            dtype = data[0]
            if dtype not in need_dtypes:
                continue
            
            dtype = dtype.lower()
            if len(data) > 2:
                for i, d in enumerate(data[1:]):
                    row[dtype + '_' + str(i + 1)] = d
            else:
                row[dtype] = data[1]
        
        
        rows.append(row)

    # Create Pandas dataframe
    df = pd.DataFrame(rows)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    df.index = df['date']
    df['day'] = df.index.day
    df['month'] = df.index.month
    df['year'] = df.index.year

    return df