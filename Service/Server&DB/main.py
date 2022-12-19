from typing import Optional, Union
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.logger import logger
from  Inference_model import inference_model
import logging
from pydantic import BaseModel
import sqlite3
import os
import sys
import pickle
import json
from query_DB import build_query_statement, query_result
from fastapi.encoders import jsonable_encoder


sys.path.insert(0, 'model')


logger = logging.getLogger('gunicorn.error')


app = FastAPI()
con = sqlite3.connect('db_test2.db', check_same_thread=False)
cur = con.cursor()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

columns = {'0': ['대분류', '모션', '저상', '수납', '헤드'], '1': ['대분류', '팔걸이', '등받이', '다리형태']}

with open('actual_cls_mapping1', 'rb') as fp:
    cls_mapper = pickle.load(fp)


@app.post("/inference")
async def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        message = "error"
    else:
        message = inference_model('best.onnx', file.filename, cls_mapper, columns)
    finally:
        file.file.close()
        os.remove(file.filename)
    filtered_message = list()
    while len(message) != 0:
        detection = message.pop()
        message = [i for i in message if i != detection]
        filtered_message.append(detection)
    
    if filtered_message is None:
        return  None
    else:

        result = list()
        for detection in filtered_message:
            result.append(build_query_statement(detection, cur, columns))
        return {"result": result}



class tt(BaseModel):
    def items(self):
        return [('대분류', self.대분류), ('브랜드', self.브랜드), ('팔걸이', self.팔걸이), ('등받이', self.등받이), ('다리형태', self.다리형태), ('모션', self.모션), ('저상', self.저상형), ('수납', self.수납형), ('헤드', self.헤드), ('색상태그', self.색상태그), ('주요재질', self.주요재질)]

    대분류:int
    브랜드:Optional[str] = None
    팔걸이:Optional[int] = None
    등받이:Optional[int] = None
    다리형태:Optional[int] = None
    모션:Optional[int] = None
    저상형:Optional[int] = None
    수납형:Optional[int] = None
    헤드:Optional[int] = None
    색상태그:Optional[list] = None
    주요재질:Optional[list] = None


@app.post('/edittags/')
async def edit_tags(item:tt):
    result = list()
    result.append(build_query_statement(item, cur, columns))
    return {'result' : result}
    