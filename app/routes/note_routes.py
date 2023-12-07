from fastapi import APIRouter, Depends, HTTPException
from ..models.note_model import NoteModel
from ..config.db import mongo_client
from ..schema.schemas import notesEntity, noteEntity
from bson import ObjectId
router = APIRouter()

db = mongo_client.notes
notes_collection = db.notes

@router.get('/')
async def get_all_notes():
    notes = notesEntity(notes_collection.find())
    return {"status": "success", "notes": notes}

@router.get('/{note_id}')
async def get_one_note(note_id):
    note = noteEntity(notes_collection.find_one({"_id": ObjectId(note_id)}))
    return {'status': 'success', 'note': note}

@router.post('/')
async def create_note(request: NoteModel):
    notes_collection.insert_one(request.model_dump())
    return {'status': 'success', "note": 'Note created successfully'}

@router.put('/{note_id}') 
async def update_note(note_id, request: NoteModel):
    notes_collection.update_one({"_id": ObjectId(note_id)}, {"$set": request.model_dump()})
    return {'status': 'success', 'note': 'Note updated successfully'}

@router.delete('/{note_id}')
async def delete_note(note_id):
    notes_collection.find_one_and_delete({"_id": ObjectId(note_id)})
    return {'status': 'success', 'note': 'Note deleted successfully'}