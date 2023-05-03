# Magpie Project backend
### Backend Stack

- FastApi 
  - 장고보다 가벼워 작은 프로젝트에 적합하며, 플라스크 보다 빠르다는 장점이 있음.
---

### Requirement

- Python over 3.10.x
- Poetry over 1.4.2

### Packages

- `poetry add SQLAlchemy mysqlclient PyMySQL 'databases[mysql]'`
- `poetry add python-multipart`
  - for form data upload 
### CORS

```
origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
```