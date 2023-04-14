# SPDX-License-Identifier: CC0-1.0

pycamera_sources = files([
    'py_camera_manager.h',
    'py_camera_manager.cpp',
    'py_enums.cpp',
    'py_geometry.cpp',
    'py_helpers.h',
    'py_helpers.cpp',
    'py_main.h',
    'py_main.cpp',
])

foreach f : pycamera_sources
    configure_file(
        input: f,
        output: '@PLAINNAME@',
        copy: true,
    )
endforeach

# Generate controls
gen_py_controls_input_files = files([
    '../../libcamera/control_ids.yaml',
    '../templates/py_controls_generated.cpp.in',
])

gen_py_controls = files('../codegen.py')

custom_target('py_gen_controls',
              input : gen_py_controls_input_files,
              output : ['py_controls_generated.cpp'],
              command : [gen_py_controls, '--mode', 'controls', '-o', '@OUTPUT@', '@INPUT@'],
              build_always: true
)

# Generate properties
gen_py_property_enums_input_files = files([
    '../../libcamera/property_ids.yaml',
    '../templates/py_properties_generated.cpp.in',
])

custom_target('py_gen_properties',
              input : gen_py_property_enums_input_files,
              output : ['py_properties_generated.cpp'],
              command : [gen_py_controls, '--mode', 'properties', '-o', '@OUTPUT@', '@INPUT@'],
              build_always: true
)

# Generate formats
gen_py_formats_input_files = files([
    '../../libcamera/formats.yaml',
    '../templates/py_formats_generated.cpp.in',
])

custom_target('py_gen_formats',
              input : gen_py_formats_input_files,
              output : ['py_formats_generated.cpp'],
              command : [gen_py_controls, '--mode', 'formats', '-o', '@OUTPUT@', '@INPUT@'],
              build_always: true
)

run_command('cp', files('__init__.py'), 
            meson.current_build_dir() / '__init__.py',
            check: true)

run_command('cp', '-r', meson.current_source_dir() / 'utils',
            meson.current_build_dir() / 'utils',
            check: true)

subdir_done()

# \todo Generate stubs when building. See https://peps.python.org/pep-0484/#stub-files
# Note: Depends on pybind11-stubgen. To generate pylibcamera stubs:
# $ PYTHONPATH=build/src/py pybind11-stubgen --no-setup-py -o build/src/py libcamera
