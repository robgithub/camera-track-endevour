import bpy, math

print("Camera tracking script starting")
TARGET="Empty.target"
TRACK="Curve.camera.track"
CAMERATOP="Camera.top"
CAMERABOTTOM="Camera.bottom"
TRACKSIZE=11

#Set the layer and ensure not in EDIT mode
bpy.context.scene.layers[0] = True
bpy.ops.object.mode_set(mode='OBJECT')

# Create empty(camera target)
bpy.ops.object.empty_add(type='SPHERE', view_align=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.object.name = TARGET
# Create camera track curve
bpy.ops.curve.primitive_bezier_circle_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.object.name = TRACK
bpy.context.object.scale[1] = TRACKSIZE
bpy.context.object.scale[2] = TRACKSIZE
bpy.context.object.scale[0] = TRACKSIZE
# Create Top camera
bpy.ops.object.camera_add(view_align=True, enter_editmode=False, location=(0, 0, 0), rotation=(0,0,0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.object.name = CAMERATOP
# Parent to camera track
bpy.data.objects[TRACK].select = True
bpy.context.scene.objects.active = bpy.data.objects[TRACK]
bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)
bpy.data.objects[TRACK].select = False
bpy.context.scene.objects.active = bpy.data.objects[CAMERATOP]
bpy.context.object.location[1] = 0-TRACKSIZE     # Y
bpy.context.object.location[2] = 3     # Z
# Create tracking constraint
bpy.ops.object.constraint_add(type='LOCKED_TRACK')
bpy.context.object.constraints["Locked Track"].target = bpy.data.objects[TARGET]
bpy.context.object.constraints["Locked Track"].track_axis = 'TRACK_NEGATIVE_Z'
bpy.context.object.constraints["Locked Track"].lock_axis = 'LOCK_X'
# Create Bottom camera
bpy.ops.object.duplicate() 
bpy.context.object.name = CAMERABOTTOM
bpy.context.object.location[2] = -3     # Z
bpy.data.objects[CAMERABOTTOM].select = False
# Create orbit animation
bpy.data.objects[TRACK].select = True
# NOPE bpy.context.user_preferences.edit.keyframe_new_interpolation_type ='LINEAR'
# NOPE bpy.ops.anim.keyframe_insert_menu(type='Rotation')
bpy.context.scene.frame_current = 0
bpy.data.objects[TRACK].keyframe_insert(data_path='rotation_euler', frame=(bpy.context.scene.frame_current))
bpy.context.scene.frame_end = 360
bpy.context.scene.frame_current = 360
bpy.data.objects[TRACK].rotation_euler = ( 0, 0, math.radians(359) )
# NOPE bpy.ops.transform.rotate(value=6.283, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
bpy.data.objects[TRACK].keyframe_insert(data_path='rotation_euler', frame=(bpy.context.scene.frame_current))
# Set interpolation
for fc in bpy.data.objects[TRACK].animation_data.action.fcurves:
    fc.extrapolation = 'LINEAR'
    for kp in fc.keyframe_points:
        kp.interpolation = 'LINEAR'

print("Camera tracking script finished setup")
