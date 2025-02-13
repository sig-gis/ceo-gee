from fastapi import Request, APIRouter
from app.core.utils import initialize
from app.core.gee_features import (
    imageCollection,
    filteredLandsat,
    filteredNicfi,
    filteredSentinel2,
    filteredSentinelSAR,
    imageCollectionByIndex,
    featureCollection,
    getPlanetTile,
    timeSeriesByIndex,
    degradationTimeSeries,
    degradationTileUrl,
    image,
    getAvailableBands,
    statistics
)

router = APIRouter(prefix="/gee")

@router.post("/initialize/")
async def init(request: Request):
    payload = await request.json()
    return initialize(payload["ee_account"], payload["ee_key_path"])

@router.post("/image-collection/")
async def image_collection(request: Request):
    payload = await request.json()
    return imageCollection(payload)

@router.post("/filtered-nicfi/")
async def filtered_nicfi(request: Request):
    payload = await request.json()
    return filteredNicfi(payload)

@router.post("/filtered-landsat/")
async def filtered_landsat(request: Request):
    payload = await request.json()
    return filteredLandsat(payload)

@router.post("/filtered-sentinel/")
async def filtered_sentinel(request: Request):
    payload = await request.json()
    return filteredSentinel2(payload)

@router.post("/filtered-sentinel-sar/")
async def filtered_sentinel_sar(request: Request):
    payload = await request.json()
    return filteredSentinelSAR(payload)

@router.post("/image-collection-by-idx/")
async def image_collection_idx(request: Request):
    payload = await request.json()
    return imageCollectionByIndex(payload)

@router.post("/feature-collection/")
async def feature_collection(request: Request):
    payload = await request.json()
    return featureCollection(payload)

@router.post("/planet-tile/")
async def planet_tile(request: Request):
    payload = await request.json()
    return getPlanetTile(payload)

@router.post("/time-series-by-idx/")
async def time_series_idx(request: Request):
    payload = await request.json()
    return timeSeriesByIndex(payload)

@router.post("/degradation-time-series/")
async def degradation_time_series(request: Request):
    payload = await request.json()
    return degradationTimeSeries(payload)

@router.post("/degradation-tile-url/")
async def degradation_tile_url(request: Request):
    payload = await request.json()
    return degradationTileUrl(payload)

@router.post("/image/")
async def img(request: Request):
    payload = await request.json()
    return image(payload)

@router.post("/get-available-bands/")
async def get_available_bands(request: Request):
    payload = await request.json()
    return getAvailableBands(payload)

@router.post("/statistics/")
async def stats(request: Request):
    payload = await request.json()
    return statistics(payload)
