from app.main import create_app
import uvicorn

if __name__ == '__main__':

    uvicorn.run(
        create_app(),
        host="0.0.0.0",
        port=5000,
        workers=1,
        log_level="debug",
        timeout_keep_alive=36
    )