# Concurrent LRU KV Store

An in-memory, thread-safe **Least Recently Used (LRU)** cache exposed via a **REST API**.  
This project blends fundamental computer science concepts — concurrency, caching, and API design — into a practical key-value store.

## 🚀 Features
- Thread-safe operations using locks or concurrent data structures  
- Configurable cache size with automatic eviction (LRU policy)  
- RESTful endpoints for CRUD operations  
- JSON-based request/response format  
- Lightweight and fast — ideal for microservices or local caching

## 🧩 Tech Stack
- Language: Go / Rust / Python (choose your implementation)
- Framework: [Gin / FastAPI / Actix] for REST API
- Testing: Unit + Integration tests
- Build: Dockerfile for containerization

## ⚙️ Installation
```bash
git clone https://github.com/Shripad1ve/concurrent-lru-kvstore.git
cd concurrent-lru-kvstore
