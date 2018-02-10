# Purpose: constant values
# Created: 10.03.2011
# Copyright (C) 2011, Manfred Moitzi
# License: MIT License
from __future__ import unicode_literals
__author__ = "mozman <me@mozman.at>"

acad_release = {
    'AC1009': 'R12',
    'AC1012': 'R13',
    'AC1014': 'R14',
    'AC1015': 'R2000',
    'AC1018': 'R2004',
    'AC1021': 'R2007',
    'AC1024': 'R2010',
    'AC1027': 'R2013',
    'AC1032': 'R2018',
}

versions_supported_by_new = ['AC1009', 'AC1015', 'AC1018', 'AC1021', 'AC1024', 'AC1027', 'AC1032']
LATEST_DXF_VERSION = versions_supported_by_new[-1]

acad_release_to_dxf_version = {
    acad: dxf for dxf, acad in acad_release.items()
}


class DXFError(Exception):  # root exception
    pass


class DXFStructureError(DXFError):
    pass


class DXFAppDataError(DXFStructureError):
    pass


class DXFXDataError(DXFStructureError):
    pass


class DXFVersionError(DXFError):
    pass


class DXFInternalEzdxfError(DXFError):
    pass


class DXFValueError(DXFError, ValueError):
    pass


class DXFKeyError(DXFError, KeyError):
    pass


class DXFAttributeError(DXFError, AttributeError):
    pass


class DXFIndexError(DXFError, IndexError):
    pass


class DXFTypeError(DXFError, TypeError):
    pass


class DXFTableEntryError(DXFValueError):
    pass


class DXFEncodingError(DXFError):
    pass


class DXFDecodingError(DXFError):
    pass


class DXFInvalidLayerName(DXFValueError):
    pass


APP_DATA_MARKER = 102
SUBCLASS_MARKER = 100
XDATA_MARKER = 1001
COMMENT_MARKER = 999
STRUCTURE_MARKER = 0
HEADER_VAR_MARKER = 9

# Special tag codes for internal purpose
# -1 to -5 id reserved by AutoCAD for internal use, but this tags will never be saved to file.
# Same approach here, the following tags have to be converted/transformed into normal tags before
# saved to file.
COMPRESSED_TAGS = -10


# Entity: Polyline, Polymesh
# 70 flags
POLYLINE_CLOSED = 1
POLYLINE_MESH_CLOSED_M_DIRECTION = POLYLINE_CLOSED
POLYLINE_CURVE_FIT_VERTICES_ADDED = 2
POLYLINE_SPLINE_FIT_VERTICES_ADDED = 4
POLYLINE_3D_POLYLINE = 8
POLYLINE_3D_POLYMESH = 16
POLYLINE_MESH_CLOSED_N_DIRECTION = 32
POLYLINE_POLYFACE = 64
POLYLINE_GENERATE_LINETYPE_PATTERN = 128

# Entity: Polymesh
# 75 surface smooth type
POLYMESH_NO_SMOOTH = 0
POLYMESH_QUADRIC_BSPLINE = 5
POLYMESH_CUBIC_BSPLINE = 6
POLYMESH_BEZIER_SURFACE = 8

# Entity: Vertex
# 70 flags
VERTEXNAMES = ('vtx0', 'vtx1', 'vtx2', 'vtx3')
VTX_EXTRA_VERTEX_CREATED = 1  # Extra vertex created by curve-fitting
VTX_CURVE_FIT_TANGENT = 2  # Curve-fit tangent defined for this vertex.
# A curve-fit tangent direction of 0 may be omitted from the DXF output, but is
# significant if this bit is set.
# 4 = unused, never set in dxf files
VTX_SPLINE_VERTEX_CREATED = 8  # Spline vertex created by spline-fitting
VTX_SPLINE_FRAME_CONTROL_POINT = 16
VTX_3D_POLYLINE_VERTEX = 32
VTX_3D_POLYGON_MESH_VERTEX = 64
VTX_3D_POLYFACE_MESH_VERTEX = 128

