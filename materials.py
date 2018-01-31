import bpy

print("Material library script starting")
# Load materials
# Current materials
#
# LL_WireTrans
# LL_WireHold
# LL_Clay
# LL_Glass
# 
bpy.ops.wm.link(filepath="/home/rednuht/projects/blender/camera track endevour/materiallibrary.blend/Material/LL_WireTrans", directory="/home/rednuht/projects/blender/camera track endevour/materiallibrary.blend/Material/", filename="LL_WireTrans", files=[{"name":"LL_Clay", "name":"LL_Clay"}, {"name":"LL_Glass", "name":"LL_Glass"}, {"name":"LL_WireHold", "name":"LL_WireHold"}, {"name":"LL_WireTrans", "name":"LL_WireTrans"}], relative_path=True)
print("Material library script finished")
