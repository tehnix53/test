from flask import Flask, render_template
from test_db import data, MLO

app = Flask(__name__)
app.secret_key = "randomstring"


@app.route('/')
def choose_modality():
    return render_template('index.html')


@app.route('/mmg/<sorted_by>')
def mmg_worklist(sorted_by):
    if sorted_by == 'by_index':
        sorted_file = MLO.sort_values(['id']).values
    elif sorted_by == 'by_status':
        sorted_file = MLO.sort_values(['status']).values
    elif sorted_by == 'by_birth':
        sorted_file = MLO.sort_values(['birth_date']).values
    elif sorted_by == 'by_date':
        sorted_file = MLO.sort_values(['study_date']).values
    elif sorted_by == 'by_pectoral':
        sorted_file = MLO.sort_values(['pectorals']).values
    else:
        sorted_file = MLO.sort_values(['id']).values

    return render_template('mmg_db.html', mmg_files=sorted_file)


@app.route('/flg/<sorted_by>')
def flg_worklist(sorted_by):
    if sorted_by == 'by_index':
        sorted_file = data.sort_values(['id']).values
    elif sorted_by == 'by_status':
        sorted_file = data.sort_values(['status']).values
    elif sorted_by == 'by_cross':
        sorted_file = data.sort_values(['cross_shoulder']).values
    elif sorted_by == 'by_cut':
        sorted_file = data.sort_values(['cut_border']).values
    elif sorted_by == 'by_birth':
        sorted_file = data.sort_values(['birth_date']).values
    elif sorted_by == 'by_date':
        sorted_file = data.sort_values(['study_date']).values
    elif sorted_by == 'by_rotation':
        sorted_file = data.sort_values(['rotation']).values
    else:
        sorted_file = data.sort_values(['id']).values

    return render_template('flg_db.html', flg_files=sorted_file)


@app.route('/info')
def info():
    return render_template('language_choice.html')


@app.route('/dev_language_choice')
def dev_lang():
    return render_template('dev_lang_choice.html')


@app.route('/info_en')
def info_en():
    return render_template('info_en.html')


@app.route('/info_ru')
def info_ru():
    return render_template('info_ru.html')


@app.route('/dev_ru')
def dev_ru():
    return render_template('dev_ru.html')


@app.route('/dev_en')
def dev_en():
    return render_template('dev_en.html')


@app.route('/mmg_viewer/<id>/<mode>')
def m_viewer(id, mode):
    if mode == 'image':
        pass
    elif mode == 'pectorals':
        pass
    elif mode == 'nipples':
        pass

    digree = MLO.loc[MLO.id == int(id)]['degree'].values[0]
    status = MLO.loc[MLO.id == int(id)]['status'].values[0]
    nipples = MLO.loc[MLO.id == int(id)]['nipples'].values[0]
    pectorals_status = MLO.loc[MLO.id == int(id)]['pectoral_status'].values[0]
    return render_template('mmg_viewer.html', id=id, mode=mode, digree=digree, status=status,
                           pectorals_status=pectorals_status, nipples=nipples)


@app.route('/flg_viewer/<id>/<mode>')
def viewer(id, mode):
    if mode == 'image':
        pass
    elif mode == 'lungs':
        pass
    elif mode == 'clavicles':
        pass
    elif mode == 'shoulder':
        pass
    elif mode == 'breath':
        pass
    elif mode == 'heart':
        pass

    cut_region = data.loc[data.id == int(id)]['cut_border'].values[0]
    r_koef = data.loc[data.id == int(id)]['r_koef'].values[0]
    cross_region = data.loc[data.id == int(id)]['cross_shoulder_region'].values[0]
    deep = data.loc[data.id == int(id)]['breath'].values[0]
    rotation = data.loc[data.id == int(id)]['rotation'].values[0]
    cti = data.loc[data.id == int(id)]['cti'].values[0]

    return render_template('flg_viewer.html', id=id, mode=mode, r_koef=r_koef,
                           cut_region=cut_region, cross_region=cross_region,
                           deep=deep, rotation=rotation, cti=cti)


#app.run('127.0.0.1', 8000, debug=True)
if __name__ == '__main__':
    app.run()
