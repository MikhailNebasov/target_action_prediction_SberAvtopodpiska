import pandas as pd
"""
import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

out = []

df_temp = pd.read_csv('E:/Datasets/target_action_prediction_SberAvtopodpiska/result.csv')
for i in range(len(df_temp)):
    driver.get('https://sberauto.com/cars/' + df_temp['keys'][i])
    get_url = driver.current_url
    if ' 404 ' in driver.title:
        out.append('0')
    else:
        out.append(get_url)
    time.sleep(2.7)

driver.quit()

df_out = pd.DataFrame(list(zip(df_temp['keys'], out)), columns=['keys', 'path'])
df_out.to_csv('result.csv', index=False)
"""
"""
# Repairing hit page path
def repair_hit_page_path(src):
    if '/cars/all' not in src:
        if '/cars/' in src:
            pos = src.find('/cars/')
            sea = src[pos : pos + 14]
            res = df_repair[df_repair['keys'] == sea]
            if len(res) > 0:
                src = res['path']
    return src


# Getting brand from path
def get_brand_from_hit_page_path(src):
    if '/cars/all/' in src:
        index = src.find('/cars/all/')
        cutted_str = src[index + 10 : ]
        index = cutted_str.find('/')
        brand = cutted_str[0 : index]
    else:
        if '/cars/bmw' in src:
            brand = 'bmw'
        elif '/cars/lamborghini' in src:
            brand = 'lamborghini'
        elif '/cars/opel' in src:
            brand = 'opel'
        elif '/cars/hawtai' in src:
            brand = 'hawtai'
        elif '/cars/mazda' in src:
            brand = 'mazda'
        elif '/cars/subaru' in src:
            brand = 'subaru'
        elif '/cars/ford' in src:
            brand = 'ford'
        elif '/cars/geely' in src:
            brand = 'geely'
        elif '/cars/audi' in src:
            brand = 'audi'
        elif '/cars/nissan' in src:
            brand = 'nissan'
        elif '/cars/acura' in src:
            brand = 'acura'
        elif '/cars/honda' in src:
            brand = 'honda'
        elif '/cars/scion' in src:
            brand = 'scion'
        elif '/cars/great-wall' in src:
            brand = 'great-wall'
        elif '/cars/peugeot' in src:
            brand = 'peugeot'
        elif '/cars/rolls-royce' in src:
            brand = 'rolls-royce'
        elif '/cars/lexus' in src:
            brand = 'lexus'
        elif '/cars/foton' in src:
            brand = 'foton'
        elif '/cars/suzuki' in src:
            brand = 'suzuki'
        elif '/cars/ravon' in src:
            brand = 'ravon'
        elif '/cars/uaz' in src:
            brand = 'uaz'
        elif '/cars/volvo' in src:
            brand = 'volvo'
        elif '/cars/asia' in src:
            brand = 'asia'
        elif '/cars/haval' in src:
            brand = 'haval'
        elif '/cars/daewoo' in src:
            brand = 'daewoo'
        elif '/cars/zaz' in src:
            brand = 'zaz'
        elif '/cars/skoda' in src:
            brand = 'skoda'
        elif '/cars/kia' in src:
            brand = 'kia'
        elif '/cars/porsche' in src:
            brand = 'porsche'
        elif '/cars/toyota' in src:
            brand = 'toyota'
        elif '/cars/lifan' in src:
            brand = 'lifan'
        elif '/cars/jeep' in src:
            brand = 'jeep'
        elif '/cars/citroen' in src:
            brand = 'citroen'
        elif '/cars/saab' in src:
            brand = 'saab'
        elif '/cars/faw' in src:
            brand = 'faw'
        elif '/cars/bentley' in src:
            brand = 'bentley'
        elif '/cars/renault' in src:
            brand = 'renault'
        elif '/cars/?rent' in src:
            brand = 'none'
        elif '/cars/datsun' in src:
            brand = 'datsun'
        elif '/cars/buick' in src:
            brand = 'buick'
        elif '/cars/chery?' in src:
            brand = 'chery'
        elif '/cars/chery/' in src:
            brand = 'chery'
        elif '/cars/mini' in src:
            brand = 'mini'
        elif '/cars/fiat' in src:
            brand = 'fiat'
        elif '/cars/tesla' in src:
            brand = 'tesla'
        elif '/cars/hummer' in src:
            brand = 'hummer'
        elif '/cars/rover' in src:
            brand = 'rover'
        elif '/cars/ij' in src:
            brand = 'ij'
        elif '/cars/mercedes-benz' in src:
            brand = 'mercedes-benz'
        elif '/cars/jaguar' in src:
            brand = 'jaguar'
        elif '/cars/daihatsu' in src:
            brand = 'daihatsu'
        elif '/cars/dw-hower' in src:
            brand = 'dw-hower'
        elif '/cars/byd' in src:
            brand = 'byd'
        elif '/cars/dodge' in src:
            brand = 'dodge'
        elif '/cars/maserati' in src:
            brand = 'maserati'
        elif '/cars/hyundai' in src:
            brand = 'hyundai'
        elif '/cars/genesis' in src:
            brand = 'genesis'
        elif '/cars/mitsubishi' in src:
            brand = 'mitsubishi'
        elif '/cars/jac' in src:
            brand = 'jac'
        elif '/cars/gac' in src:
            brand = 'gac'
        elif '/cars/ssangyong' in src:
            brand = 'ssangyong'
        elif '/cars/dacia' in src:
            brand = 'dacia'
        elif '/cars/vortex' in src:
            brand = 'vortex'
        elif '/cars/gaz' in src:
            brand = 'gaz'
        elif '/cars/lada-vaz' in src:
            brand = 'lada-vaz'
        elif '/cars/lada_(vaz)' in src:
            brand = 'lada-vaz'
        elif '/cars/changan' in src:
            brand = 'changan'
        elif '/cars/seat' in src:
            brand = 'seat'
        elif '/cars/smart' in src:
            brand = 'smart'
        elif '/cars/lincoln' in src:
            brand = 'lincoln'
        elif '/cars/brilliance' in src:
            brand = 'brilliance'
        elif '/cars/iran-khodro' in src:
            brand = 'iran-khodro'
        elif '/cars/alfa-romeo' in src:
            brand = 'alfa-romeo'
        elif '/cars/volkswagen' in src:
            brand = 'volkswagen'
        elif '/cars/dongfeng' in src:
            brand = 'dongfeng'
        elif '/cars/land-rover' in src:
            brand = 'land-rover'
        elif '/cars/chevrolet' in src:
            brand = 'chevrolet'
        elif '/cars/chrysler' in src:
            brand = 'chrysler'
        elif '/cars/haima' in src:
            brand = 'haima'
        elif '/cars/cadillac' in src:
            brand = 'cadillac'
        elif '/cars/infiniti' in src:
            brand = 'infiniti'
        else:
            brand = 'none'
    return brand


#  Getting model from path
def get_model_from_hit_page_path(src):
    if '/cars/all/' in src:
        index = src.find('/cars/all/')
        cutted_str = src[index + 10 : ]
        index = cutted_str.find('/')
        cutted_str = cutted_str[index + 1 : ]
        index = cutted_str.find('/')
        model = cutted_str[0 : index]
    else:
        if '/cars/bmw/' in src:
            index = src.find('/cars/bmw/')
            cutted_str = src[index + 10 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/opel/' in src:
            index = src.find('/cars/opel/')
            cutted_str = src[index + 11 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/mazda/' in src:
            index = src.find('/cars/mazda/')
            cutted_str = src[index + 12 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/subaru/' in src:
            index = src.find('/cars/subaru/')
            cutted_str = src[index + 13 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/ford/' in src:
            index = src.find('/cars/ford/')
            cutted_str = src[index + 11 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/geely/' in src:
            index = src.find('/cars/geely/')
            cutted_str = src[index + 12 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/audi/' in src:
            index = src.find('/cars/audi/')
            cutted_str = src[index + 11 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/nissan/' in src:
            index = src.find('/cars/nissan/')
            cutted_str = src[index + 13 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/acura/' in src:
            index = src.find('/cars/acura/')
            cutted_str = src[index + 12 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/honda/' in src:
            index = src.find('/cars/honda/')
            cutted_str = src[index + 12 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/great-wall/' in src:
            index = src.find('/cars/great-wall/')
            cutted_str = src[index + 17 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/peugeot/' in src:
            index = src.find('/cars/peugeot/')
            cutted_str = src[index + 14 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/lexus/' in src:
            index = src.find('/cars/lexus/')
            cutted_str = src[index + 12 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/suzuki/' in src:
            index = src.find('/cars/suzuki/')
            cutted_str = src[index + 13 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/ravon/' in src:
            index = src.find('/cars/ravon/')
            cutted_str = src[index + 12 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/uaz/' in src:
            index = src.find('/cars/uaz/')
            cutted_str = src[index + 10 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/volvo/' in src:
            index = src.find('/cars/volvo/')
            cutted_str = src[index + 12 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/haval/' in src:
            index = src.find('/cars/haval/')
            cutted_str = src[index + 12 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/daewoo/' in src:
            index = src.find('/cars/daewoo/')
            cutted_str = src[index + 13 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/skoda/' in src:
            index = src.find('/cars/skoda/')
            cutted_str = src[index + 12 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/kia/' in src:
            index = src.find('/cars/kia/')
            cutted_str = src[index + 10 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/porsche/' in src:
            index = src.find('/cars/porsche/')
            cutted_str = src[index + 14 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/toyota/' in src:
            index = src.find('/cars/toyota/')
            cutted_str = src[index + 13 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/lifan/' in src:
            index = src.find('/cars/lifan/')
            cutted_str = src[index + 12 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/jeep/' in src:
            index = src.find('/cars/jeep/')
            cutted_str = src[index + 11 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/qashqai' in src:
            model = 'qashqai'
        elif '/cars/highlander' in src:
            model = 'highlander'
        elif '/cars/santa-fe' in src:
            model = 'santa-fe'
        elif '/cars/h6' in src:
            model = 'h6'
        elif '/cars/g80' in src:
            model = 'g80'
        elif '/cars/granta' in src:
            model = 'granta'
        elif '/cars/es' in src:
            model = 'es'
        elif '/cars/?rent' in src:
            model = 'none'
        elif '/cars/citroen/' in src:
            index = src.find('/cars/citroen/')
            cutted_str = src[index + 14 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/bentley/' in src:
            index = src.find('/cars/bentley/')
            cutted_str = src[index + 14 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/renault/' in src:
            index = src.find('/cars/renault/')
            cutted_str = src[index + 14 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/datsun/' in src:
            index = src.find('/cars/datsun/')
            cutted_str = src[index + 13 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/chery/' in src:
            index = src.find('/cars/chery/')
            cutted_str = src[index + 12 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/mini/' in src:
            index = src.find('/cars/mini/')
            cutted_str = src[index + 11 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/fiat/' in src:
            index = src.find('/cars/fiat/')
            cutted_str = src[index + 11 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/tesla/' in src:
            index = src.find('/cars/tesla/')
            cutted_str = src[index + 12 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/mercedes-benz/' in src:
            index = src.find('/cars/mercedes-benz/')
            cutted_str = src[index + 20 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/jaguar/' in src:
            index = src.find('/cars/jaguar/')
            cutted_str = src[index + 13 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/dodge/' in src:
            index = src.find('/cars/dodge/')
            cutted_str = src[index + 12 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/hyundai/' in src:
            index = src.find('/cars/hyundai/')
            cutted_str = src[index + 14 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/genesis/' in src:
            index = src.find('/cars/genesis/')
            cutted_str = src[index + 14 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/mitsubishi/' in src:
            index = src.find('/cars/mitsubishi/')
            cutted_str = src[index + 17 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/gac/' in src:
            index = src.find('/cars/gac/')
            cutted_str = src[index + 10 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/ssangyong/' in src:
            index = src.find('/cars/ssangyong/')
            cutted_str = src[index + 16 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/lada-vaz/' in src:
            index = src.find('/cars/lada-vaz/')
            cutted_str = src[index + 15 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/lada_(vaz)/' in src:
            index = src.find('/cars/lada_(vaz)/')
            cutted_str = src[index + 17 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/changan/' in src:
            index = src.find('/cars/changan/')
            cutted_str = src[index + 14 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/alfa-romeo/' in src:
            index = src.find('/cars/alfa-romeo/')
            cutted_str = src[index + 17 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/volkswagen/' in src:
            index = src.find('/cars/volkswagen/')
            cutted_str = src[index + 17 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/land-rover/' in src:
            index = src.find('/cars/land-rover/')
            cutted_str = src[index + 17 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/chevrolet/' in src:
            index = src.find('/cars/chevrolet/')
            cutted_str = src[index + 16 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/cadillac/' in src:
            index = src.find('/cars/cadillac/')
            cutted_str = src[index + 15 : ]
            index = cutted_str.find('?')
            model = cutted_str[0 : index]
        elif '/cars/infiniti/' in src:
            index = src.find('/cars/infiniti/')
            cutted_str = src[index + 15 : ]
            index = cutted_str.find('?')
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
df_repair = pd.read_csv('E:/Datasets/target_action_prediction_SberAvtopodpiska/for_repair.csv', sep='\t')
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
df_full['hit_page_path'] = df_full['hit_page_path'].apply(repair_hit_page_path).astype(str)
df_full['brand'] = df_full.hit_page_path.apply(get_brand_from_hit_page_path).astype(str)
df_full['model'] = df_full.hit_page_path.apply(get_model_from_hit_page_path).astype(str)
df_full = df_full.drop('hit_page_path', axis=1)
"""

"""
a = df_full[df_full.hit_page_path != '']
keys = set()
for elem in a['hit_page_path']:
    pos = elem.find('/cars/')
    data = elem[pos + 6 : pos + 14]
    keys.add(data)

df_out = pd.DataFrame(list(keys), columns=['keys'])
df_out.to_csv('result.csv', index=False)
"""
"""
df_full.to_parquet('E:/Datasets/target_action_prediction_SberAvtopodpiska/merged_wo_hpp.parquet', index=False)
"""

df_full = pd.read_parquet('E:/Datasets/target_action_prediction_SberAvtopodpiska/merged_wo_hpp.parquet')
print(df_full.head())
