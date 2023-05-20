from glob import glob
from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension

# from codegen import main as codegen
from pybind11_stubgen import main as gen_stub


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
        library_dirs=['../libcamera'],
        extra_compile_args=[
            '-fvisibility=hidden',
            '-Wno-shadow',
            '-DLIBCAMERA_BASE_PRIVATE',
            '-std=c++17',
        ],
    ),
]

from setuptools import setup, Extension, find_packages, Command

# Custom command to generate stubs using pybind11-stubgen
class GenerateStubs(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        gen_stub(["libcamera", "-o", "libcamera"])


setup(
    name='libcamera',
    version='0.0.5',
    description='Python wrapper to `libcamera`',
    author='Libcamera Developers',
    author_email=' libcamera-devel@lists.libcamera.org',
    url='https://libcamera.org/',
    packages=['libcamera', 'libcamera.utils'],
    ext_modules=ext_modules,
    cmdclass={"generate_stubs": GenerateStubs},
)
