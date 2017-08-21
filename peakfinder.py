# This is a new version of peakfinder (started on 11/10/16) that will restructure the old version.
# The old version was becoming difficult to use due to lack of experience coding.
# The idea with this version is to restructure the code with functions.

import module as mod
from input import *

############################################################################################

t0, tpy0 = mod.startwatch()


gsqr_est, pos_est = mod.make_bcc(gsqr_max = gsqr_max, negative_k = negative_k, remove_000 = remove_000)


md_temperature_2d = 300.0
md_temperature_3d = 300.0

#rot_pos_est = mod.enforce_rotation_111(pos_est = pos_est)


#source_cut, atom_count = mod.cut_atoms(source = source, xlo = xlo, xhi = xhi, ylo = ylo, yhi = yhi, zlo = zlo, zhi = zhi)


#md_temperature_2d, md_temperature_3d = mod.get_md_temperature(source = source, mass = mass, piston_velocity = piston_velocity)


#pos_est_compressed, gsqr_est_compressed, compression_factor = mod.compensate_for_compression(source = source, rotated_to_111 = rotated_to_111, initial_hkl_pos_est = pos_est, run_soh = run_soh, k_steps = k_steps_compression, pos_est = rot_pos_est, a_lattice = a_lattice, mass = mass, show_plot = False, timestep = timestep)



accurate_breadths = mod.get_peak_intensities(source = source, pos_est = pos_est, initial_hkl_pos_est = pos_est, compression_factor = [1.0, 1.0, 1.0], a_lattice = a_lattice, mass = mass, del_kx = del_kx, del_ky = del_ky, del_kz = del_kz, k_steps = k_steps, k_steps_accurate = k_steps_accurate, run_soh = run_soh, timestep = timestep, make_plots = make_plots)



pos_integrated, gsqr_integrated, ln_complex_intensity_integrated, ln_norm_complex_intensity_integrated, ln_simple_intensity_integrated, ln_norm_simple_intensity_integrated = mod.get_ln_intensity(pos_est = pos_est, initial_hkl_pos_est = pos_est, source = source, miller_pos_est = pos_est, show_plot = False, timestep = timestep, a_lattice = a_lattice, del_kx = del_kx, del_ky = del_ky, del_kz = del_kz, k_steps = k_steps, compression_factor = [1.0,1.0,1.0], make_plots = make_plots)



slope_ln_complex_intensity_integrated_vs_gsqr, constant_ln_complex_intensity_vs_gsqr = mod.get_slope_ln_intensity_vs_gsqr(gsqr = gsqr_integrated, ln_intensity = ln_complex_intensity_integrated)

slope_ln_simple_intensity_integrated_vs_gsqr, constant_ln_simple_intensity_vs_gsqr = mod.get_slope_ln_intensity_vs_gsqr(gsqr = gsqr_integrated, ln_intensity = ln_simple_intensity_integrated)

"""
slope_ln_sum_intensity_vs_gsqr, constant_ln_sum_intensity_vs_gsqr = mod.get_slope_ln_intensity_vs_gsqr(gsqr = gsqr_integrated, ln_intensity = ln_sum_intensity)

slope_ln_peak_intensity_vs_gsqr, constant_ln_peak_intensity_vs_gsqr = mod.get_slope_ln_intensity_vs_gsqr(gsqr = gsqr_integrated, ln_intensity = ln_peak_intensity)
"""


debye_temperature = mod.calc_debye_temperature(slope_ln_intensity_vs_gsqr = slope_ln_complex_intensity_integrated_vs_gsqr, mass = mass, md_temperature = md_temperature_2d)



temperature_est_simple_integration, central_temperature_simple_integration = mod.calc_temperature_xrd(slope_ln_intensity_vs_gsqr = slope_ln_simple_intensity_integrated_vs_gsqr, constant_ln_intensity_vs_gsqr = constant_ln_simple_intensity_vs_gsqr, gruneisen_uncompressed = gruneisen_uncompressed, a_lattice = a_lattice, compression_factor = [1.0,1.0,1.0], mass = mass, pos = pos_integrated, gsqr = gsqr_integrated, uncompressed_pos_est = pos_est, uncompressed_gsqr_est = gsqr_est, plot_name = "ln_simpleI_vs_Gsqr.png", show_plot = False, ln_intensity = ln_simple_intensity_integrated, md_temperature_3d = md_temperature_3d, md_temperature_2d = md_temperature_2d, debye_temperature_uncompressed = debye_temperature_uncompressed) 

temperature_est_complex_integration, central_temperature_complex_integration = mod.calc_temperature_xrd(slope_ln_intensity_vs_gsqr = slope_ln_complex_intensity_integrated_vs_gsqr, constant_ln_intensity_vs_gsqr = constant_ln_complex_intensity_vs_gsqr, gruneisen_uncompressed = gruneisen_uncompressed, a_lattice = a_lattice, compression_factor = [1.0,1.0,1.0], mass = mass, pos = pos_integrated, gsqr = gsqr_integrated, uncompressed_pos_est = pos_est, uncompressed_gsqr_est = gsqr_est, plot_name = "ln_complexI_vs_Gsqr.png", show_plot = False, ln_intensity = ln_complex_intensity_integrated, md_temperature_3d = md_temperature_3d, md_temperature_2d = md_temperature_2d, debye_temperature_uncompressed = debye_temperature_uncompressed) 

"""
temperature_est_sum, central_temperature_sum = mod.calc_temperature_xrd(slope_ln_intensity_vs_gsqr = slope_ln_sum_intensity_vs_gsqr, constant_ln_intensity_vs_gsqr = constant_ln_sum_intensity_vs_gsqr, gruneisen_uncompressed = gruneisen_uncompressed, a_lattice = a_lattice, compression_factor = compression_factor, mass = mass, pos = pos_integrated, gsqr = gsqr_integrated, uncompressed_pos_est = pos_est, uncompressed_gsqr_est = gsqr_est, plot_name = "ln_sumI_vs_Gsqr.png", show_plot = False, ln_intensity = ln_sum_intensity, md_temperature_3d = md_temperature_3d, md_temperature_2d = md_temperature_2d, debye_temperature_uncompressed = debye_temperature_uncompressed) 

temperature_est_peak, central_temperature_peak = mod.calc_temperature_xrd(slope_ln_intensity_vs_gsqr = slope_ln_peak_intensity_vs_gsqr, constant_ln_intensity_vs_gsqr = constant_ln_peak_intensity_vs_gsqr, gruneisen_uncompressed = gruneisen_uncompressed, a_lattice = a_lattice, compression_factor = compression_factor, mass = mass, pos = pos_integrated, gsqr = gsqr_integrated, uncompressed_pos_est = pos_est, uncompressed_gsqr_est = gsqr_est, plot_name = "ln_peakI_vs_Gsqr.png", show_plot = False, ln_intensity = ln_peak_intensity, md_temperature_3d = md_temperature_3d, md_temperature_2d = md_temperature_2d, debye_temperature_uncompressed = debye_temperature_uncompressed) 
"""





mod.profile_peaks(source = source, timestep = timestep, initial_hkl_pos_est = pos_est, make_plots = make_plots)



mod.checkout(xrd_temperatures = [central_temperature_simple_integration, central_temperature_complex_integration], xrd_temperature_labels = ["Temperature by simple integration\t", "Temperature by complex integration"], md_temperatures = [md_temperature_2d, md_temperature_3d], md_temperature_labels = ["2D","3D"])



mod.stopwatch(t0, tpy0)
