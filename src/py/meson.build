# SPDX-License-Identifier: CC0-1.0

py3_dep = dependency('python3', required : get_option('pycamera'))

if not py3_dep.found()
    pycamera_enabled = false
    subdir_done()
endif

pycamera_enabled = true

# python = find_program('python', required : true)
py_setup_build = run_target('pycamera_setup_build',
    command : ['python', 'setup.py', 'build'],
    depends : [libcamera_h],
)

custom_target('libcamera_python_bindings',
    command: ['python', 'setup.py', 'build'],
    depend_files: [libcamera_h],
    output: ['libcamera/_libcamera.so'],
)

meson.add_install_script('python', 'setup.py', 'install')

