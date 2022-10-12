# simple_xml

This repo is used as a starting point for tutorials but feel free to use it as a template
for ocean_only or ice_ocean configurations.

## Installation

quick and dirty way:

```
git clone https://github.com/raphaeldussin/simple_xml.git
```

If you're confortable with git, you can also create your own repo by clicking *use as template*
and populate it with your own xmls.

## Compile and run the examples:

### Phillips 2 layers

```
module load fre/bronx-19

fremake -x ocean_only_experiments.xml -p ncrc4.intel18 -t prod MOM6_compile
frerun -t prod -p ncrc4.intel18 -x ocean_only_experiments.xml Phillips_2layers_example
```

### Baltic

```
module load fre/bronx-19

fremake -x ice_ocean_experiments.xml -p ncrc4.intel18 -t prod MOM6_SIS2_compile
frerun -x ice_ocean_experiments.xml -t prod -p ncrc4.intel18 Baltic_025_example
```

## Exercices:

1. create a new Phillips experiment that **inherit** from the existing example,
copy the **MOM_override** into the new **<input>** of the xml and make it a f-plane
experiment (i.e. BETA = 0.)

2. edit the Baltic example and replace the current diag_table by your own, in which you
will save daily output for SST (tos), SSS (sos)

3. the Baltic sea has a maximum depth of 500 meters, finish the code snippet to build a custom
**diagnostic** vertical coordinate with 5 meters resolution from the surface to 100 meters and 
25 meters below 100 meters.

```python
mport numpy as np
import xarray as xr


interfaces = 

thicknesses = 

# define netcdf variables and write to file
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

```

Add this new coordinate to the **DIAG_COORDS** and add thetao and so to the diag_table.

advice: you can use my python install

```
alias ipython=/lustre/f2/dev/Raphael.Dussin/miniconda3/envs/repro/bin/ipython
```

if you're having issues creating the file (or we're running out of time), use the one I already created:

```
/lustre/f2/dev/Raphael.Dussin/input/MOM6tutorial/Baltic/diag_z_baltic.nc
```
