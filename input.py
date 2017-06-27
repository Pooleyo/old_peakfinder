run_soh = True
make_plots = True
source = "cu_300K_N20_uncompressed_111_10000.atom"
timestep = 10000 # Only used for file locations. 


a_lattice = 3.615	# In Angstroms.
mass = 63.55 	# In g/mol.


negative_k = True
remove_000 = True
gsqr_max = 3
del_kx = 1/10.0
del_ky = 1/10.0
del_kz = 1/10.0


k_steps_compression = 1e3
k_steps = 11
k_steps_accurate = 1e4 + 1


rotated_to_111 = True


xlo = 0.0
xhi = 1.0
ylo = 0.0
yhi = 1.0
zlo = 0.0
zhi = 1.0


piston_velocity = 0.0


gruneisen_uncompressed = 1.98
debye_temperature_uncompressed = 319.059756455
