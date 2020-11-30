from typing import Optional

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://192.168.1.140:8080/",
    "https://sedlab-catalog.netlify.app/",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/applications/")
def read_applicationa():
    applications = [{
            "name": "EF-M",
            "href": "https://github.com/sed-group/sedlab-efm",
            "description": "Enhanced Function-Means modeller",
            "contact": "Jakob Müller",
            "href_access": "https://sedlab-efm.netlify.app/",
            "href_docs": "",
            "href_source": "https://github.com/sed-group/sedlab-efm"
        },
        {
            "name": "Morpheus",
            "href": "https://github.com/sed-group/morpheus",
            "description": "This is a graphical tool for creating morphological matrices. It can be used to quickly create a matrix with 'sub-functions' (SF) and 'sub-solutions' (SS). Once all SFs and SSs have been fed into the matrix the tool can be used to generate all possible solutions.",
            "contact": "Julian Martinsson",
            "href_access": "",
            "href_docs": "",
            "href_source": "https://github.com/sed-group/morpheus"
        },
        {
            "name": "Value",
            "href": "https://github.com/sed-group/sedlab-value",
            "description": "Value Driven Design application",
            "contact": "Iñigo Alonso Fernandez",
            "href_access": "https://sedlab-valueapp.netlify.app/",
            "href_docs": "",
            "href_source": "https://github.com/sed-group/sedlab-value"
        }
    ]
    return applications
