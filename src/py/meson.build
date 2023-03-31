# SPDX-License-Identifier: CC0-1.0

py3 = find_program('python', required : get_option('pycamera'))


if not py3.found()
    pycamera_enabled = false
    subdir_done()
endif

# Check to make sure version is sufficient
is_py3 = run_command(py3, '--version').stdout().strip().split()[1].split('.')[0].to_int() >= 3

if not is_py3
    pycamera_enabled = false
    subdir_done()
endif

pycamera_enabled = true

subdir('libcamera')
# # python = find_program('python', required : true)
# py_setup_build = run_target('pycamera_setup_build',
#     command : [py3, 'setup.py', 'build'],
#     depends : [libcamera_h],
# )

# # custom_target('libcamera_python_bindings',
# #     command: ['python', 'setup.py', 'build'],
# #     depend_files: [libcamera_h],
# #     output: ['libcamera/_libcamera.so'],
# # )

# run_target('pycamera_install',
#     command : ['python', 'setup.py', 'install'],
#     depends : [py_setup_build],
# )

# meson.add_install_script('python', 'setup.py', 'install')

