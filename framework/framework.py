"""Framework for building a web knowledge retrieval system."""

from abc import ABC
import logging

__all__ = [
    'Adaptor',
    'SourceStrategy',
    'PageSourceStrategy',
    'SearchSourceStrategy',
    'Engine'
]

class Adaptor(ABC):
    """Adapator is the abstract class for all task adaptors."""
    def __init__(self):
        pass

    async def is_suitable(self, question, source_strategy) -> bool:
        """Check if the adaptor is suitable for the given question and source strategy."""

    async def run(self, question, source_strategy) -> str:
        """Run the task."""


class SourceStrategy(ABC):
    """Base class for source strategies."""


class PageSourceStrategy(SourceStrategy):
    """Single web page source strategy."""
    def __init__(self, url, content):
        self.url = url
        self.content = content

class SearchSourceStrategy(SourceStrategy):
    """Search result source strategy."""


class Engine:
    """Web knowledge retrieval engine."""

    def __init__(self, adaptors, backup_adaptor):
        self.adaptors = adaptors
        self.backup_adaptor = backup_adaptor

    async def run(self, question, source_strategy):
        """Run the engine."""
        for adaptor in self.adaptors:
            logging.info("Trying %s", adaptor.__class__.__name__)
            if await adaptor.is_suitable(question, source_strategy):
                logging.info("Using %s", adaptor.__class__.__name__)
                answer = await adaptor.run(question, source_strategy)
                if answer is not None:
                    break
                logging.info("Adaptor %s failed", adaptor.__class__.__name__)
        if answer is None:
            logging.info("Using backup adaptor %s", self.backup_adaptor.__class__.__name__)
            answer = await self.backup_adaptor.run(question, source_strategy)
        return answer
