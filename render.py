# Blender render settings
# FYI : only uses default "Scene"
import bpy

FILEFORMAT='FFMPEG' # 'PNG'
#bpy.data.scenes[my_scene_name_here].file_format = 'H264'
#bpy.data.scenes[my_scene_name_here].format = 'H264'
#bpy.data.scenes[my_scene_name_here].use_lossless_output = True
OUTPUTFILENAME='/home/rednuht/temp/'

bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
bpy.context.scene.render.resolution_percentage = 25
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 360
bpy.context.scene.frame_step = 1
bpy.context.scene.render.pixel_aspect_x = 1
bpy.context.scene.render.pixel_aspect_y = 1
bpy.context.scene.render.use_file_extension = True
bpy.context.scene.render.image_settings.color_mode ='RGB'
bpy.context.scene.render.image_settings.file_format=FILEFORMAT 
bpy.context.scene.render.image_settings.compression = 90
#bpy.context.scene.render.use_stamp = 1
#bpy.context.scene.render.stamp_background = (0,0,0,1)

bpy.context.scene.render.use_antialiasing = True
##sampling;=path tracing 
bpy.context.scene.cycles.progressive = 'PATH'
bpy.context.scene.cycles.samples = 50
bpy.context.scene.cycles.max_bounces = 1
bpy.context.scene.cycles.min_bounces = 1
bpy.context.scene.cycles.glossy_bounces = 1
bpy.context.scene.cycles.transmission_bounces = 1
bpy.context.scene.cycles.volume_bounces = 1
bpy.context.scene.cycles.transparent_max_bounces = 1
bpy.context.scene.cycles.transparent_min_bounces = 1
bpy.context.scene.cycles.use_progressive_refine = True

#Render results
#bpy.ops.render.render(write_still=True)
bpy.ops.render.render(animation=True)























