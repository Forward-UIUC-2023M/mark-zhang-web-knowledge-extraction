import logging
import asyncio
from simple_adaptor import SimpleAdaptor
from list_answer_adaptor import ListAnswerAdaptor
from web_search_adaptor import GoogleSearchAdaptor
from framework import Engine, PageSourceStrategy, SearchSourceStrategy


for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(
    handlers=[
        logging.FileHandler("output.log"),
        logging.StreamHandler()
    ], 
    level=logging.INFO)


class DownloadedPageSourceStrategy(PageSourceStrategy):
    """Source strategy for downloaded pages.
    
    Args:
    - path: path to the downloaded page.
    - has_url: whether the downloaded page has a url in the first line."""
    @staticmethod
    def load(path, has_url=False):
        """Load a downloaded page from a file."""
        url = ""
        with open(path, 'r', encoding='utf-8') as f:
            if has_url:
                url = f.readline() # first line is url
            content = f.read()
        return DownloadedPageSourceStrategy(url, content)


engine = Engine(
    [
        GoogleSearchAdaptor(),
        ListAnswerAdaptor(),
    ], 
    backup_adaptor=SimpleAdaptor()
    )

# QUESTION = """Who are the professors with the exact title "teaching assistant professor?"""
QUESTION = """What does Professor Kevin Chang at UIUC specialize in?"""


async def main():
    logging.info("Start")
    answer = await engine.run(
        QUESTION,
        # DownloadedPageSourceStrategy.load('data/html/cs_faculty.html')
        SearchSourceStrategy(),
        )
    print(answer)
    logging.info("Finished")


if __name__ == '__main__':
    asyncio.run(main())
