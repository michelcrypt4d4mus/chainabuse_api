"""
Reports requests
"""
from dataclasses import asdict, dataclass
from typing import Any, Dict, List, Optional, Union

from inflection import camelize
from pendulum import DateTime

ASC = 'ASC'
DESC = 'DESC'


@dataclass(kw_only=True)
class ReportsRequest:
    trusted: Optional[bool] = None
    checked: Optional[bool] = None
    address: Optional[str] = None
    domain: Optional[str] = None
    chain: Optional[str] = None
    category: Optional[str] = None
    order_by_direction: str = ASC
    order_by_field: str = 'CREATED_AT'
    before: Optional[DateTime] = None
    since: Optional[DateTime] = None
    page: int = 1
    per_page: int = 50
    min_loss_amount: Optional[float] = None
    scammerloc: Optional[float] = None
    username: Optional[float] = None

    def to_params(self) -> Dict[Any, Any]:
        return {camelize(k, False): v for k,v in asdict(self).items() if v is not None}
