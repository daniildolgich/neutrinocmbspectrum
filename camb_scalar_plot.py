import camb
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def camb_plot(params, ombh2, omch2, omnuh2):
    params.ombh2 = ombh2
    params.omch2 = omch2
    params.omnuh2 = omnuh2
    results = camb.get_results(params)

    unlensed = results.get_cmb_unlensed_scalar_array_dict(lmax=2200, CMB_unit='muK')

    tt = unlensed['TxT']
    ee = unlensed['ExE']
    te = unlensed['TxE']

    fig, ax = plt.subplots()
    tt = np.delete(tt, [0, 1])
    ax.plot(tt, linewidth=1)
    ax.set_xlim([None, 2500])
    ax.set_ylim([None, 7000])
    ax.set(xlabel='Multipole Moment (l)', ylabel='CMB_Unit (uK)', title='Cl TT CMB Power Spectrum')
    fig.savefig("Cl_TT.pdf")
    plt.show()


params = camb.read_ini('camb_interface/camb_params.ini')
camb_plot(params, params.ombh2, params.omch2, params.omnuh2)
print('done')
