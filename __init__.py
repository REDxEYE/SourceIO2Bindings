import bpy

from SourceIO2Bindings.source2.model import SOURCEIO2_OT_VMDLImport

bl_info = {
    "name": "SourceIO 2.0",
    "author": "RED_EYE, ShadelessFox, Syborg64",
    "version": (0, 0, 1),
    "blender": (3, 0, 0),
    "location": "File > Import-Export > SourceIO 2.0",
    "description": "Source2 Engine assets(.vmat_c, .vmdl_c, .vwrld_c, .vtex_c)",
    "category": "Import-Export"
}

classes = (
    SOURCEIO2_OT_VMDLImport,
)

register_, unregister_ = bpy.utils.register_classes_factory(classes)


def register():
    register_()


def unregister():
    unregister_()
