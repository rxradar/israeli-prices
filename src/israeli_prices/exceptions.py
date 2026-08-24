"""Exceptions raised by israeli-prices."""


class IsraeliPricesError(Exception):
    """Base class for all israeli-prices errors."""


class ChainNotFound(IsraeliPricesError):
    """Unknown chain slug, or no adapter implemented for it yet."""


class PortalError(IsraeliPricesError):
    """A chain portal could not be reached or answered unexpectedly."""


class FileNotFound(IsraeliPricesError):
    """No file on the portal matches the requested type/store."""


class ParseError(IsraeliPricesError):
    """The downloaded payload could not be parsed as a transparency file."""
