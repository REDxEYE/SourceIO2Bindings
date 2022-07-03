from pathlib import Path

import bpy
from bpy.props import StringProperty, BoolProperty, CollectionProperty, FloatProperty

from SourceIO2Bindings.SourceIO2.utils import SOURCE2_HAMMER_UNIT_TO_METERS


class SOURCEIO2_OT_VMDLImport(bpy.types.Operator):
    """Load Source2 VMDL"""
    bl_idname = "sourceio2.vmdl"
    bl_label = "Import Source2 VMDL file"
    bl_options = {'UNDO'}

    filepath: StringProperty(subtype="FILE_PATH")
    files: CollectionProperty(name='File paths', type=bpy.types.OperatorFileListElement)
    filter_glob: StringProperty(default="*.vmdl_c", options={'HIDDEN'})

    scale: FloatProperty(name="World scale", default=SOURCE2_HAMMER_UNIT_TO_METERS, precision=6)

    def execute(self, context):
        if Path(self.filepath).is_file():
            directory = Path(self.filepath).parent.absolute()
        else:
            directory = Path(self.filepath).absolute()

        file_count = len(self.files)
        for n, file in enumerate(self.files):
            print(f"Loading {n + 1}/{file_count}")
            print(str(directory / file.name))

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}
