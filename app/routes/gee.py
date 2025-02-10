from fastapi import Request, APIRouter
from app.core.gee_features import (
    imageCollection,
    filteredLandsat,
    filteredNicfi,
    filteredSentinel,
    imageCollectionByIndex,
    featureCollection,
    getPlanetTile,
    timeSeriesByIndex,
    degradationTimeSeries,
    degradationTileUrl
)

router = APIRouter()

@router.post("image-collection/")
def image_collection(request: Request):
    payload = await request.json()
    return imageCollection(payload)

@router.post("filtered-landsat/")
def filtered_landsat(request: Request):
    payload = await request.json()
    return filteredLandsat(payload)

@router.post("filtered-nicfi/")
def filtered_nicfi(request: Request):
    payload = await request.json()
    return filteredNicfi(payload)

@router.post("filtered-landsat/")
def filtered_landsat(request: Request):
    payload = await request.json()
    return filteredLandsat(payload)

@router.post("filtered-sentinel/")
def filtered_sentinel(request: Request):
    payload = await request.json()
    return filteredSentinel(payload)

@router.post("filtered-sentinel-sar/")
def filtered_sentinel_sar(request: Request):
    payload = await request.json()
    return filteredSentinel(payload)

@router.post("image-collection-by-idx/")
def image_collection_idx(request: Request):
    payload = await request.json()
    return imageCollectionByIndex(payload)

@router.post("feature-collection/")
def feature_collection(request: Request):
    payload = await request.json()
    return featureCollection(payload)

@router.post("planet-tile/")
def planet_tile(request: Request):
    payload = await request.json()
    return getPlanetTile(payload)

@router.post("time-series-idx/")
def time_series_idx(request: Request):
    payload = await request.json()
    return timeSeriesByIndex(payload)

@router.post("degradation-time-series/")
def degradation_time_series(request: Request):
    payload = await request.json()
    return degradationTimeSeries(payload)

@router.post("degradation-tile-url/")
def degradation_tile_url(request: Request):
    payload = await request.json()
    return degradationTileUrl(payload)
