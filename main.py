import pandas as pd

# Loading of data without features omitted on EDA stage
print('Data loading...')
df_hits = pd.read_csv('E:/Datasets/target_action_prediction_SberAvtopodpiska/ga_hits.csv', usecols = [
    'session_id', 'hit_number', 'hit_page_path', 'event_action'])
df_sessions = pd.read_csv('E:/Datasets/target_action_prediction_SberAvtopodpiska/ga_sessions.csv', usecols = [
    'session_id', 'client_id', 'visit_date', 'visit_time', 'visit_number', 'utm_source', 'utm_medium', 'utm_campaign',
    'utm_adcontent', 'device_category', 'device_brand', 'device_screen_resolution', 'device_browser', 'geo_country',
    'geo_city'], low_memory=False)
print('Data loaded')

# Filling null values in accordance with EDA stage
df_sessions.utm_source.fillna('ZpYIoDJMcFzVoPFsHGJL', inplace=True)
df_sessions.utm_campaign.fillna('other', inplace=True)
df_sessions.utm_adcontent.fillna('other', inplace=True)
df_sessions.device_brand.fillna('other', inplace=True)

# Merging of tables
df_full = df_hits.merge(right=df_sessions, on='session_id', how='inner', validate='m:1')

# Constants belong to target actions
TARGET_ACTIONS = ['sub_car_claim_click', 'sub_car_claim_submit_click', 'sub_open_dialog_click', 'sub_custom_question_submit_click',
                  'sub_call_number_click', 'sub_callback_submit_click', 'sub_submit_success', 'sub_car_request_submit_click']

# Transforming of target feature
df_full.event_action = df_full.event_action.apply(lambda x: 1 if x in TARGET_ACTIONS else 0)


#a = df_full[df_full.session_id == '4024492994895054107.1640269084.1640269084']
a = df_full[df_full.event_action == 1]
print(df_full.isna().any())





print(df_hits.head())
