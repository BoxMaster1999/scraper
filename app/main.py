from fastapi import FastAPI, status

from app.internal import scrap_router


app = FastAPI(title='Scraper',
              description='Fastapi service for scrap html',
              version='0.1')

# Adding v1 namespace route
app.include_router(scrap_router)


@app.get('/health',
         tags=['System probs'])
def health() -> int:
    return status.HTTP_200_OK
