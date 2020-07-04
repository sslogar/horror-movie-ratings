from joblib import load
import os.path

filename='gridsearchreg.joblib'
if os.path.isfile(filename):
    model=load(filename)
else:
    print("File not in directory")
