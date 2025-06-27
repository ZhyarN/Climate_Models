# Description of the Model
This is a 0D EBM model, which is based on multiple types of introductory texts. The model assumes no atmospheric layers and provides an output of the surface temperature of the earth based on different values of emissivity and albedo. 

It follows the following equation:

T= ((1 - α) S₀ / 4 ε σ)^1/4 

T: Surface Temperature of the Earth

α: Albedo

S₀: Solar Constant

ε: Emissivity

σ: Stefan-Boltzmann constant

The Figure 1 illustrates what bare earth's temperature would be given different values of albedo and emissivity

Then, we include cloud cover to see what effect does it have on the surface temperature. We assume that for full cloud cover, a part of the radiation passes through anyways. So, we introduce this to get

T= ((1 - α) S₀ / 4 ε σ (1-(c/2)))^1/4 

c: cloud cover

Figure 2 illustrates that for given albedo and emissivity values (0.3 and 0.95 respectively) how different cloud cover values affect the surface temperature of the earth.
