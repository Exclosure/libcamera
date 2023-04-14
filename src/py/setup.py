from glob import glob
from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension

# from codegen import main as codegen
# from pybind11_stubgen import main as gen_stub


# NOTE(meawoppl) These can be vastly simplified to not go through 
# the argparse and assorted tomfoolery that remains
# codegen([
#     '--mode', 'controls', 
#     '-o', "libcamera/py_controls_generated.cpp", 
#     '../libcamera/control_ids.yaml',
#     'libcamera/py_controls_generated.cpp.in',
# ])

# codegen([
#     '--mode', 'properties', 
#     '-o', 'libcamera/py_properties_generated.cpp',
#     '../libcamera/property_ids.yaml',
#     'libcamera/py_properties_generated.cpp.in'
# ])

# codegen(["placeholder",
#     '--mode', 'formats',
#     '-o', 'libcamera/py_formats_generated.cpp',
#     '../libcamera/formats.yaml',
#     'libcamera/py_formats_generated.cpp.in',
# ])

#gen_stub(["pybind11-stubgen", "--no-setup-py", "-o", "libcamera", "libcamera"])


import os
this_dir = os.path.dirname(os.path.abspath(__file__))
print("Running from ", this_dir)
os.chdir(this_dir)

cpp_sources = list(sorted(glob("libcamera/*.cpp"))) 

ext_modules = [
    Pybind11Extension(
        "libcamera._libcamera",
        cpp_sources,
        libraries=['camera'],
        include_dirs=['../../include', "../../../include"],
        extra_compile_args=[
            '-fvisibility=hidden',
            '-Wno-shadow',
            '-DLIBCAMERA_BASE_PRIVATE',
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
