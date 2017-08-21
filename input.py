run_soh = True
make_plots = True


source = "nb_uncompressed_300K.atom"
timestep = 10000 # Only used for file locations. 


a_lattice = 3.3004	# In Angstroms.
mass = 92.90638 	# In g/mol.


negative_k = True
remove_000 = True
gsqr_max = 14
del_kx = 1/60.0
del_ky = 1/60.0
del_kz = 1/60.0


k_steps_compression = 1e2 + 1
k_steps_accurate = 1e2 + 1
k_steps = 3


rotated_to_111 = False


xlo = 0.0
xhi = 1.0
ylo = 0.0
yhi = 1.0
zlo = 0.0
zhi = 1.0


piston_velocity = 0.0


gruneisen_uncompressed = 1.74
debye_temperature_uncompressed = 283
