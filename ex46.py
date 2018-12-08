try:    
from setuptools import setup except ImportError:    
from distutils.core import setup config = {    'description': 
'My Project',    
'author': 'My Name',    
'url': 'URL to get it at.',    
'download_url': 'Where to download it.',    
'author_email': 'My email.',    'version': '0.1',    
'install_requires': ['nose'],    'packages': ['NAME'],    
'scripts': [],    'name': 'projectname' } 
setup(**config)




wget https://www.dropbox.com/s/xtms9g31aicstvv/train.csv?dl=1


plot(arange(5))

import pandas as pd

import numpy as np
import matplotlib as plt
%matplotlib inline

df = pd.read_csv("/home/kunal/Downloads/Loan_Prediction/train.csv") #Reading the dataset in a dataframe using 
Pandas

df['Property_Area'].value_counts()