from abc import ABC, abstractmethod
from typing import Dict
from bin.web_api.requests import Request, SafeBotRequest
from bin.web_api.responses import EmptyCurrencyResponse
from bin.web_api.urls import CommonUrl


class ExchangeRate(ABC):
    """Abstraction of a exchange rate."""

    @abstractmethod
    def currency_records(self) -> Dict[str, str]:
        pass


class EmptyRateOf(ExchangeRate):
    """Represent empty exchange rate."""

    def __init__(self, rate: ExchangeRate) -> None:
        self._rate: ExchangeRate = rate

    def currency_records(self) -> Dict[str, str]:
        try:
            return self._rate.currency_records()
        except IndexError:
            pass


class ToUahRate(ExchangeRate):
    """To `uah` exchange rate."""

    def __init__(self, currency: str) -> None:
        self._req: Request = SafeBotRequest(
            CommonUrl(
                "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=",
                currency,
                "&json",
            )
        )

    def currency_records(self) -> Dict[str, str]:
        return EmptyCurrencyResponse(self._req.get()).json()
