# generated by datamodel-codegen:
#   filename:  DatDocumentStream.yml
#   timestamp: 2024-04-02T08:32:13+00:00

from __future__ import annotations

from typing import Any, Dict, Optional

from pydantic import BaseModel, Field
from dat_core.pydantic_models.base import EnumWithStr


class ReadSyncMode(EnumWithStr):
    FULL_REFRESH = 'FULL_REFRESH'
    INCREMENTAL = 'INCREMENTAL'


class WriteSyncMode(EnumWithStr):
    APPEND = 'APPEND'
    UPSERT = 'UPSERT'
    REPLACE = 'REPLACE'


class DatDocumentStream(BaseModel):
    class Config:
        extra = 'allow'
    
    name: str = Field(..., description='The name of the document stream.')
    namespace: Optional[str] = Field(
        None, description='The namespace the data is associated with.'
    )
    json_schema: Optional[Dict[str, Any]] = Field(
        None, description='The JSON schema for the document stream.'
    )
    read_sync_mode: Optional[ReadSyncMode] = Field(
        'INCREMENTAL',
        description='A list of supported sync modes for the stream while reading.',
    )
    write_sync_mode: Optional[WriteSyncMode] = Field(
        'APPEND',
        description='A list of supported sync modes for the stream while writing.',
    )
    cursor_field: Optional[str] = Field(
        None,
        description='The path to the field used to determine if a record is new or modified.\nREQUIRED for INCREMENTAL sync mode.',
    )
