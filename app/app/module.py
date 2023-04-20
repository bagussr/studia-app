# fastapi dependencies
from fastapi import FastAPI, APIRouter, Request, Depends, Body, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder

# sqlalchemy dependencies
from sqlalchemy import Integer, String, Boolean, create_engine, func, DateTime, Column, Enum, ForeignKey, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy.exc import InternalError

# mongo dependencies
import motor.motor_asyncio as motor
from bson import ObjectId

# sccurity dependencies
from fastapi.security import HTTPBearer
from passlib.context import CryptContext
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException


# other dependencies
import uuid
import datetime
from enum import Enum as EnumClass, IntEnum
from pydantic import BaseModel, Field, BaseSettings, validator, PrivateAttr
from typing import Any, List, Annotated
import json
import os
from dotenv import load_dotenv

load_dotenv()
