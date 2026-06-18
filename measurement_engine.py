import cv2
import numpy as np



def calculate_measurements(
    front_image,
    side_image,
    back_image
):


    height, width, _ = front_image.shape



    # This is the measurement engine location
    # Later we replace this with AI body landmarks


    body_ratio = height / width



    if body_ratio > 1.5:

        measurements = {


            "neck": 38,

            "chest": 98,

            "waist": 82,

            "hip": 96,

            "shoulder": 45,

            "sleeve": 61,

            "bicep": 34,

            "thigh": 55,

            "calf": 38,

            "ankle": 23,


        }


    else:


        measurements = {


            "neck": 36,

            "chest": 92,

            "waist": 78,

            "hip": 90,

            "shoulder": 43,

            "sleeve": 59,

            "bicep": 32,

            "thigh": 52,

            "calf": 36,

            "ankle": 22,


        }



    return measurements