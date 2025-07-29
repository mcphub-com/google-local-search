import os, requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP('serp-local')


serp_url = "https://serpapi.com/search"
serp_api_key = os.getenv("SERP_API_KEY")

@mcp.tool()
def search_local(q: Annotated[str, Field(description='Parameter defines the query you want to search. You can use anything that you would use in a regular Google Local search.')],
                location: Annotated[Union[str, None], Field(description="Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to the /locations.json API if you need more precise control. The location and uule parameters can't be used together. It is recommended to specify location at the city level in order to simulate a real user’s search. If location is omitted, the search may take on the location of the proxy.")] = None,
                start: Annotated[Union[int, None], Field(description="Parameter defines the result offset. It skips the given number of results. It's used for pagination. On desktop, parameter only accepts multiples of 20 (e.g. 20 for the second page results, 40 for the third page results, etc.). On mobile, parameter only accepts multiples of 10 (e.g. 10 for the second page results, 20 for the third page results, etc.).")] = None,
                device: Annotated[Union[str, None], Field(description="Parameter defines the device to use to get the results. It can be set to desktop (default) to use a regular browser, tablet to use a tablet browser (currently using iPads), or mobile to use a mobile browser.")] = None,
                no_cache: Annotated[Union[bool, None], Field(description="Parameter will force SerpApi to fetch the Google Jobs results even if a cached version is already present. A cache is served only if the query and all parameters are exactly the same. Cache expires after 1h. Cached searches are free, and are not counted towards your searches per month. It can be set to false (default) to allow results from the cache, or true to disallow results from the cache. no_cache and async parameters should not be used together.")] = None,
                aasync: Annotated[Union[bool, None], Field(description="Parameter defines the way you want to submit your search to SerpApi. It can be set to false (default) to open an HTTP connection and keep it open until you got your search results, or true to just submit your search to SerpApi and retrieve them later. In this case, you'll need to use our Searches Archive API to retrieve your results. async and no_cache parameters should not be used together. async should not be used on accounts with Ludicrous Speed enabled.")] = None
            ):
    '''This tool allows you to scrape results from the Google Local page.'''

    if location:
        q = q + ", location: %s"%location

    payload = {
        'q': q,
        'engine': "google_local",
        'api_key': serp_api_key,
        "start": start,
        "device": device,
        "no_cache": no_cache,
        "async": aasync
    }
    payload = {k: v for k, v in payload.items() if v is not None}

    response = requests.get(serp_url, params=payload)
    print(response)
    return response.json()

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")