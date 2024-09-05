from fastapi import APIRouter
from controllers.objectController import (
    fetch_objects,
    fetch_object,
    create_object,
    update_object,
    delete_object,
    delete_objects,
)

router = APIRouter()

router.add_api_route("/", methods=["GET"], endpoint=fetch_objects)

router.add_api_route("/{id}", methods=["GET"], endpoint=fetch_object)

router.add_api_route("/", methods=["POST"], endpoint=create_object)

router.add_api_route("/{id}", methods=["PUT"], endpoint=update_object)

router.add_api_route("/{id}", methods=["DELETE"], endpoint=delete_object)

router.add_api_route("/", methods=["DELETE"], endpoint=delete_objects)
