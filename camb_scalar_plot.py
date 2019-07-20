import camb
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

params = camb.read_ini('camb_interface/camb_params.ini')

print('Om_b h^2 = ', params.ombh2)
print('Om_c h^2 = ', params.omch2)
print('Om_nu h^2 = ', params.omnuh2)

# params.ombh2 = 0.2

results = camb.get_results(params)

spectra = results.get_cmb_power_spectra(params=None, lmax=2200, spectra=['unlensed_scalar'])

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

# ax.plot(ee)
# ax.set(xlabel='Multipole Moment (l)', ylabel='CMB_Unit (uK)', title='Cl EE CMB Power Spectrum')
# fig.savefig("Cl_EE.png")
# plt.show()

print('done')
