# generated by datamodel-codegen:
#   filename:  DatLogMessage.yml
#   timestamp: 2024-04-03T10:02:34+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Level(Enum):
    FATAL = 'FATAL'
    ERROR = 'ERROR'
    WARN = 'WARN'
    INFO = 'INFO'
    DEBUG = 'DEBUG'
    TRACE = 'TRACE'


class DatLogMessage(BaseModel):
    class Config:
        extra = 'allow'

    level: Level = Field(..., description='log level of the log message')
    message: str = Field(..., description='log message')
    stack_trace: Optional[str] = Field(
        None,
        description='an optional stack trace if the log message corresponds to an exception',
    )
