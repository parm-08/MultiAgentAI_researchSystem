"""
main.py
FastAPI wrapper around the existing multi-agent research pipeline.
Nothing in pipeline.py / agents.py is modified — this file only calls
run_research_pipeline() and exposes it over HTTP for the HTML/CSS/JS frontend.
"""

import asyncio
import logging

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from pipeline import run_research_pipeline

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("research-api")

app = FastAPI(
    title="Multi-Agent Research API",
    description="HTTP layer over the search -> read -> write -> critique pipeline",
    version="1.0.0",
)

# Allow the static frontend (served from anywhere, e.g. Live Server on a
# different port) to call this API during development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ResearchRequest(BaseModel):
    topic: str = Field(..., min_length=1, description="Research topic to investigate")


class ResearchResponse(BaseModel):
    topic: str
    search_results: str
    scraped_content: str
    report: str
    feedback: str


@app.get("/api/health")
async def health():
    return {"status": "ok"}


@app.post("/api/research", response_model=ResearchResponse)
async def research(payload: ResearchRequest):
    topic = payload.topic.strip()
    if not topic:
        raise HTTPException(status_code=400, detail="Topic cannot be empty.")

    logger.info("Starting research pipeline for topic: %s", topic)

    try:
        # run_research_pipeline() is fully synchronous (blocking) LangChain/agent
        # code. asyncio.to_thread() runs it in a worker thread so it doesn't
        # freeze the FastAPI event loop while it's working.
        state = await asyncio.to_thread(run_research_pipeline, topic)
    except Exception as exc:  # noqa: BLE001
        logger.exception("Pipeline failed for topic: %s", topic)
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return ResearchResponse(
        topic=topic,
        search_results=str(state.get("search_results", "")),
        scraped_content=str(state.get("scraped_content", "")),
        report=str(state.get("report", "")),
        feedback=str(state.get("feedback", "")),
    )


# Serve the frontend (index.html, style.css, script.js) from ./static
# Keep this mounted LAST so it doesn't shadow the /api routes above.
app.mount("/", StaticFiles(directory="static", html=True), name="static")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
