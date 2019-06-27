import pandas as pd
import numpy as np
from flask import jsonify
from sklearn.preprocessing import Normalizer, MaxAbsScaler
from sklearn.impute import SimpleImputer
from sklearn.decomposition import NMF
from sklearn.pipeline import make_pipeline
import pickle
from os import path


dir_path = 'data/'


def get_data(file_name):
    """returns dataframe from the file_name string"""

    return pd.read_csv(path.join(dir_path + file_name))


wine_ratings_df = get_data("reviews.csv")
wine_ratings_df = wine_ratings_df.drop(['id','Unnamed: 0', 'comment'], axis=1)


def get_df_info(df):
    print(df.head())
    print('')
    print(df.columns)
    print('')
    print(df.shape)
    print('')
    print(df.info())
    print('')
    return None


# massage data to get it into correct format

def product_user_matrix(dataframe):
    df = dataframe.pivot_table(index='wine_id', columns='username')
    df.columns = df.columns.droplevel().rename(None)
    df.reset_index(inplace=True)
    return df


user_prod_df = product_user_matrix(wine_ratings_df)


imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
scaler = MaxAbsScaler()
nmf = NMF(n_components=3)
normalizer = Normalizer()
pipeline = make_pipeline(imp, scaler, nmf, normalizer)

norm_features = pipeline.fit_transform(user_prod_df.values)
factorized = pd.DataFrame(norm_features, index=user_prod_df.wine_id)

factorized.to_csv('nmf_features')

