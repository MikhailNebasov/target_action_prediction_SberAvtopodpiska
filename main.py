from asyncio.windows_events import NULL
import pandas as pd

df_hits = pd.read_csv('E:/Datasets/target_action_prediction_SberAvtopodpiska/ga_hits.csv', usecols = [
    'session_id', 'hit_number', 'hit_page_path', 'event_category', 'event_action'])

df_sessions = pd.read_csv('E:/Datasets/target_action_prediction_SberAvtopodpiska/ga_sessions.csv', usecols = [
    'session_id', 'client_id', 'visit_date', 'visit_time', 'visit_number', 'utm_source', 'utm_medium', 'utm_campaign',
    'utm_adcontent', 'device_category', 'device_brand', 'device_screen_resolution', 'device_browser', 'geo_country',
    'geo_city'], low_memory=False)

df_sessions.utm_source.fillna('ZpYIoDJMcFzVoPFsHGJL', inplace=True)
df_sessions.utm_campaign.fillna('other', inplace=True)
df_sessions.utm_adcontent.fillna('other', inplace=True)
df_sessions.device_brand.fillna('other', inplace=True)

df_full = df_hits.merge(right=df_sessions, on='session_id', how='inner', validate='m:1')
print(df_full.info())
a = df_full[df_full.session_id == '4024492994895054107.1640269084.1640269084']
print(df_full.isna().any())





print(df_hits.head())
