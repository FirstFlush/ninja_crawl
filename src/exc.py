
class NinjaCrawlError(Exception):
    """Base exception for the Ninja Crawl app"""
    pass


class ScrapingServiceError(NinjaCrawlError):
    """Raised when the ScrapingService fails for any reason"""
    pass


class TransformerError(NinjaCrawlError):
    """Raised when a Spider class fails for any reason"""
    pass


class TransformerRegistryError(NinjaCrawlError):
    """Raised when the SpiderRegistry fails to find and instantiate the requested spider."""
    pass