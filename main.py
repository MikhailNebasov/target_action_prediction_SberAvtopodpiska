from datetime import datetime
import dill
import pandas as pd
from sklearn.preprocessing import TargetEncoder
from sklearn.model_selection import cross_val_score
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import ColumnTransformer


# Loading of data without features omitted on EDA stage
print('Data loading...')
df_hits = pd.read_csv('E:/Datasets/target_action_prediction_SberAvtopodpiska/ga_hits.csv', usecols = [
    'session_id', 'event_action'])
df_sessions = pd.read_csv('E:/Datasets/target_action_prediction_SberAvtopodpiska/ga_sessions.csv', usecols = [
    'session_id', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_adcontent', 'device_category', 'device_brand',
    'device_screen_resolution', 'device_browser', 'geo_country', 'geo_city'], low_memory=False)
print('Data loaded')

# Constants belong to target actions
TARGET_ACTIONS = ['sub_car_claim_click', 'sub_car_claim_submit_click', 'sub_open_dialog_click', 'sub_custom_question_submit_click',
                  'sub_call_number_click', 'sub_callback_submit_click', 'sub_submit_success', 'sub_car_request_submit_click']

# Transforming of target feature
df_hits.event_action = df_hits.event_action.apply(lambda x: 1 if x in TARGET_ACTIONS else 0)

# Grouping by session_id and getting whether event_action was successful
df_hits_agg = df_hits.groupby('session_id', as_index=False).max()

# Filling null values in accordance with EDA stage
df_sessions.utm_source.fillna('ZpYIoDJMcFzVoPFsHGJL', inplace=True)
df_sessions.utm_campaign.fillna('other', inplace=True)
df_sessions.utm_adcontent.fillna('other', inplace=True)
df_sessions.device_brand.fillna('other', inplace=True)

# Merging of tables and dropping of session_id
df_full = df_hits_agg.merge(right=df_sessions, on='session_id', how='left')
df_full = df_full.drop('session_id', axis=1)
print('Merging of tables performed')

X = df_full.drop(columns=['event_action'], axis=1)
y = df_full['event_action']

categorical_transformer = Pipeline(steps=[
    ('target_encoder', TargetEncoder(cv=7))
    ])

categorical_features = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_adcontent', 'device_category', 'device_brand',
    'device_screen_resolution', 'device_browser', 'geo_country', 'geo_city']

to_engineer_features = ColumnTransformer(transformers=[('categorical', categorical_transformer, categorical_features)])

models = [LogisticRegression(random_state=0, solver='liblinear'), RandomForestClassifier(random_state=0, n_jobs=12),
    MLPClassifier(random_state=0, hidden_layer_sizes=(100, 50))]

preprocessor = Pipeline(steps=[('to_engineer_features', to_engineer_features),])

best_score = 0.0
best_pipe = None
for model in models:
    pipe = Pipeline(steps=[('preprocessor', preprocessor), ('model', model)])

    score = cross_val_score(pipe, X, y, cv=5, scoring='roc_auc')
    print(f'model: {type(model).__name__}, acc_mean: {score.mean():.4f}, acc_std: {score.std():.4f}')

    if score.mean() > best_score:
        best_score = score.mean()
        best_pipe = pipe

best_pipe.fit(X, y)
print(f'best model: {type(best_pipe.named_steps["model"]).__name__}, accuracy: {best_score:.4f}')

file_name = 'best_pipe.pkl'
with open(file_name, 'wb') as file:
    dill.dump({
        'model':best_pipe,
        'metadata':{
            'name':'Target action prediction model',
            'author':'Mikhail Nebasov',
            'version':'1.0.0',
            'date':datetime.now(),
            'type':type(best_pipe.named_steps['model']).__name__,
            'accuracy':best_score
            }
        }, file)