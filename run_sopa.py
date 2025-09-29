import sopa
import spatialdata

imagepath = "/nemo/stp/lm/inputs/lil/ForDave/EHP601_25_1_Stitched.ome.tif"

dataset = sopa.io.ome_tif(imagepath, as_image=False)

dataset.write("./demo.zarr")

dataset = spatialdata.read_zarr("demo.zarr")  # we can read the data back

sopa.make_image_patches(dataset)

channels = sopa.utils.get_channel_names(dataset)

print(channels)

sopa.segmentation.cellpose(dataset, "DAPI (DAPI)", diameter=35, key_added="nuclei", gpu=True)

print("Done")