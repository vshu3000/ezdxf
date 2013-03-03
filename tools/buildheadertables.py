#!/usr/bin/env python
#coding:utf-8
# Author:  mozman -- <mozman@gmx.at>
# Purpose: build header var tables
# Created: 12.03.2011
# Copyright (C) 2011, Manfred Moitzi
# License: MIT License
import os
import ezdxf
from ezdxf.dxffactory import factories

TABLEPRELUDE = """# auto-generated by buildheadertables.py - do not edit
# Copyright (C) 2011, Manfred Moitzi
# License: MIT License
from __future__ import unicode_literals
__author__ = "mozman <mozman@gmx.at>"

from functools import partial
from ..hdrvars import SingleValue, Point2D, Point3D

VARMAP = {
"""
TABLEEPILOGUE = "}\n"


def write_table(filename, headersection):
    def write_var(key, value):
        if value.ispoint:
            if len(value.getpoint()) == 2:
                factory = "Point2D"
            else:
                factory = "Point3D"
        else:
            factory = "partial(SingleValue, code=%d)" % value.code
        fp.write("    '%s': %s,\n" % (key, factory))

    with open(filename, 'wt') as fp:
        fp.write(TABLEPRELUDE)
        keys = sorted(headersection.hdrvars.keys())
        for key in keys:
            value = headersection.hdrvars[key]
            write_var(key, value)
        fp.write(TABLEEPILOGUE)


def export_header_table(dwg):
    print("writing HEADER table for DXF Version {0.dxfversion}".format(dwg))
    filename = os.path.join('..', 'ezdxf', dwg.dxfversion.lower(), 'headervars.py')
    write_table(filename, dwg.header)


def main():
    for version in factories.keys():
        dwg = ezdxf.new(version)
        export_header_table(dwg)

if __name__ == '__main__':
    main()
