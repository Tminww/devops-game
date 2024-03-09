from src.main import app
import uvicorn

# FIXME dev server for poetry

server = uvicorn.run(app=app, host="127.0.0.1", port=8000, log_level="info")
