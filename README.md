# simple_xml

This repo is used as a starting point for tutorials but feel free to use it as a template
for ocean_only or ice_ocean configurations.

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

