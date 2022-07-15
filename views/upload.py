from fastapi import APIRouter, File, UploadFile

upload_router = APIRouter()


@upload_router.post("")
async def upload_file(file: UploadFile = File(..., media_type="*")) :
    res = await file.read()
    with open("upload/" + file.filename, 'wb+') as f:
        f.write(res)
    return {"file_info": file.filename, "content_type": file.content_type, "status": "文件上传成功"}
