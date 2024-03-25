import  pandas as pd
import numpy as np
data = pd.read_csv('D:\data.tsv', sep='\t')


def cau1():
    print(data.head(5))


def cau2():
    print(data.shape)


def cau3():
    print(data.columns)


def cau4():
    return 'object'


def cau5():
    country = data.get('country')
    for i in range(5):
        print(country[i])


def cau6():
    country = data.get('country')
    for i in range(len(country)-6, len(country)-1):
        print(country[i])


def cau7():
    print(data[['country', 'continent', 'year']].head(5))
    print(data[['country', 'continent', 'year']].tail(5))


def cau8():
    print(data.iloc[0,:])
    print(data.iloc[100])


def cau9():
    print(data.iloc[:,0])
    print(data.iloc[:,len(data.columns)-1])


def cau10():
    print(data.loc[len(data)-1])


def cau11():
    print(data.iloc[1])
    print(data.iloc[100])
    print(data.iloc[1000])


def cau12():
    print(data.iloc[43, 0])


def cau13():
    print(data.iloc[1, 0])
    print(data.iloc[100, 3])
    print(data.iloc[1000, 5])


def cau14():
    print(data.head(10))


def cau15():
    print(int(data['year'].mean()))


def cau16():
    ages = data['year']
    print(ages.mean())


def cau17():
    s = pd.Series(['banana', 42])
    return s


def cau18():
    s = pd.Series(['Wes MCKinney', 'Creator of Pandas'], index=['Person', 'Who'])
    return s


def cau19():
    dict = {'Occupation':['Chemist', 'Statistician'], 'Born': ['1920-07-25', '1876-06-13']
        , 'Died':['1958-04-16', '1937-10-16'], 'Age': [37, 61]}
    df = pd.DataFrame(dict, index=['Franklin','Gosset'])
    return df

if __name__ == '__main__':
    print(cau19())