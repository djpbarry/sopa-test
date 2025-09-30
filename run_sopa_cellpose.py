import sopa
import spatialdata

print("Loading Zarr...")

dataset = spatialdata.read_zarr("demo.zarr")  # we can read the data back

print("Make image patches...")

sopa.make_image_patches(dataset)

print("Set dask backend...")

sopa.settings.parallelization_backend = "dask"

print("Get channel names...")

channels = sopa.utils.get_channel_names(dataset)

print(channels)

print("Run cellpose...")

sopa.segmentation.cellpose(dataset, "DAPI (DAPI)", diameter=35, key_added="nuclei", gpu=True, overwrite=True)

print("Done")
