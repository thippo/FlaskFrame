from flask import Blueprint, render_template, url_for
from .bitcoin_form import *
from ..packages.bitcoin_script import utils, py3private2address

bitcoin_bitcoin_blueprint = Blueprint('bitcoin', __name__, url_prefix='/bitcoin', template_folder='templates', static_folder='static')

@bitcoin_bitcoin_blueprint.route('/index', methods=('GET', 'POST'))
def bitcoin_index():
    form = SearchForm()
    transfer_dict = {}
    if form.validate_on_submit():
        data = form.q.data.strip()
        if not utils.whether_privatekey(data):
            transfer_dict['type'] = 2
        else:
            if len(data) == 51 and '5' in data[0]:
                transfer_dict['type'] = 1
                transfer_dict['pkuc'] = data
                transfer_dict['pkc'] = utils.WIF_to_compressed(data)
                p2a = py3private2address.Private2Address(data)
                transfer_dict['bauc'] = p2a.bitcoinaddress_uncompressed
                transfer_dict['bac'] = p2a.bitcoinaddress_compressed
            elif len(data) == 52 and ('K' is data[0] or 'L' is data[0]):
                transfer_dict['type'] = 1
                transfer_dict['pkc'] = data
                transfer_dict['pkuc'] = utils.compressed_to_WIF(data)
                p2a = py3private2address.Private2Address(data)
                transfer_dict['bauc'] = p2a.bitcoinaddress_uncompressed
                transfer_dict['bac'] = p2a.bitcoinaddress_compressed
            elif (26 <= len(data) and len(data) <=34) and ('1' is data[0] or '3' is data[0]):
                if utils.whether_bitcoinaddress(data):
                    return render_template('bitcoinaddress', data=data, form=form)
                else:
                    transfer_dict['type'] = 2
            else:
                transfer_dict['type'] = 2
    else:
        transfer_dict['type'] = 0
    return render_template('bitcoin', transfer_dict=transfer_dict, form=form)
