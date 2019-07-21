import camb
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def camb_plot_unlensed(params, ombh2, omch2, omnuh2):
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


def camb_plot_lensed(params, ombh2, omch2, omnuh2):
    params.ombh2 = ombh2
    params.omch2 = omch2
    params.omnuh2 = omnuh2
    results = camb.get_results(params)

    unlensed = results.get_cmb_unlensed_scalar_array_dict(lmax=2200, CMB_unit='muK')

    tt_unlensed = unlensed['TxT']

    lensed = results.get_lensed_scalar_cls(lmax=2100, CMB_unit='muK')
    transposed = np.transpose(lensed)

    tt_lensed = transposed[0]
    ee = transposed[1]
    te = transposed[3]

    fig, ax = plt.subplots()
    tt_unlensed = np.delete(tt_unlensed, [0, 1])
    tt_lensed = np.delete(tt_lensed, [0, 1])
    ax.plot(tt_lensed, linewidth=1, color='red')
    ax.plot(tt_unlensed, linewidth=1, color='blue')
    ax.set_xlim([None, 2500])
    ax.set_ylim([None, 7000])
    ax.set(xlabel='Multipole Moment (l)', ylabel='CMB_Unit (uK)', title='Cl TT Lensed CMB Power Spectrum')
    fig.savefig("Cl_TT_lensed.pdf")


params = camb.read_ini('camb_interface/camb_params.ini')
camb_plot_lensed(params, params.ombh2, params.omch2, params.omnuh2)
# camb_plot_unlensed(params, params.ombh2, params.omch2, params.omnuh2)
plt.show()

print('done')
