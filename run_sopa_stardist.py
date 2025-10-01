import sopa
import spatialdata

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

sopa.segmentation.stardist(dataset, model_type='2D_versatile_fluo', channels='0')

print("Done")
