#!/usr/bin/env python

from gimpfu import *

def landscape_inator(dirname, color, max_width):
    pdb.gimp_context_push()

    pattern_jpg = dirname + "\\*.jpg"
    pattern_jpeg = dirname + "\\*.jpeg"

    encoding = 1 # filename encoding
    num_files_jpg, files_jpg = pdb.file_glob(pattern_jpg, encoding)
    num_files_jpeg, files_jpeg = pdb.file_glob(pattern_jpeg, encoding)

    num_files = num_files_jpg + num_files_jpeg
    files = files_jpg + files_jpeg

    for filename in files:
        image = pdb.gimp_file_load(filename, filename)
        drawable = pdb.gimp_image_get_active_layer(image)

        width = pdb.gimp_image_width(image)
        height = pdb.gimp_image_height(image)

        if height > width:
            new_width = height
            offx = (new_width - width) / 2
            offy = 0
            pdb.gimp_image_resize(image, new_width, height, offx, offy)

            type = 0 # RGB-IMAGE
            name = ""
            opacity = 100
            mode = 28 # LAYER-MODE-NORMAL
            new_layer = pdb.gimp_layer_new(image, new_width, height, type, name, opacity, mode)

            parent = None
            num_layers, layer_ids = pdb.gimp_image_get_layers(image)
            position = num_layers + 1
            pdb.gimp_image_insert_layer(image, new_layer, parent, position)

            foreground = color
            pdb.gimp_context_set_foreground(foreground)

            drawable = new_layer
            fill_type = 0 # FILL-FOREGROUND
            pdb.gimp_edit_fill(drawable, fill_type)

            merge_type = 1 # CLIP-TO-IMAGE
            drawable = pdb.gimp_image_merge_visible_layers(image, merge_type)

            width = new_width

        new_width = min(width, max_width)
        new_height = height * (1.0 * new_width / width)
        pdb.gimp_image_scale(image, new_width, new_height)

        filename_split = filename.split(".")
        filename_landscape = ".".join(filename_split[:-1]) + "_quer." + filename_split[-1]
        pdb.gimp_file_save(image, drawable, filename_landscape, filename_landscape)

    pdb.gimp_context_pop()


register(
    "python-fu-landscape-inator",
    "Verwandelt hochformatige Bilder in quadratische.",
    "Fuegt Bildern im Hochformat einen farbigen Rand hinzu, sodass sie quadratisch sind.",
    "Maximilian Schoen", "Maximilian Schoen", "2021",
    "Querformat-inator",
    "", 
    [
        (PF_DIRNAME, "dirname", "Verzeichnis", None),
        (PF_COLOR, "color", "Fuellfarbe", (255, 255, 255)),
        (PF_SPINNER, "max_width", "Max. Bildbreite", 1920, (1, 9999, 1))
    ],
    [],
    landscape_inator, menu="<Image>/File/Create")


main()
