from osgeo import gdal

version = gdal.VersionInfo()

assert version == "3120200"

print(f"GDAL version: {version}")