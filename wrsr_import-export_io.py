bl_info = {
    "name": "Workers & Resources Quick IO",
    "author": "Lex713",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > WRSR",
    "description": "Adds quick access buttons for NMF/NAF import/export",
    "category": "Import-Export",
}

import bpy


class WRTOOLS_PT_panel(bpy.types.Panel):
    bl_label = "Import-Export IO"
    bl_idname = "WRTOOLS_PT_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "WRSR"

    def draw(self, context):
        layout = self.layout

        layout.label(text="Import / Export")

        # Import NMF
        layout.operator("file.nmf", text="Import NMF", icon="IMPORT")

        # Export NMF
        layout.operator("export_object.nmf", text="Export NMF", icon="EXPORT")

        # Export NAF
        layout.operator("export_anim.naf", text="Export NAF", icon="EXPORT")


classes = (
    WRTOOLS_PT_panel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
