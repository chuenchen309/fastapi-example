from fastapi import APIRouter, Request, status, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime

from app.schemas.base import TemplateModel
from app.config import configs as p
from app.services.database import MongoDB
from app.utils.base import message_exists, message_not_found, get_uuid

router = APIRouter(tags=["Template"])

@router.get("", status_code=status.HTTP_200_OK)
def get_template_list(*, request: Request):
    pipeline = [
        {
            "$project": {
                "_id": 0,
            }
        },
        {
            "$addFields": {
                "created_at": {
                    "$dateToString": {
                        "format": "%Y-%m-%dT%H:%M:%SZ",
                        "date": "$created_at",
                    }
                },
                "updated_at": {
                    "$dateToString": {
                        "format": "%Y-%m-%dT%H:%M:%SZ",
                        "date": "$updated_at",
                    }
                },
            }
        },
    ]

    data = MongoDB.get_many(p.MDB_TEMPLATE, pipeline)
    content = {"data": data, "total": len(data)}

    return content


@router.post("", status_code=status.HTTP_201_CREATED)
def create_template(*, item: TemplateModel, request: Request):
    check = MongoDB.get_one(p.MDB_TEMPLATE, {"name": item.name})
    if check is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=message_exists("name", item.name),
        )

    item = item.model_dump()
    id = get_uuid()
    now = datetime.now()
    item["id"] = id
    item["created_at"] = now
    item["updated_at"] = now
    MongoDB.insert_one(p.MDB_TEMPLATE, item)

    return {"id": id}


@router.put("/{id}", status_code=status.HTTP_200_OK)
def update_template(*, id: str, item: TemplateModel, request: Request):
    check = MongoDB.get_one(p.MDB_TEMPLATE, {"id": id})
    if check is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=message_not_found("id", id),
        )
    item = item.model_dump()
    item["updated_at"] = datetime.now()
    MongoDB.update_one(p.MDB_TEMPLATE, {"id": id}, item)

    return {id: "success"}


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_template(*, id: str, request: Request):
    check = MongoDB.find_one_and_delete(p.MDB_TEMPLATE, {"id": id})
    if check is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=message_not_found("id", id),
        )
    else:
        return None
