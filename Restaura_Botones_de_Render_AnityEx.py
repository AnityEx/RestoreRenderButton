# coding: utf-8
bl_info = {
    "name": "Restaura botones de render por AnityEx",
    "description": "Boton de render restaurados como blender 2.79b y dos botones extras",
    "author": "AnityEx",
    "version": (1, 1, 0),
    "blender": (3,0),
    "location": "Properties>Output>Render",
    "warning": "",
    "wiki_url": "https://www.anityex.com",
    "category": "Object" }


import bpy

class BotonRenderAnity (bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Render"
    bl_idname = "SCENE_RENDER_BOTON"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "output"
    bl_order = 1  # <-- Set the panel's order to 1

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        
        row = layout.row(align=True)
        row.scale_y = 1.5
        
        sub = row.row(align=True)
        sub.scale_x = 0.9
        sub.operator("render.render", text="Render", icon='RENDER_STILL')
        
        row.operator("render.render", text="Animation", icon='RENDER_ANIMATION').animation = True
        
        sub = row.row(align=True)
        sub.scale_x = 0.8
        sub.operator("sound.mixdown", text="Audio", icon='SOUND')
        
        """botones extra para viewport render"""
        row = layout.row(align=True)
        row.scale_y = 1.2
        row.operator("render.opengl", text="Viewport", icon="FILE_IMAGE")
        row.operator("render.opengl", text="Viewport Anim", icon='RENDERLAYERS').animation = True

def register():
    bpy.utils.register_class(BotonRenderAnity)


def unregister():
    bpy.utils.unregister_class(BotonRenderAnity)


if __name__ == "__main__":
    register()
