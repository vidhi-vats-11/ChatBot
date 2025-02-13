from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from transformers import pipeline
from langgraph import LangGraph

DATABASE_URL = "sqlite:///./test.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

# Models
class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_info = Column(String)
    product_categories = Column(String)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    brand = Column(String)
    price = Column(Float)
    category = Column(String)
    description = Column(String)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    supplier = relationship("Supplier")

Base.metadata.create_all(bind=engine)

# LLM for summarization
summarizer = pipeline("summarization")

@app.post("/query")
async def query(query: str):
    # Use LangGraph to process the query
    response = LangGraph.process(query)  # Example placeholder
    # Summarize response using LLM
    summary = summarizer(response, max_length=50, min_length=25, do_sample=False)
    return {"response": summary[0]['summary_text']}