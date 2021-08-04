import numpy as np
import pandas as pd

def merge_index(bunjang_index,joongabi_index,mintit_index,price_list,phone_list):
    
    join_keys = ['pattern','storage'] #모델명으로 데이터 조인
    b_merge = bunjang_index.drop('id',axis=1).astype({'storage': 'str'})
    j_merge = joongabi_index.drop('id',axis=1).fillna(0).astype({'storage': 'str'})
    m_merge = mintit_index.fillna(0).astype({'storage': 'str'})
    p_merge = price_list.drop(['price_id','model_name','price'],axis=1).rename(columns={'model_code':'price_list_key'})
    df_OUTER_JOIN = pd.merge(b_merge, j_merge, left_on=join_keys, right_on=join_keys, how='outer')
    df_OUTER_JOIN = pd.merge(df_OUTER_JOIN,m_merge, left_on=join_keys, right_on=join_keys, how='outer')
    df_OUTER_JOIN = pd.merge(df_OUTER_JOIN,p_merge, left_on=join_keys, right_on=join_keys, how='outer')
    # display(df_OUTER_JOIN)
    result = df_OUTER_JOIN.drop(['name','brand_id_x','brand_name_x','model_id_x','model_name_x','id','generation','retail_price',
                                'brand_id_y','brand_name_y','model_id_y','model_name_y'],axis=1)
    result = result[['pattern', 'storage', 'key','model_code','mintit_key','price_list_key']]
    result = result.fillna(0)
    result = result.astype({'storage': 'str'})
    result = result.rename(columns={'key':'번장키','model_code':'중가비키','mintit_key':'민팃키'})
    result = result.replace(0,np.NAN).drop_duplicates()
    # display(result)
    result_for_join = result.rename(columns={'pattern':'pl_model_code'})
    result_for_join = pd.merge(result_for_join,phone_list, left_on='pl_model_code', right_on='pl_model_code', how='inner')
    # display(result_for_join[['pl_id','pl_model_name','pl_model_code','storage' ,'번장키', '중가비키','민팃키']].replace(0,np.NaN))
    result_for_join = result_for_join[['pl_model_code','storage' ,'민팃키', '번장키','중가비키','price_list_key']].replace(0,np.NaN)

    result_for_join.columns = ['original_code', 'storage', 'mintit_code','bunjang_code','joongabi_code','price_code']
    result_for_join = result_for_join.replace("0",np.NAN)

    result_for_join

    return result_for_join