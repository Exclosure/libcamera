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

pycamera = custom_target('python_setup_build',
    input: pycamera_sources,
    command: [py3, setup_py_copy, 'bdist_wheel'],
    output: ['libcamera.cpython-39-x86_64-linux-gnu.so'],
    depends: libcamera,
    build_by_default: true,
)

meson.add_install_script(py3, setup_py_copy, 'install')

