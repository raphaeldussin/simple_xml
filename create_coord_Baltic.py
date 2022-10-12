import numpy as np
import xarray as xr

upper_fine = np.arange(0., 100.,5)
deeper_coarse = np.arange(100.,500.+25.,25.)

interfaces = np.concatenate([upper_fine, deeper_coarse], axis=0)

thicknesses = np.concatenate([5.*np.ones(len(upper_fine)),
                              25.*np.ones(len(deeper_coarse)-1)],
                              axis=0)

vertcoord = xr.Dataset()

vertcoord["z_i"] = xr.DataArray(interfaces,
                                dims=("z_i"),
                                attrs={"long_name": "Interface target depth",
                                       "units": "m"})
vertcoord["dz"] = xr.DataArray(thicknesses,
                               dims=("z_l"),
                               attrs={"long_name": "z* coordinate level thickness",
                                       "units": "m"})

vertcoord.to_netcdf("diag_z_baltic.nc", encoding={"z_i": {"_FillValue": 1e+20},
                                                  "dz": {"_FillValue": 1e+20}})