VERTEX_FLAGS = {
    'AcDb2dPolyline': 0,
    'AcDb3dPolyline': VTX_3D_POLYLINE_VERTEX,
    'AcDbPolygonMesh': VTX_3D_POLYGON_MESH_VERTEX,
    'AcDbPolyFaceMesh': VTX_3D_POLYGON_MESH_VERTEX | VTX_3D_POLYFACE_MESH_VERTEX,
}
POLYLINE_FLAGS = {
    'AcDb2dPolyline': 0,
    'AcDb3dPolyline': POLYLINE_3D_POLYLINE,
    'AcDbPolygonMesh': POLYLINE_3D_POLYMESH,
    'AcDbPolyFaceMesh': POLYLINE_POLYFACE,
}

# block-type flags (bit coded values, may be combined):
# Entity: BLOCK
# 70 flags

# This is an anonymous block generated by hatching, associative dimensioning, other internal operations, or an
# application
BLK_ANONYMOUS = 1

# This block has non-constant attribute definitions (this bit is not set if the block has any attribute definitions that
# are constant, or has no attribute definitions at all)
BLK_NON_CONSTANT_ATTRIBUTES = 2

BLK_XREF = 4  # This block is an external reference (xref)
BLK_XREF_OVERLAY = 8  # This block is an xref overlay
BLK_EXTERNAL = 16  # This block is externally dependent
BLK_RESOLVED = 32  # This is a resolved external reference, or dependent of an external reference (ignored on input)
BLK_REFERENCED = 64  # This definition is a referenced external reference (ignored on input)

LWPOLYLINE_CLOSED = 1
LWPOLYLINE_PLINEGEN = 128

TEXT_ALIGN_FLAGS = {
    'LEFT': (0, 0),
    'CENTER': (1, 0),
    'RIGHT': (2, 0),
    'ALIGNED': (3, 0),
    'MIDDLE': (4, 0),
    'FIT': (5, 0),
    'BOTTOM_LEFT': (0, 1),
    'BOTTOM_CENTER': (1, 1),
    'BOTTOM_RIGHT': (2, 1),
    'MIDDLE_LEFT': (0, 2),
    'MIDDLE_CENTER': (1, 2),
    'MIDDLE_RIGHT': (2, 2),
    'TOP_LEFT': (0, 3),
    'TOP_CENTER': (1, 3),
    'TOP_RIGHT': (2, 3),
}
TEXT_ALIGNMENT_BY_FLAGS = dict((flags, name) for name, flags in TEXT_ALIGN_FLAGS.items())


MTEXT_TOP_LEFT = 1
MTEXT_TOP_CENTER = 2
MTEXT_TOP_RIGHT = 3
MTEXT_MIDDLE_LEFT = 4
MTEXT_MIDDLE_CENTER = 5
MTEXT_MIDDLE_RIGHT = 6
MTEXT_BOTTOM_LEFT = 7
MTEXT_BOTTOM_CENTER = 8
MTEXT_BOTTOM_RIGHT = 9

MTEXT_LEFT_TO_RIGHT = 1
MTEXT_TOP_TO_BOTTOM = 3
MTEXT_BY_STYLE = 5

MTEXT_AT_LEAST = 1
MTEXT_EXACT = 2

MTEXT_COLOR_INDEX = {
    'red': 1,
    'yellow': 2,
    'green': 3,
    'cyan': 4,
    'blue': 5,
    'magenta': 6,
    'white': 7,
}

CLOSED_SPLINE = 1
PERIODIC_SPLINE = 2
RATIONAL_SPLINE = 4
PLANAR_SPLINE = 8
LINEAR_SPLINE = 16

# Hatch constants
HATCH_TYPE_USER_DEFINED = 0
HATCH_TYPE_PREDEFINED = 1
HATCH_TYPE_CUSTOM = 2

HATCH_STYLE_NORMAL = 0
HATCH_STYLE_OUTERMOST = 1
HATCH_STYLE_IGNORE = 2

BOUNDARY_PATH_DEFAULT = 0
BOUNDARY_PATH_EXTERNAL = 1
BOUNDARY_PATH_POLYLINE = 2
BOUNDARY_PATH_DERIVED = 4
BOUNDARY_PATH_TEXTBOX = 8
BOUNDARY_PATH_OUTERMOST = 16

GRADIENT_TYPES = frozenset([
    'LINEAR',
    'CYLINDER',
    'INVCYLINDER',
    'SPHERICAL',
    'INVSPHERICAL',
    'HEMISPHERICAL',
    'INVHEMISPHERICAL',
    'CURVED',
    'INVCURVED'
])


