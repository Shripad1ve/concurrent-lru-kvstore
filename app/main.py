from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Any
from app.lru_engine import ThreadSafeLRUCache

app = FastAPI(title="High-Throughput LRU Cache Service")
cache = ThreadSafeLRUCache(capacity=5000)

class CacheItem(BaseModel):
    key: str
    value: Any

@app.get("/cache/{key}", status_code=status.HTTP_200_OK)
def read_cache(key: str):
    value = cache.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found or expired")
    return {"key": key, "value": value}

@app.post("/cache", status_code=status.HTTP_201_CREATED)
def write_cache(item: CacheItem):
    cache.put(item.key, item.value)
    return {"status": "success", "key": item.key}

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "healthy"}
