import bpy
import sys       # to get command line args
import argparse  # to parse options for us and print a nice help message

# argument parsing code from https://developer.blender.org/diffusion/B/browse/master/release/scripts/templates_py/background_job.py

def main():
    import sys       # to get command line args
    import argparse  # to parse options for us and print a nice help message

    # get the args passed to blender after "--", all of which are ignored by
    # blender so scripts may receive their own arguments
    argv = sys.argv

    if "--" not in argv:
        argv = []  # as if no args are passed
    else:
        argv = argv[argv.index("--") + 1:]  # get all args after "--"

    # When --help or no args are given, print this help
    usage_text = (
            "Run blender with this script:"
            "  blender --python " + __file__ + " -- [options]"
            )

    parser = argparse.ArgumentParser(description=usage_text)

    # Possible types are: string, int, long, choice, float and complex.
    parser.add_argument("-m", "--material", dest="material", type=str, required=False,
            help="This material will be used for the render layers")

    parser.add_argument("-l", "--layers", dest="layers", type=str, required=False,
            help="This comma separated list of layer numbers defines which are the render layers")

    parser.add_argument("-c", "--camera", dest="camera", type=str, required=False,
            help="Camera to set active")

    parser.add_argument("-n", "--name", dest="name", type=str, required=False,
            help="file name prefix")

#    parser.add_argument("-s", "--save", dest="save_path", metavar='FILE',
#            help="Save the generated file to the specified path")
#    parser.add_argument("-r", "--render", dest="render_path", metavar='FILE',
#            help="Render an image to the specified path")

    args = parser.parse_args(argv)  # In this example we wont use the args

    if not argv:
        parser.print_help()
        return

    # Run the example function
    #example_function(args.text, args.save_path, args.render_path)
    print("setting up")

    cname='unset'
    matname='unset'
    name='unset'
    # Set layers 
    if args.layers :
      print("--layers", args.layers)
      layerarray=args.layers.split(',')
      for i in range(len(bpy.context.scene.layers)) :
        if str(i) in layerarray :
          bpy.context.scene.layers[i]=True
        else :
          bpy.context.scene.layers[i]=False

    # Set render material
    if args.material:
      print("--material", args.material)
      matname = args.material
      if args.material in bpy.data.materials :
        bpy.context.scene.render.layers["RenderLayer"].material_override = bpy.data.materials[args.material]

    # set camera
    if args.camera:
      print("--camera", args.camera)
      cname = args.camera
      if args.camera in bpy.data.objects :
        bpy.context.scene.camera = bpy.data.objects[args.camera]

    # set file name
    if args.name:
      print("--name", args.name)
      name = args.name

    OUTPUTFILENAME='/home/rednuht/temp/' + name + '_' + cname + '_' + matname + '.avi'
    bpy.context.scene.render.filepath = OUTPUTFILENAME
    print("set up complete")

# call main function
main()