# Viewport Status Flags (VSF) group code=90
VSF_PERSPECTIVE_MODE = 0x1  # enabled if set
VSF_FRONT_CLIPPING = 0x2  # enabled if set
VSF_BACK_CLIPPING = 0x4  # enabled if set
VSF_USC_FOLLOW = 0x8  # enabled if set
VSF_FRONT_CLIPPING_NOT_AT_EYE = 0x10  # enabled if set
VSF_UCS_ICON_VISIBILITY = 0x20  # enabled if set
VSF_UCS_ICON_AT_ORIGIN = 0x40  # enabled if set
VSF_FAST_ZOOM = 0x80  # enabled if set
VSF_SNAP_MODE = 0x100  # enabled if set
VSF_GRID_MODE = 0x200  # enabled if set
VSF_ISOMETRIC_SNAP_STYLE = 0x400  # enabled if set
VSF_HIDE_PLOT_MODE = 0x800  # enabled if set
VSF_KISOPAIR_TOP = 0x1000  # If set and kIsoPairRight is not set, then isopair top is enabled. If both kIsoPairTop and kIsoPairRight are set, then isopair left is enabled
VSF_KISOPAIR_RIGHT = 0x2000  # If set and kIsoPairTop is not set, then isopair right is enabled
VSF_VIEWPORT_ZOOM_LOCKING = 0x4000  # enabled if set
VSF_CURRENTLY_ALWAYS_ENABLED = 0x8000  # always set without a meaning :)
VSF_NON_RECTANGULAR_CLIPPING = 0x10000  # enabled if set
VSF_TURN_VIEWPORT_OFF = 0x20000

# Viewport Render Mode (VRM) group code=281
VRM_2D_OPTIMIZED = 0
VRM_WIREFRAME = 1
VRM_HIDDEN_LINE = 2
VRM_FLAT_SHADED = 3
VRM_GOURAUD_SHADED = 4
VRM_FLAT_SHADED_WITH_WIREFRAME = 5
VRM_GOURAUD_SHADED_WITH_WIREFRAME = 6

IMAGE_SHOW = 1
IMAGE_SHOW_WHEN_NOT_ALIGNED = 2
IMAGE_USE_CLIPPING_BOUNDARY = 4
IMAGE_TRANSPARENCY_IS_ON = 8

UNDERLAY_CLIPPING = 1
UNDERLAY_ON = 2
UNDERLAY_MONOCHROME = 4
UNDERLAY_ADJUST_FOR_BG = 8

DIM_LINEAR = 0
DIM_ALIGNED = 1
DIM_ANGULAR = 2
DIM_DIAMETER = 3
DIM_RADIUS = 4
DIM_ANGULAR_3P = 5
DIM_ORDINATE = 6
DIM_REF = 32
DIM_ORDINATE_TYPE = 64
DIM_USER_LOCATION_OVERRIDE = 128

DimensionTypeNames = [
    'Rotated',  # 0
    'Aligned',  # 1
    'Angular',  # 2
    'Diameter',  # 3
    'Radial',   # 4
    'Angular3point',  # 5
    'Ordinate',  # 6
]

# ATTRIB & ATTDEF flags
ATTRIB_INVISIBLE = 1  # Attribute is invisible (does not appear)
ATTRIB_CONST = 2  # This is a constant attribute
ATTRIB_VERIFY = 4  # Verification is required on input of this attribute
ATTRIB_IS_PRESET = 8  # no prompt during insertion


class Error:
    MISSING_REQUIRED_ROOT_DICT_ENTRY = 1
    DUPLICATE_TABLE_ENTRY_NAME = 2
    POINTER_TARGET_NOT_EXISTS = 3
    TABLE_NOT_FOUND = 4
    UNDEFINED_LINETYPE = 100
    UNDEFINED_DIMENSION_STYLE = 101
    UNDEFINED_TEXT_STYLE = 102
    INVALID_LAYER_NAME = 200
    INVALID_COLOR_INDEX = 201
    INVALID_OWNER_HANDLE = 202


INVALID_LAYER_NAME_CHARACTERS = frozenset(['<', '>', '/', '\\',  '"', ':', ';', '?', '*', '|', '=', '`'])
