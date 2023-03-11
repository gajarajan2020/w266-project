import pandas as pd

df = pd.read_csv(r'../data/sample-data.csv')

def clean_alt_list(list_):
    list_ = list_.replace(', ', '","')
    list_ = list_.replace('[', '["')
    list_ = list_.replace(']', '"]')
    return list_
df['auth_merch_name'] = df['auth_merch_name'].str.split()
df['auth_merch_name'].apply(clean_alt_list)

def parseList(index, list_):
    try:
        if len(list_[index]) > 2:
            return list_[index].replace('*','').replace('www.','').capitalize().replace('.com','').replace('/bill','').replace('\t','').replace('Amzn','Amazon')
    except:
        pass


df['merchant_name_1'] = df['auth_merch_name'].apply(lambda x: parseList(0,x))
df['merchant_name_2'] = df['auth_merch_name'].apply(lambda x: parseList(1,x))
df['merchant_name_3'] = df['auth_merch_name'].apply(lambda x: parseList(2,x))
df['merchant_name_4'] = df['auth_merch_name'].apply(lambda x: parseList(3,x))
df['merchant_name_5'] = df['auth_merch_name'].apply(lambda x: parseList(4,x))
df['merchant_name_6'] = df['auth_merch_name'].apply(lambda x: parseList(5,x))

df.to_csv('output_sample-data.csv')
