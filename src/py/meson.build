# SPDX-License-Identifier: CC0-1.0

py3 = find_program('python', required : get_option('pycamera'))

if not py3.found()
    pycamera_enabled = false
    warning('Python 3 not found, disabling pycamera')
    subdir_done()
endif

# Check to make sure version is sufficient
version_string = run_command(py3, '--version', check: true).stdout().strip()
message('Building against Python version: ' + version_string)
is_py3 = version_string.split()[1].split('.')[0].to_int() >= 3

if not is_py3
    pycamera_enabled = false
    warning('Python 3 not found, disabling pycamera found: ' + version_string)
    subdir_done()
endif

pycamera_enabled = true

subdir('libcamera')

setup_py_copy = configure_file(input: 'setup.py', output: 'setup.py', copy: true)


#setup_py = files('setup.py')


pycamera = custom_target('python_setup_build',
    input: pycamera_sources,
    command: [py3, setup_py_copy, 'bdist_wheel'],
    output: ['libcamera.cpython-39-x86_64-linux-gnu.so'],
    depends: libcamera,
    build_by_default: true,
)

# message('cbd:', meson.current_build_dir())
# install_data(
#     setup_py,
#     sources: pycamera_sources,
#     install_dir: meson.current_build_dir())

# install_data(sources: pycamera_sources, install_dir: meson.current_build_dir())


# run_python_build = custom_target('run_python_build',
#     input: ['setup.py'],
#     output: [join_paths('libcamera', '_libcamera.so')],
#     command: [py3, 'setup.py', 'build'],
#     build_by_default: true,
#     depend_files: [pycamera_sources],
# )



# pycamera_deps = declare_dependency(
#     sources: pycamera_sources
# )

# pycamera = run_target('pycamera',
#     command : [py3, 'setup.py', 'build'],
#     depends : [libcamera_h, pycamera_deps],
# )

# subdir('libcamera')
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

