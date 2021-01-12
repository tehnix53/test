import os
from PIL import Image, ImageOps
from flask import Flask, render_template
from test_db import data, MLO

app = Flask(__name__)
app.secret_key = "randomstring"

from utility import diff_mask, add_colored_plt, add_colored_mask


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
    return render_template('info.html')


@app.route('/mmg_viewer/<id>/<mode>')
def m_viewer(id, mode):
    if mode == 'image':
        pass

    elif mode == 'pectorals':
        for i in os.listdir('static/pectorals/temp/'):
            os.remove(os.path.join('static/pectorals/temp', i))
        image = 'static/mammo/' + str(id) + '.png'
        mask = 'static/pectorals/' + str(id) + '.png'
        apply_mask = Image.fromarray(add_colored_mask(image, mask))
        #apply_mask = ImageOps.equalize(apply_mask)
        apply_mask.save('static/pectorals/temp/' + str(id) + '.png')

    elif mode == 'nipples':
        for i in os.listdir('static/nipples/temp/'):
            os.remove(os.path.join('static/nipples/temp', i))

        image = 'static/mammo/' + str(id) + '.png'
        mask = 'static/pectorals/' + str(id) + '.png'
        apply_mask = Image.fromarray(add_colored_mask(image, mask))
        #apply_mask = ImageOps.equalize(apply_mask)
        apply_mask.save('static/nipples/temp/mask.png')



        image = 'static/nipples/temp/mask.png'
        mask = 'static/nipples/' + str(id) + '.png'
        apply_mask = Image.fromarray(add_colored_mask(image, mask))
        #apply_mask = ImageOps.equalize(apply_mask)
        apply_mask.save('static/nipples/temp/' + str(id) + '.png')




    digree = MLO.loc[MLO.id == int(id)]['degree'].values[0]
    status = MLO.loc[MLO.id == int(id)]['status'].values[0]
    nipples  = MLO.loc[MLO.id == int(id)]['nipples'].values[0]
    pectorals_status = MLO.loc[MLO.id == int(id)]['pectoral_status'].values[0]
    return render_template('mmg_viewer.html', id=id, mode=mode, digree=digree, status=status,
                           pectorals_status=pectorals_status, nipples = nipples)


@app.route('/flg_viewer/<id>/<mode>')
def viewer(id, mode):
    if mode == 'image':
        pass

    elif mode == 'lungs':
        for i in os.listdir('static/lungs/temp/'):
            os.remove(os.path.join('static/lungs/temp', i))
        image = 'static/images/' + str(id) + '.png'
        mask = 'static/lungs/' + str(id) + '.png'
        apply_mask = Image.fromarray(add_colored_mask(image, mask))
        apply_mask = ImageOps.equalize(apply_mask)
        apply_mask.save('static/lungs/temp/' + str(id) + '.png')
        # apply_mask = add_colored_plt(image, mask)
        # apply_mask.save('static/clavicles/temp/' + str(id) + '.jpg', "JPEG", quality=100)

    elif mode == 'clavicles':
        for i in os.listdir('static/clavicles/temp/'):
            os.remove(os.path.join('static/clavicles/temp', i))
        image = 'static/images/' + str(id) + '.png'
        mask = 'static/clavicles/' + str(id) + '.png'

        apply_mask = Image.fromarray(diff_mask(image, mask))
        # apply_mask = add_colored_plt(image, mask)
        apply_mask = ImageOps.equalize(apply_mask)
        apply_mask.save('static/clavicles/temp/' + str(id) + '.png')
        # apply_mask.save('static/clavicles/temp/' + str(id) + '.jpg', "JPEG", quality=100)

    elif mode == 'shoulder':
        for i in os.listdir('static/shoulder/temp/'):
            os.remove(os.path.join('static/shoulder/temp', i))
        image = 'static/images/' + str(id) + '.png'
        mask = 'static/lungs/' + str(id) + '.png'
        apply_mask = Image.fromarray(add_colored_mask(image, mask))
        # apply_mask = ImageOps.invert(apply_mask)
        apply_mask.save('static/shoulder/temp/' + 'mask.png')
        # change another color
        image = 'static/shoulder/temp/' + 'mask.png'
        mask = 'static/shoulder/' + str(id) + '.png'
        apply_mask = Image.fromarray(diff_mask(image, mask))
        apply_mask = ImageOps.equalize(apply_mask, mask=None)
        apply_mask.save('static/shoulder/temp/' + str(id) + '.png')

    elif mode == 'breath':
        for i in os.listdir('static/edge/temp/'):
            os.remove(os.path.join('static/edge/temp', i))
        image = 'static/images/' + str(id) + '.png'
        mask = 'static/lungs/' + str(id) + '.png'
        apply_mask = Image.fromarray(add_colored_mask(image, mask))
        apply_mask.save('static/edge/temp/' + 'mask.png')
        image = 'static/edge/temp/' + 'mask.png'
        mask = 'static/edge/' + str(id) + '.png'
        apply_mask = Image.fromarray(diff_mask(image, mask))
        apply_mask = ImageOps.equalize(apply_mask, mask=None)
        apply_mask.save('static/edge/temp/' + str(id) + '.png')

    cut_region = data.loc[data.id == int(id)]['cut_border'].values[0]
    r_koef = data.loc[data.id == int(id)]['r_koef'].values[0]
    cross_region = data.loc[data.id == int(id)]['cross_shoulder_region'].values[0]
    deep = data.loc[data.id == int(id)]['breath'].values[0]
    rotation = data.loc[data.id == int(id)]['rotation'].values[0]

    return render_template('flg_viewer.html', id=id, mode=mode, r_koef=r_koef,
                           cut_region=cut_region, cross_region=cross_region,
                           deep=deep, rotation=rotation)


#app.run('127.0.0.1', 8000, debug=True)
if __name__ == '__main__':
    app.run()
