import scanpy as sc
import sopa
import spatialdata
import squidpy as sq

#imagepath = "./EHP601_25_1_Stitched_cropped.tif"

#print("Opening image")

#dataset = sopa.io.ome_tif(imagepath, as_image=False)

#print("Saving as Zarr...")

#dataset.write("./demo.zarr", overwrite=True)

print("Loading Zarr...")

dataset = spatialdata.read_zarr("./demo.zarr")  # we can read the data back

#print("Make image patches...")

#sopa.make_image_patches(dataset)

print("Set dask backend...")

sopa.settings.parallelization_backend = "dask"

#print("Get channel names...")

#channels = sopa.utils.get_channel_names(dataset)

#print(channels)

#print("Run stardist...")

#sopa.segmentation.stardist(dataset, model_type='2D_versatile_fluo', channels=str(channels[0]))

#print("Aggregating...")

#sopa.aggregate(dataset)
adata = dataset['table']

#print("Generating report...")

#sopa.io.write_report("report.html", dataset)

# Step 1: Preprocess and cluster based on intensity data
# Normalize the data
sc.pp.normalize_total(adata)

# Compute PCA for dimensionality reduction
sc.tl.pca(adata)

# Compute neighborhood graph
sc.pp.neighbors(adata, n_neighbors=15, n_pcs=10)

sc.tl.umap(adata)

# Using the igraph implementation and a fixed number of iterations can be significantly faster,
# especially for larger datasets
sc.tl.leiden(adata, flavor="igraph", n_iterations=2)

sc.pl.umap(adata, color=["leiden"])

print("Saving as Zarr...")

dataset.write("./demo.zarr", overwrite=True)

sq.pl.spatial_scatter(adata)

print("Done")
