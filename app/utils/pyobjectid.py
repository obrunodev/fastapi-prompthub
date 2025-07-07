# app/utils/pyobjectid.py
from typing import Any
from bson.objectid import ObjectId
from pydantic import GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema


class PyObjectId(ObjectId):
    """MongoDB ObjectId compatível com Pydantic v2"""

    @classmethod
    def __get_pydantic_core_schema__(  # <-- NOVO em v2
        cls,
        _source_type: Any,
        _handler: Any,
    ) -> core_schema.CoreSchema:
        # validador: aceita ObjectId ou string‑hex válida
        def _validate(value: Any) -> ObjectId:
            if isinstance(value, ObjectId):
                return value
            if not ObjectId.is_valid(value):
                raise ValueError("Invalid ObjectId")
            return ObjectId(value)

        #      python (entrada)           →   json (saída)
        return core_schema.no_info_plain_validator_function(
            _validate,
            serialization=core_schema.to_string_ser_schema(),  # sempre vira str no JSON
        )

    @classmethod
    def __get_pydantic_json_schema__(   # <-- mantém o OpenAPI feliz
        cls,
        _core_schema: core_schema.CoreSchema,
        handler: GetJsonSchemaHandler,
    ) -> JsonSchemaValue:
        # Diz ao FastAPI: “no JSON, eu apareço como string”
        return handler(core_schema.str_schema())
