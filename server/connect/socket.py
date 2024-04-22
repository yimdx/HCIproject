# This is for server-client connection

from fastapi import FastAPI, File, UploadFile, WebSocket
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/upload/")
async def upload_audio(file: UploadFile = File(...)):
    try:
        with open(f"{file.filename}", "wb") as audio:
            audio.write(await file.read())
        return JSONResponse(status_code=200, content={"message": "File uploaded successfully"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})


@app.websocket("/real_time_streaming/")
async def real_time_streaming(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_bytes()
            print("Received audio data")
            await websocket.send_text("Data received")
    except Exception as e:
        await websocket.close()
        print(f"Connection closed: {e}")
