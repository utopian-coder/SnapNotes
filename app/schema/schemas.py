def noteEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "description": item["description"]
    }

def notesEntity(entity) -> list:
    return [noteEntity(item) for item in entity]