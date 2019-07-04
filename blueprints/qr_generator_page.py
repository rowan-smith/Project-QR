from flask import Blueprint, render_template, request

qr_gen_blueprint = Blueprint('qr_generator_page', __name__)


@qr_gen_blueprint.route('/qr', methods=['GET'])
def qr_page():

    data = {
        'url': 'it.jcu.io',
        'size': 60,
        'colour': 'white',
        'image': 'default'
    }

    temp_data = dict(request.values)
    for i in temp_data:

        if str(i).lower() == 'image':
            data['image'] = temp_data[i]

        if str(i).lower() == 'size':
            data['size'] = temp_data[i]

        if str(i).lower() == 'colour' or str(i).lower() == 'color':
            data['colour'] = temp_data[i]

        if str(i).lower() == 'url':
            data['url'] = temp_data[i]
    del temp_data

    return render_template('qr_generator.html', data=data)
