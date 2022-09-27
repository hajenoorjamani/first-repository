from fastapi import FastAPI

app = FastAPI()
mahasiswa = [{ "NIM" : 18220085, "Nama": "Haje Noorjamani" },
{"NIM" : 18220027, "Nama": "Andreana Hartadi Suliman"},
{"NIM" : 18220105, "Nama": "Made Adi Surya Pramana"},
{"NIM" : 18220059, "Nama": "Faiza Aqiela Zuma"},
{"NIM" : 18220005, "Nama": "Muhammad Rifqi Riansyah M"},
{"NIM" : 1822071, "Nama": "Muhammad Zaky"},
{"NIM" : 1822073, "Nama": "Umar Hakim"},]
@app.get("/")
async def hello() -> dict:
    return mahasiswa