# This is a new version of peakfinder (started on 11/10/16) that will restructure the old version.
# The old version was becoming difficult to use due to lack of experience coding.
# The idea with this version is to restructure the code with functions.

import module as mod

run_soh = True
make_plots = True
source = "shock_9000.atom"
a_lattice = 3.615	# In Angstroms.
mass = 63.55 	# In g/mol.
timestep = 9000 # Only used for file locations. 

del_kx = 1/15.0
del_ky = 1/12.0
del_kz = 1/20.0
k_steps = 21
k_steps_accurate = 1e3 + 1



gsqr_est, pos_est = mod.make_fcc(range_num = 3, negative_k = True, remove_000 = True)


rot_pos_est = mod.enforce_rotation_111(pos_est = pos_est)


source_cut, atom_count = mod.cut_atoms(source = source, xlo = 0.0, xhi = 1.0, ylo = 0.0, yhi = 1.0, zlo = 0.3, zhi = 0.44)


md_temperature_2d, md_temperature_3d = mod.get_md_temperature(source = source_cut, mass = mass, piston_velocity = 5.01)


pos_est_compressed, gsqr_est_compressed, compression_factor = mod.compensate_for_compression(source = source_cut, rotated_to_111 = True, initial_hkl_pos_est = pos_est, run_soh = run_soh, k_steps = 10001, pos_est = rot_pos_est, a_lattice = a_lattice, mass = mass, show_plot = False, timestep = timestep)


#mod.find_actual_peak_centres(pos_est = pos_est_compressed, initial_pos_est = pos_est, del_kx = del_kx, del_ky = del_ky, del_kz = del_kz, k_steps_accurate = k_steps_accurate, compression_factor = compression_factor, rotated_to_111 = True, run_soh = run_soh, mass = mass, a_lattice = a_lattice, timestep = timestep, make_plots = make_plots, source = source_cut)


mod.get_peak_intensities(source = source_cut, pos_est = pos_est_compressed, initial_hkl_pos_est = pos_est, compression_factor = compression_factor, a_lattice = a_lattice, mass = mass, del_kx = del_kx, del_ky = del_ky, del_kz = del_kz, k_steps = k_steps, k_steps_accurate = k_steps_accurate, run_soh = run_soh, timestep = timestep)



pos_integrated, gsqr_integrated, ln_intensity_integrated, ln_norm_intensity_integrated = mod.get_ln_intensity(pos_est = pos_est_compressed, initial_hkl_pos_est = pos_est, source = source_cut, miller_pos_est = pos_est, show_plot = False, timestep = timestep, a_lattice = a_lattice, del_kx = del_kx, del_ky = del_ky, del_kz = del_kz, k_steps = k_steps, compression_factor = compression_factor, make_plots = make_plots)



slope_ln_intensity_integrated_vs_gsqr, constant_ln_intensity_vs_gsqr = mod.get_slope_ln_intensity_vs_gsqr(gsqr = gsqr_integrated, ln_intensity = ln_intensity_integrated)



debye_temperature = mod.calc_debye_temperature(slope_ln_intensity_vs_gsqr = slope_ln_intensity_integrated_vs_gsqr, mass = mass, md_temperature = md_temperature_2d)



temperature_est = mod.calc_temperature_xrd(slope_ln_intensity_vs_gsqr = slope_ln_intensity_integrated_vs_gsqr, constant_ln_intensity_vs_gsqr = constant_ln_intensity_vs_gsqr, gruneisen_uncompressed = 1.98, a_lattice = a_lattice, compression_factor = compression_factor, mass = mass, pos = pos_integrated, gsqr = gsqr_integrated, uncompressed_pos_est = pos_est, uncompressed_gsqr_est = gsqr_est, plot_name = "ln_I_vs_Gsqr.png", show_plot = False, ln_intensity = ln_intensity_integrated, md_temperature_3d = md_temperature_3d, md_temperature_2d = md_temperature_2d, debye_temperature_uncompressed = 319.059756455) 
