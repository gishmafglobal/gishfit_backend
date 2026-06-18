from fastapi import FastAPI, UploadFile, File

import cv2
import numpy as np


from measurement_engine import calculate_measurements



app = FastAPI()



@app.get("/")
def home():

    return {

        "status":
        "GishFit AI Measurement API running"

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

        np.frombuffer(
            front_bytes,
            np.uint8
        ),

        cv2.IMREAD_COLOR

    )



    side_image = cv2.imdecode(

        np.frombuffer(
            side_bytes,
            np.uint8
        ),

        cv2.IMREAD_COLOR

    )



    back_image = cv2.imdecode(

        np.frombuffer(
            back_bytes,
            np.uint8
        ),

        cv2.IMREAD_COLOR

    )





    if (

        front_image is None

        or side_image is None

        or back_image is None

    ):


        return {

            "error":
            "Invalid images"

        }




    measurements = calculate_measurements(

        front_image,

        side_image,

        back_image

    )





    return measurements