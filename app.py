import numpy as np
import physical_utils as pu
import objects as ob


proton = ob.Object (pu.evToKg(937000000), np.array([0, 0, 0]), pu.spinToEnergy(1.5), np.array([700, 350, 350]))
electron = ob.Object (pu.evToKg(511000), np.array([0, 0, 0]), pu.spinToEnergy(0.5), np.array([350, 350, 350]))
