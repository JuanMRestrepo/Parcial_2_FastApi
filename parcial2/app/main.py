from fastapi import FastAPI
from app.routes import pay_routes, tenant_routes
from app.config.config import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(pay_routes.router, prefix="/api", tags=["pago"])
app.include_router(tenant_routes.router,prefix="/api", tags=["arrendatario"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8084)