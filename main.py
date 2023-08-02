import pandas as pd

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
df_full = df_hits_agg.merge(right=df_sessions, on='session_id', how='inner')
df_full = df_full.drop('session_id', axis=1)

print(df_full.head())
