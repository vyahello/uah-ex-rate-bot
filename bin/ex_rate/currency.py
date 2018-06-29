from abc import ABC, abstractmethod
from typing import Callable

from bin.ex_rate.rate import ToUahRate


class Currency(ABC):
    """Abstraction of a currency."""

    @abstractmethod
    def txt(self) -> str:
        pass

    @abstractmethod
    def rate(self) -> str:
        pass

    @abstractmethod
    def cc(self) -> str:
        pass

    @abstractmethod
    def exchange_date(self) -> str:
        pass


class ForeignCurrency(Currency):
    """Concrete currency."""

    def __init__(self, currency: str) -> None:

        def _currency_data(value: str) -> str:
            return ToUahRate(currency.lstrip('/')).currency_records().get(value)

        self._currency_data: Callable[[str], str] = _currency_data

    def txt(self) -> str:
        return self._currency_data('txt')

    def rate(self) -> str:
        return self._currency_data('rate')

    def cc(self) -> str:
        return self._currency_data('cc')

    def exchange_date(self) -> str:
        return self._currency_data('exchangedate')
