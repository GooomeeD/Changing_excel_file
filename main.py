import os

import pandas as pd

path = '/Users/20146403/Desktop/Банкротства /Банкротства .xlsx'

b = pd.read_excel(path, sheet_name='Лист1', engine='openpyxl' )

dic = []
dic1 = []

vstrPrefDev = "LAB02D"  # префикс Dev
vstrPrefPre = "LAB02P"  # префикс ПреПром
vstrPrefProm = "MISPLT"  # префикс Пром

TGT_SYS_CODE_LAB = "MIS3_MISDEV_GPSMD_W"  # таргет система для лабы
TGT_SYS_CODE_PROM = "MIS3_MISPLT_GPSMD_W"  # таргет система для прома

TGT_OWN_NM_LAB = "s_grnplm_ld_fin_mis3_misdev_smd"  # таргет схема для лабы
TGT_OWN_NM_PROM = "s_grnplm_as_fin_mis3_misplt_smd"  # таргет схема для прома

vstr_SUBSCR_ID_DETAIL_DEV = "f85b614a-0fd3-415b-b147-63c1be127416"  # ID подписки DETAIL DEV
vstr_SUBSCR_ID_DETAIL_PREPROM = "3f437bbb-150a-4076-bfef-641896b5ead5"  # ID подписки DETAIL PreProm
vstr_SUBSCR_ID_DETAIL_PROM = "e4b5033c-aa1e-476b-b9ec-4e143b946b3d"  # ID подписки DETAIL Prom

vstr_SUBSCR_ID_CRED_COA_DEV = "ad763fa9-2007-4c52-8d4b-1e3f55a9ef5d"  # ID подписки CRED_COA DEV
vstr_SUBSCR_ID_CRED_COA_PREPROM = "1b5ea35f-d257-4aa7-99db-9f502e25abee"  # ID подписки CRED_COA PreProm
vstr_SUBSCR_ID_CRED_COA_PROM = "0610a451-f94a-4080-9999-e9f88ea0b032"  # ID подписки CRED_COA Prom

vstr_SUBSCR_ID_MAIN1_DEV = "77786919-a339-4111-bc53-3481423684b8"  # ID подписки MAIN1 DEV
vstr_SUBSCR_ID_MAIN1_PREPROM = "04a36562-d300-49ec-9ac7-748b144877d9"  # ID подписки MAIN1 PreProm
vstr_SUBSCR_ID_MAIN1_PROM = "3e25dd83-ec25-47a9-9017-6cf406d2da6f"  # ID подписки MAIN1 Prom

vstr_SUBSCR_ID_MAIN2_DEV = "3dd15a33-fe76-4bc5-961c-32d56f9e6c43"  # ID подписки MAIN2 DEV
vstr_SUBSCR_ID_MAIN2_PREPROM = "29a287dd-c19e-46c4-9a1e-3e4c21b8d4eb"  # ID подписки MAIN2 PreProm
vstr_SUBSCR_ID_MAIN2_PROM = "6ee79416-ce54-4e96-8ccd-04bd3417e87d"  # ID подписки MAIN2 Prom

vstr_SUBSCR_ID_OPTN_DEV = "78f22137-e2c0-4eda-914a-1f4121ffdd79"  # ID подписки OPTN DEV
vstr_SUBSCR_ID_OPTN_PREPROM = "7f626b18-23af-4c71-9712-899458ed24ae"  # ID подписки OPTN PreProm
vstr_SUBSCR_ID_OPTN_PROM = "fe224477-056c-4cde-8b7a-a7bcd9f9a900"  # ID подписки OPTN Prom

vstr_SUBSCR_ID_OPTN_H_DEV = "eca7b83d-de82-4cba-8a3a-767d232ac4fc"  # ID подписки OPTN_H DEV
vstr_SUBSCR_ID_OPTN_H_PREPROM = "333bd05a-775f-4b27-8ba9-3c19c165476c"  # ID подписки OPTN_H PreProm
vstr_SUBSCR_ID_OPTN_H_PROM = "519dac2c-8025-48c2-a46d-b3cf91ea9a03"  # ID подписки OPTN_H Prom

vstr_SUBSCR_ID_RDM_DEV = "9616402b-5507-4a22-ab75-7e175527fc74"  # ID подписки RDM DEV
vstr_SUBSCR_ID_RDM_PREPROM = "c45c570d-29c2-4a1d-84d4-932444e2c7de"  # ID подписки RDM PreProm
vstr_SUBSCR_ID_RDM_PROM = "22d3d992-1399-47eb-966e-c83e83563f19"  # ID подписки RDM Prom


ST = {

}

# class Folder:
#
#     p = input('Folder name:')
#     path = os.listdir()
#
#     input_data= {
#
#     }
#
#     def lif(self):  # Lists in file
#         h = pd.ExcelFile(Folder.path, engine='openpyxl')
#         l = len(h.sheet_names)
#         return l
#
#     def framing(self, data):
#         self.df = pd.DataFrame(data)
#         return self.df
#
#     def saving(self, data, name):
#         data.to_excel(f'{name}.xlsx')


def list_of_copies(data):
    # if type(data)!=
    ST = pd.DataFrame(data)
    PreProm = pd.DataFrame(data)
    Prom = pd.DataFrame(data)
    k = [ST, PreProm, Prom]
    return k

# def formatting_lists()

def framing(data):
    df = pd.DataFrame(data)
    return df

def replacing(data, p, r):
    if type(data) != 'pandas.core.frame.DataFrame':
        t = framing(data)
    t = t.replace(p, r, regex=True)
    return t

def saving(data, name):
    data.to_excel(f'{name}.xlsx')

# for i in range(len(dict)):
#     b = replacing(b, dic[i], dic_1[i])



changes = [1, 4, 5, 7, 8, 10]

#Для среды ПреПром
preprom_file = {
    vstr_SUBSCR_ID_DETAIL_DEV:vstr_SUBSCR_ID_DETAIL_PREPROM,
    vstr_SUBSCR_ID_CRED_COA_DEV:vstr_SUBSCR_ID_CRED_COA_PREPROM,
    vstr_SUBSCR_ID_MAIN1_DEV:vstr_SUBSCR_ID_MAIN1_PREPROM,
    vstr_SUBSCR_ID_MAIN2_DEV:vstr_SUBSCR_ID_MAIN2_PREPROM,
    vstr_SUBSCR_ID_OPTN_DEV:vstr_SUBSCR_ID_OPTN_PREPROM,
    vstr_SUBSCR_ID_OPTN_H_DEV:vstr_SUBSCR_ID_OPTN_H_PREPROM,
    vstr_SUBSCR_ID_RDM_PREPROM:vstr_SUBSCR_ID_RDM_PREPROM
}



file = 'LOAD2BD.xlsx'
xls = pd.ExcelFile(file, engine='openpyxl')
sheet_names = xls.sheet_names


xls = pd.ExcelFile(file, engine='openpyxl')

print(xls.sheet_names)

for i in sheet_names:
        if i == 'PRJ':
            prj = pd.read_excel(xls, i)
            print(prj)
            prj = prj.replace({'PRJ':{vstrPrefDev:vstrPrefProm}}, regex = True)
            print(prj)
            prj['PRJ'] = 'NOENNAE'
            print(prj)

