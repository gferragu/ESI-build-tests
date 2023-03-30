import pooch

gmprocess_tests = pooch.create(
    # Use the default cache folder for the operating system
    path=pooch.os_cache("gmprocess"),
    base_url="https://code.usgs.gov/ghsc/esi/groundmotion-processing/-/raw/main/tests/",
    # The registry specifies the files that can be fetched
    registry={
        "gmprocess_registry.txt": "sha256:19uheidhlkjdwhoiwuhc0uhcwljchw9ochwochw89dcgw9dcgwc",
    },
)
