from glob import glob
from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension

from codegen_controls import main as gen_controls
from codegen_formats import main as gen_formats
from pybind11_stubgen import main as gen_stub


# NOTE(meawoppl) These can be vastly simplified to not go through 
# the argparse and assorted tomfoolery that remains
gen_controls(["placeholder",
    '--mode', 'controls', 
    '-o', "libcamera/py_controls_generated.cpp", 
    '../libcamera/control_ids.yaml',
    'libcamera/py_controls_generated.cpp.in',
])

gen_controls(["placeholder",
    '--mode', 'properties', 
    '-o', 'libcamera/py_properties_generated.cpp',
    '../libcamera/property_ids.yaml',
    'libcamera/py_properties_generated.cpp.in'
])

gen_formats(["placeholder",
    '-o', 'libcamera/py_formats_generated.cpp',
    '../libcamera/formats.yaml',
    'libcamera/py_formats_generated.cpp.in',
])

#gen_stub(["pybind11-stubgen", "--no-setup-py", "-o", "libcamera", "libcamera"])


ext_modules = [
    Pybind11Extension(
        "libcamera",
        sorted(glob("libcamera/*.cpp")),  # Sort source files for reproducibility
        include_dirs=['../../include'],
        extra_compile_args=[
            '-fvisibility=hidden',
            '-Wno-shadow',
            '-DPYBIND11_USE_SMART_HOLDER_AS_DEFAULT',
        ],

    ),
]

setup(
    name='libcamera',
    version='0.0.4',
    description='Python wrapper to `libcamera`',
    author='Libcamera Developers',
    author_email=' libcamera-devel@lists.libcamera.org',
    url='https://libcamera.org/',
    packages=['libcamera', 'libcamera.utils'],
    ext_modules=ext_modules
)