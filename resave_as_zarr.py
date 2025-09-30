import sopa

imagepath = "/EHP601_25_1_Stitched_cropped.ome.tif"

print("Opening image")

dataset = sopa.io.ome_tif(imagepath, as_image=False)

print("Saving as Zarr...")

dataset.write("./demo.zarr", overwrite=True)

print("Done")
