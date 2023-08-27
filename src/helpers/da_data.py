from dadata import Dadata
from typing import Dict, Union
from src.helpers.consts import DADATA_INFO_INDEX


def get_dadata_info(company_inn: str) -> Dict[str, Union[str, dict]]:
    token = "Your token"
    dadata = Dadata(token)
    dadata_info = {}
    result = dadata.find_by_id(
        "party",
        company_inn,
        branch_type="MAIN",
    )
    if len(result) == 1:
        result = result[DADATA_INFO_INDEX]
        dadata_info["name_full"] = result["data"]["name"].get("full")
        dadata_info["name"] = result["data"]["name"].get("short")
        dadata_info["fio"] = result["data"].get("fio")
        dadata_info["okato"] = result["data"].get("okato")
        dadata_info["oktmo"] = result["data"].get("oktmo")
        dadata_info["okpo"] = result["data"].get("okpo")
        dadata_info["adress"] = result["data"]["address"].get("data")
        dadata_info["status"] = result["data"]["state"].get("status")
    return dadata_info
