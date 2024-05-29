from fastapi.middleware.cors import CORSMiddleware
from api.routers.admin import router as login_router
from api.routers.user import router as user_router
import fastapi

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login_router)
app.include_router(user_router)
