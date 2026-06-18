from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np


app = FastAPI()



@app.get("/")
def home():

    return {
        "status":"GishFit AI Measurement API running"
    }




@app.post("/measure")
async def measure(

    front: UploadFile = File(...),

    side: UploadFile = File(...),

    back: UploadFile = File(...)

):


    front_bytes = await front.read()

    side_bytes = await side.read()

    back_bytes = await back.read()



    front_image = cv2.imdecode(

        np.frombuffer(front_bytes,np.uint8),

        cv2.IMREAD_COLOR

    )


    side_image = cv2.imdecode(

        np.frombuffer(side_bytes,np.uint8),

        cv2.IMREAD_COLOR

    )


    back_image = cv2.imdecode(

        np.frombuffer(back_bytes,np.uint8),

        cv2.IMREAD_COLOR

    )



    if front_image is None or side_image is None or back_image is None:


        return {

            "error":"Invalid images"

        }





    # TEMPORARY AI PIPELINE PLACEHOLDER
    # This is where the body model goes

    measurements = {


        "neck":39,

        "chest":102,

        "waist":86,

        "hip":98,

        "shoulder":48,

        "sleeve":63,

        "bicep":35,

        "thigh":57,

        "calf":39,

        "ankle":24


    }




    return measurements