from fastapi import FastAPI
from .database import engine
from fastapi.middleware.cors import CORSMiddleware

from .routers import users, category, paymentMethod, paymentNetwork, paymentAddress, pending_payment,uploadStore,store,cardInfo, buy
from .routers.products import instagram
from .models import user, payment_method, payment_address, payment_network, deposit, withdraw,transaction
from fastapi.staticfiles import StaticFiles



app = FastAPI()
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# create all tables
user.Base.metadata.create_all(bind=engine)

# allow_origins=[
#     "http://localhost:5173",
#     "http://127.0.0.1:5173"
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(category.router)
app.include_router(paymentMethod.router)
app.include_router(paymentNetwork.router)
app.include_router(paymentAddress.router)
app.include_router(pending_payment.router)
app.include_router(uploadStore.router)
app.include_router(store.router)
app.include_router(instagram.router)
app.include_router(cardInfo.router)
app.include_router(buy.router)





# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database="postgres", user="postgres", password="1234", cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Successfully connect Database")
#         break
#     except Exception as error:
#         print("Database connection failed")
#         print("Error:" , error)
#         time.sleep(3)

# @app.get("/")
# def read_root():
#     cursor.execute(""" SELECT * from accounts """)
#     data = cursor.fetchall()
#     return{"Data": data}




# @app.get("/accountsalchemy")
# def account(db: Session = Depends(get_db)):
#     return {"status": "sqlalchemy orm working"}
