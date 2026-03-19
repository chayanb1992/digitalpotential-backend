from fastapi import APIRouter, UploadFile, File
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "uploads/store_logo"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def get_unique_filename(filename: str):
    name, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(UPLOAD_DIR, new_filename)):
        new_filename = f"{name}-{counter}{ext}"
        counter += 1

    return new_filename


@router.post("/stores-images/")
async def create_store(logo: UploadFile = File(...)):

    filename = get_unique_filename(logo.filename)
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(logo.file, buffer)

    return {
        "message": "Store created",
        "logo_url": f"https://web-production-33681.up.railway.app/uploads/store_logo/{filename}"
    }