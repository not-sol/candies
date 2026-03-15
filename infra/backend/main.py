from fastapi import FastAPI
from mangum import Mangum
from controllers.app_controller import app_controller

app = FastAPI()
app_controller(app)
handler = Mangum(app)
