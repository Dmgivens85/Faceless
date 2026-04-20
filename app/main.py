from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.config import settings
from app.database import Base, SessionLocal, engine
from app.routes import breakdown_builder, content_planner, dashboard, hook_writer, ideas, scene_finder
from app.seed import seed_database


BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


app = FastAPI(title=settings.app_name)
app.state.templates = templates
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


@app.on_event("startup")
def startup() -> None:
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        seed_database(db)


app.include_router(dashboard.router, tags=["dashboard"], dependencies=[])
app.include_router(scene_finder.router, tags=["scene-finder"])
app.include_router(hook_writer.router, tags=["hook-writer"])
app.include_router(breakdown_builder.router, tags=["breakdown-builder"])
app.include_router(content_planner.router, tags=["content-planner"])
app.include_router(ideas.router, tags=["ideas"])
