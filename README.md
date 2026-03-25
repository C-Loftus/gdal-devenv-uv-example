# gdal-devenv-uv-example

GDAL is often difficult to version control for geospatial workflows since it does not provide prebuilt wheels on some platforms. The version of libgdal can also vary across brew, ubuntu, debian, and other package managers / Linux distributions. This is an example of how to use devenv to test gdal bindings with a uv-based Python environment.

## Usage

To test the gdal bindings:

```sh
devenv shell

python3 main.py
```
