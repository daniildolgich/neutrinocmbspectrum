import camb

params = camb.read_ini('camb_interface/camb_params.ini')

print('Om_b h^2 = ', params.ombh2)
print('Om_c h^2 = ', params.omch2)
print('Om_nu h^2 = ', params.omnuh2)

# params.ombh2 = 0.2

results = camb.get_results(params)

spectra = results.get_cmb_power_spectra(params=None, lmax=2200, spectra=['unlensed_scalar'])

unlensed = results.get_cmb_unlensed_scalar_array_dict(lmax=2200, CMB_unit='muK')



print('done')
