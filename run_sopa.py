import sopa
import spatialdata

imagepath = "./EHP601_25_1_Stitched_cropped.tif"

print("Opening image")

dataset = sopa.io.ome_tif(imagepath, as_image=False)

print("Saving as Zarr...")

dataset.write("./demo.zarr", overwrite=True)

print("Loading Zarr...")

dataset = spatialdata.read_zarr("./demo.zarr")  # we can read the data back

print("Make image patches...")

sopa.make_image_patches(dataset)

print("Set dask backend...")

sopa.settings.parallelization_backend = "dask"

print("Get channel names...")

channels = sopa.utils.get_channel_names(dataset)

print(channels)

print("Run stardist...")

sopa.segmentation.stardist(dataset, model_type='2D_versatile_fluo', channels=str(channels[0]))

print("Aggregating...")

sopa.aggregate(dataset)

print("Generating report...")

sopa.io.write_report("report.html", dataset)

print("Done")
