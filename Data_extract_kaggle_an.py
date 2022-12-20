
#Data extract

#Extract employee from kaggle
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()
api.dataset_download_files('threnjen/2019-airline-delays-and-cancellations')


# extract zip file

from zipfile import ZipFile
with ZipFile( 'C:\\Users\\anjaly\\2019-airline-delays-and-cancellations.zip','r') as zip_object:
    zip_object.extractall("C:\\Users\\anjaly\\Data")
    