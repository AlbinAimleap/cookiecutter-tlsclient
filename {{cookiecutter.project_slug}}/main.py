"""{{cookiecutter.project_name}}

This module serves as the main entry point for:

{{cookiecutter.project_description}}
"""

__author__ = "{{cookiecutter.author_name.title()}}"
__email__ = "{{cookiecutter.author_email.lower()}}"
__version__ = "{{cookiecutter.project_version}}"


import json
import asyncio
from tlsclient.core.base import HTTPClient
from tlsclient.core.logger import logger

from config import Config


async def main() -> None:
    """{{cookiecutter.project_description}}"""
    url = "{{cookiecutter.site_url}}"

    try:
        client = HTTPClient(async_mode=True)
        client.set_headers(Config.HEADERS)
        client.set_proxies(Config.PROXIES)
        
        response = await client.send_async_request(url)
        
        print(response.json())

    except (json.JSONDecodeError, Exception) as e:
        logger.error("An error occurred: %s", e)
        
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(main())
