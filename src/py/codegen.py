#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-or-later
#
# Generate Python bindings controls from YAML

import argparse
import string
import sys
import yaml


def generate(formats):
    fmts = []

    for format in formats:
        name, format = format.popitem()
        fmts.append(f'\t\t.def_readonly_static("{name}", &libcamera::formats::{name})')

    return {'formats': '\n'.join(fmts)}


def fill_template(template, data):
    with open(template, encoding='utf-8') as f:
        template = f.read()

    template = string.Template(template)
    return template.substitute(data)



def find_common_prefix(strings):
    prefix = strings[0]

    for string in strings[1:]:
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:len(prefix) - 1]
        if not prefix:
            break

    return prefix


def generate_py(controls, mode):
    out = ''

    for ctrl in controls:
        name, ctrl = ctrl.popitem()

        if ctrl.get('draft'):
            ns = 'libcamera::{}::draft::'.format(mode)
            container = 'draft'
        else:
            ns = 'libcamera::{}::'.format(mode)
            container = 'controls'

        out += f'\t{container}.def_readonly_static("{name}", static_cast<const libcamera::ControlId *>(&{ns}{name}));\n\n'

        enum = ctrl.get('enum')
        if not enum:
            continue

        cpp_enum = name + 'Enum'

        out += '\tpy::enum_<{}{}>({}, \"{}\")\n'.format(ns, cpp_enum, container, cpp_enum)

        if mode == 'controls':
            # Adjustments for controls
            if name == 'LensShadingMapMode':
                prefix = 'LensShadingMapMode'
            elif name == 'SceneFlicker':
                # If we strip the prefix, we would get '50Hz', which is illegal name
                prefix = ''
            else:
                prefix = find_common_prefix([e['name'] for e in enum])
        else:
            # Adjustments for properties
            prefix = find_common_prefix([e['name'] for e in enum])

        for entry in enum:
            cpp_enum = entry['name']
            py_enum = entry['name'][len(prefix):]

            out += '\t\t.value(\"{}\", {}{})\n'.format(py_enum, ns, cpp_enum)

        out += '\t;\n\n'

    return {'controls': out}


def main(argv: list[str] = sys.argv[1:]):
    # Parse command line arguments
    parser = argparse.ArgumentParser(prog="codegen_controls.py")
    parser.add_argument('-o', dest='output', metavar='file', type=str,
                        help='Output file name. Defaults to standard output if not specified.')
    parser.add_argument('input', type=str,
                        help='Input file name.')
    parser.add_argument('template', type=str,
                        help='Template file name.')
    parser.add_argument('--mode', type=str, required=True,
                        choices=['controls', 'properties', 'formats'],
                        help='Mode is either "controls" or "properties"')
    args = parser.parse_args(argv)

    with open(args.input, 'rb') as f:
        input_yml = yaml.safe_load(f)

    if args.mode == 'formats':
        data = generate(input_yml['formats'])
    else:
        data = generate_py(input_yml['controls'], args.mode)

    formatted = fill_template(args.template, data)

    if args.output:
        output = open(args.output, 'wb')
        output.write(formatted.encode('utf-8'))
        output.close()
    else:
        sys.stdout.write(formatted)

    return 0


if __name__ == '__main__':
    main()
