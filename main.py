import pandas as pd

def get_brand_from_hit_page_path(src):
    if '/cars/all/' in src:
        index = src.find('/cars/all/')
        cutted_str = src[index + 10 : ]
        index = cutted_str.find('/')
        brand = cutted_str[0 : index]
    else:
        brand = 'none'
    return brand


def get_model_from_hit_page_path(src):
    if '/cars/all/' in src:
        index = src.find('/cars/all/')
        cutted_str = src[index + 10 : ]
        index = cutted_str.find('/')
        cutted_str = cutted_str[index + 1 : ]
        index = cutted_str.find('/')
        model = cutted_str[0 : index]
    else:
        model = 'none'
    return model


# Loading of data without features omitted on EDA stage
print('Data loading...')
df_hits = pd.read_csv('E:/Datasets/target_action_prediction_SberAvtopodpiska/ga_hits.csv', usecols = [
    'session_id', 'hit_number', 'hit_page_path', 'event_action'])
df_sessions = pd.read_csv('E:/Datasets/target_action_prediction_SberAvtopodpiska/ga_sessions.csv', usecols = [
    'session_id', 'visit_date', 'visit_time', 'visit_number', 'utm_source', 'utm_medium', 'utm_campaign',
    'utm_adcontent', 'device_category', 'device_brand', 'device_screen_resolution', 'device_browser', 'geo_country',
    'geo_city'], low_memory=False)
print('Data loaded')

# Filling null values in accordance with EDA stage
df_sessions.utm_source.fillna('ZpYIoDJMcFzVoPFsHGJL', inplace=True)
df_sessions.utm_campaign.fillna('other', inplace=True)
df_sessions.utm_adcontent.fillna('other', inplace=True)
df_sessions.device_brand.fillna('other', inplace=True)

# Merging of tables and dropping of session_id
df_full = df_hits.merge(right=df_sessions, on='session_id', how='inner', validate='m:1')
df_full = df_full.drop('session_id', axis=1)

# Constants belong to target actions
TARGET_ACTIONS = ['sub_car_claim_click', 'sub_car_claim_submit_click', 'sub_open_dialog_click', 'sub_custom_question_submit_click',
                  'sub_call_number_click', 'sub_callback_submit_click', 'sub_submit_success', 'sub_car_request_submit_click']

# Transforming of target feature 
df_full.event_action = df_full.event_action.apply(lambda x: 1 if x in TARGET_ACTIONS else 0)
a = df_full[df_full.hit_page_path.str.find('podpiska.sberauto.com/') != -1]
df_full['brand'] = df_full.hit_page_path.apply(get_brand_from_hit_page_path)
df_full['model'] = df_full.hit_page_path.apply(get_model_from_hit_page_path)
df_full['hit_page_path'] = df_full['hit_page_path'].apply(lambda x: '' if '/cars/all/' in x else x)
df_full['hit_page_path'] = df_full['hit_page_path'].apply(lambda x: '' if '/cars?' in x else x)
df_full['hit_page_path'] = df_full['hit_page_path'].apply(lambda x: '' if 'podpiska.sberauto.com' in x else x)



#a = df_full[df_full.session_id == '4024492994895054107.1640269084.1640269084']
a = df_full[df_full.hit_page_path != '']
print(df_full.isna().any())





print(df_hits.head())
