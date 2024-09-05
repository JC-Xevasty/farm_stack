from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from pymongo import ReturnDocument
from pymongo.results import InsertOneResult
from bson import ObjectId
from datetime import datetime

from config.database import object_collection
from models.object import CreateObjectRequest, UpdateObjectRequest
from schema.objectShema import list_objects, individual_object

"""
@desc     Fetch all objects
route     GET api/objects
@access   Private
"""


async def fetch_objects():
    data = object_collection.find({})

    objects = list_objects(data)

    return JSONResponse(status_code=status.HTTP_200_OK, content=objects)


"""
@desc     Fetch a single object
route     GET api/objects/{id}
@access   Private
"""


async def fetch_object(id: str):

    # Check if id is valid ObjectId
    if not ObjectId.is_valid(id) or not ObjectId.is_valid(id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Error fetching object."
        )

    data = object_collection.find_one({"_id": ObjectId(id)})

    object = individual_object(data)

    return JSONResponse(status_code=status.HTTP_200_OK, content=object)


"""
@desc     Update a single object
route     PUT api/objects/{id}
@access   Private
"""


async def create_object(data: CreateObjectRequest):
    to_encode = dict(data).copy()

    to_encode.update({"updated_at": data.created_at})

    created_object: InsertOneResult = object_collection.insert_one(dict(to_encode))

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "Object created successfully",
            "created_object_id": str(created_object.inserted_id),
        },
    )


"""
@desc     Update a single object
route     PUT api/objects/
@access   Private
"""


async def update_object(id: str, data: UpdateObjectRequest):
    # Check if id is valid ObjectId
    if not ObjectId.is_valid(id) or not ObjectId.is_valid(id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Error updating object."
        )

    to_encode = dict(data).copy()

    to_encode = {k: v for k, v in to_encode.items() if v is not None}
    
    to_encode.update({"updated_at": datetime.now()})

    data = object_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(to_encode)},
        return_document=ReturnDocument.AFTER,
    )

    updated_object = individual_object(data)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "Object updated successfully.",
            "updated_object": updated_object,
        },
    )


"""
@desc     Delete a single object
route     DELETE api/objects/{id}
@access   Private
"""


async def delete_object(id: str):
    # Check if id is valid ObjectId
    if not ObjectId.is_valid(id) or not ObjectId.is_valid(id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Error deleting object."
        )

    data = object_collection.find_one_and_delete({"_id": ObjectId(id)})

    deleted_object = individual_object(data)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "Object deleted successfully",
            "deleted_dataset": deleted_object,
        },
    )


"""
@desc     Delete all objects
route     DELETE api/objects/
@access   Private
"""


async def delete_objects():
    deleted_objects = object_collection.delete_many({})

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "All objects deleted successfully"},
    )
