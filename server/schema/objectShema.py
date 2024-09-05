def individual_object(object) -> dict:
    return {
        "id": str(object["_id"]),
        "field_one": str(object["field_one"]),
        "field_two": object["field_two"],
        "created_at": str(object["created_at"]),
        "updated_at": str(object["updated_at"]),
    }


def list_objects(objects) -> list:
    return [individual_object(object) for object in objects]
