$env:DATABASE_HOST = "localhost";
$env:DATABASE_USER = "root";
$env:DATABASE_PASSWORD = "";
$env:DATABASE_PORT = "3306";
$env:DATABASE_NAME = "ctf-cm";

# Run server
# uvicorn Api:app --reload
uvicorn main:app --reload