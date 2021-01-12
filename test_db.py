import pandas as pd

flg_files = \
    [{'id': 1, 'study_date': '21.01.2020', 'birth_date': '11.01.1989', 'cut_border': 'pass', 'rotation': 'pass',
      'r_koef': '12,36%', 'cross_shoulder': 'pass', 'cross_shoulder_region': "not", "breath": 'norm'},
     {'id': 2, 'study_date': '22.01.2020', 'birth_date': '11.02.1989', 'cut_border': 'pass', 'rotation': 'pass',
      'r_koef': '16,85%', 'cross_shoulder': 'fail', 'cross_shoulder_region': "L, R", 'breath': 'norm'},

     {'id': 3, 'study_date': '23.01.2020', 'birth_date': '11.03.1989', 'cut_border': 'pass', 'rotation': 'fail',
      'r_koef': '38,21%', 'cross_shoulder': 'pass', 'cross_shoulder_region': 'not', 'breath': 'norm'},

     {'id': 4, 'study_date': '24.01.2020', 'birth_date': '11.04.1989', 'cut_border': 'pass', 'rotation': 'fail',
      'r_koef': '21,71%', 'cross_shoulder': 'fail', 'cross_shoulder_region': 'L, R', 'breath': 'norm'}

     ]

MLO_files = [{'id': 1, 'study_date': '21.01.2020', 'birth_date': '11.01.1989', 'modality': 'MLO', 'shoulder': 'pass',
              's_degree': '16,18`', 'status': 'good', 'nipples': 'pass', 'pectoral_status': 'good'},
             {'id': 2, 'study_date': '22.01.2020', 'birth_date': '11.02.1989', 'modality': 'MLO', 'shoulder': 'pass',
              's_degree': '17,61`', 'status': 'bad', 'nipples': 'hide', 'pectoral_status': 'good'},
             {'id': 3, 'study_date': '23.01.2020', 'birth_date': '11.03.1989', 'modality': 'MLO', 'shoulder': 'pass',
              's_degree': '8,77`', 'status': 'bad', 'nipples': 'pass', 'pectoral_status': 'bad'},
             {'id': 4, 'study_date': '24.01.2020', 'birth_date': '11.04.1989', 'modality': 'MLO', 'shoulder': 'pass',
              's_degree': '19,5`', 'status': 'bad', 'nipples': 'hide', 'pectoral_status': 'good'}, ]

MLO = pd.DataFrame()
MLO['id'] = [i['id'] for i in MLO_files]
MLO['study_date'] = [i['study_date'] for i in MLO_files]
MLO['birth_date'] = [i['birth_date'] for i in MLO_files]
MLO['modality'] = [i['modality'] for i in MLO_files]
MLO['pectoral'] = [i['pectoral_status'] for i in MLO_files]
MLO['degree'] = [i['s_degree'] for i in MLO_files]
MLO['status'] = [i['status'] for i in MLO_files]
MLO['nipples'] = [i['nipples'] for i in MLO_files]
MLO['pectoral_status'] = [i['pectoral_status'] for i in MLO_files]

for i in flg_files:
    if i['cut_border'] == 'fail' or i['rotation'] == 'fail' or i['cross_shoulder'] == 'fail':
        i['status'] = 'bad'
    else:
        i['status'] = 'good'

data = pd.DataFrame()

data['id'] = [i['id'] for i in flg_files]
data['study_date'] = [i['study_date'] for i in flg_files]
data['birth_date'] = [i['birth_date'] for i in flg_files]
data['cut_border'] = [i['cut_border'] for i in flg_files]
data['cross_shoulder'] = [i['cross_shoulder'] for i in flg_files]
data['rotation'] = [i['rotation'] for i in flg_files]
data['breath'] = [i['breath'] for i in flg_files]
data['status'] = [i['status'] for i in flg_files]
data['r_koef'] = [i['r_koef'] for i in flg_files]
data['cross_shoulder_region'] = [i['cross_shoulder_region'] for i in flg_files]

by_status = data.sort_values(['status']).values
by_id = data.sort_values(['id']).values

