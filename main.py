# =====================================================
# TENDER TRACKER API
# Микросервис для управления тендерами
# =====================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

# Создаём экземпляр приложения FastAPI
app = FastAPI(title="Tender Tracker API")

# Модели данных
class Tender(BaseModel):
    id: str
    title: str
    description: str
    status: str  # draft, active, won, lost

class TenderCreate(BaseModel):
    title: str
    description: str
    status: str = "draft"

# In-memory хранилище (для простоты)
tenders_db = {}

# Корневой эндпоинт
@app.get("/")
def read_root():
    return {"message": "Tender Tracker API is running"}

# Создание тендера
@app.post("/tenders/", response_model=Tender)
def create_tender(tender: TenderCreate):
    tender_id = str(uuid.uuid4())
    new_tender = Tender(
        id=tender_id,
        title=tender.title,
        description=tender.description,
        status=tender.status
    )
    tenders_db[tender_id] = new_tender
    return new_tender

# Получение всех тендеров
@app.get("/tenders/", response_model=List[Tender])
def list_tenders():
    return list(tenders_db.values())

# Получение тендера по ID
@app.get("/tenders/{tender_id}", response_model=Tender)
def get_tender(tender_id: str):
    if tender_id not in tenders_db:
        raise HTTPException(status_code=404, detail="Tender not found")
    return tenders_db[tender_id]

# Обновление тендера
@app.put("/tenders/{tender_id}", response_model=Tender)
def update_tender(tender_id: str, tender: TenderCreate):
    if tender_id not in tenders_db:
        raise HTTPException(status_code=404, detail="Tender not found")
    updated_tender = Tender(
        id=tender_id,
        title=tender.title,
        description=tender.description,
        status=tender.status
    )
    tenders_db[tender_id] = updated_tender
    return updated_tender

# Удаление тендера
@app.delete("/tenders/{tender_id}")
def delete_tender(tender_id: str):
    if tender_id not in tenders_db:
        raise HTTPException(status_code=404, detail="Tender not found")
    del tenders_db[tender_id]
    return {"message": "Tender deleted"}