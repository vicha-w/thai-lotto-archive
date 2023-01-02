import os, glob
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"data": "Hello,World"}

@app.get("/latest")
def get_lotto_latest():
    files = glob.glob('./lottonumbers/2022-12-30.txt')
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
    print(rows)
    return JSONResponse(content=rows[0])

@app.get("/date/{date_id}")
def get_lotto_date(date_id: str):
    the_file = """./lottonumbers/{0}.txt""".format(date_id)
    files = glob.glob(the_file)
    files = sorted(files)
    rows = []

    need_dtypes = [
        'FIRST',
        'TWO',
        'THREE',
        'THREE_FIRST',
        'THREE_LAST'
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
    print(rows)
    return JSONResponse(content=rows[0])