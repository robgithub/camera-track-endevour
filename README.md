Camera Track Endevour
=====================

A set of Python scripts and Blender files to make basic automated rotating renders from the command line with various materials.

I expect to expand on this README in the near future.

and yes, I am aware that Endeavour is spelt wrong.

Example:

cameras=(Camera.top Camera.bottom)
materials=(LL_WireTrans LL_WireHold LL_Clay LL_Glass)
SOURCE=/home/me/projects/blender/Raspberry\ Pi\ 3\ Model\ B\ HiRes/circuitboard68.blend
NAME=C068
LAYERS=0,9
for cam in ${cameras[@]}; do
  for mat in ${materials[@]}; do
   ./blender --background "$SOURCE" --python ~/projects/blender/camera\ track\ endevour/track.py --python ~/projects/blender/camera\ track\ endevour/materials.py --python ~/projects/blender/camera\ track\ endevour/setup.py -noaudio --python ~/projects/blender/camera\ track\ endevour/render.py --  -c "$cam" -m "$mat" -n "$NAME" -l "$LAYERS"
  done
  ./blender --background "$SOURCE" --python ~/projects/blender/camera\ track\ endevour/track.py --python ~/projects/blender/camera\ track\ endevour/materials.py --python ~/projects/blender/camera\ track\ endevour/setup.py -noaudio --python ~/projects/blender/camera\ track\ endevour/render.py --  -c "$cam" -n "$NAME" -l "$LAYERS"
done

Will loop through all the cameras and for each camera loop through all the materials uncluding 'unset', which simply does not over ride the materials.
So this will create

C068_Camera.bottom_LL_Clay.avi0001-0360.mkv
C068_Camera.bottom_LL_Glass.avi0001-0360.mkv
C068_Camera.bottom_LL_WireHold.avi0001-0360.mkv
C068_Camera.bottom_LL_WireTrans.avi0001-0360.mkv
C068_Camera.bottom_unset.avi0001-0360.mkv
C068_Camera.top_LL_Clay.avi0001-0360.mkv
C068_Camera.top_LL_Glass.avi0001-0360.mkv
C068_Camera.top_LL_WireHold.avi0001-0360.mkv
C068_Camera.top_LL_WireTrans.avi0001-0360.mkv
C068_Camera.top_unset.avi0001-0360.mkv

I have also added a new file render_final.py that can be swapped in the last part of the command for render.py that will set a higher resolution and samples.

In fact I used it with

./blender "$SOURCE" --python ~/projects/blender/camera\ track\ endevour/track.py --python ~/projects/blender/camera\ track\ endevour/materials.py --python ~/projects/blender/camera\ track\ endevour/setup.py -noaudio --  -c "$cam" -n "$NAME" -l "$LAYERS"

which did not do any rendering but opened up Blender with the $SOURCE .blend file with the track and materials all setup. Then I tweaked the animation (add a camera focus with Depth of Field) save the file as a new name.

Then, I ran

./blender --background "$NEWSOURCE" --python ~/projects/blender/camera\ track\ endevour/setup.py -noaudio --python ~/projects/blender/camera\ track\ endevour/render_final.py --  -c "$cam" -n "$NEWNAME" -l "$LAYERS"

Note the $NEWSOURCE and $NEWNAME, also the $cam was set to Camera.top.
