from fastapi import FastAPI
from utils import get_json_from_history_data
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


app = FastAPI()

@app.get("/history/{name_of_company}")
def history_json(name_of_company:str):
    data = get_json_from_history_data(name_of_company=name_of_company)
    json_compatible_item_data = jsonable_encoder(data)
    if not json_compatible_item_data:
        return JSONResponse(content={'Error':'No data'})
    return JSONResponse(content=json_compatible_item_data)