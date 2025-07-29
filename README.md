# Aigeon AI Google Local Search

## Project Description

Aigeon AI Google Local Search is a Python-based server application that facilitates scraping results from Google Local Search. It leverages the SerpAPI to perform local search queries, allowing users to simulate searches as if conducted by a real user from a specified location. This tool is particularly useful for businesses and developers who need to gather localized search data for analysis or integration into their applications.

## Features Overview

- **Local Search Simulation**: Perform searches as if originating from a specific location, simulating real user behavior.
- **Flexible Query Parameters**: Customize searches with various parameters such as location, language, device type, and more.
- **Pagination Support**: Retrieve search results across multiple pages.
- **Cache Management**: Control caching behavior to ensure fresh data retrieval.
- **Asynchronous Search**: Option to submit searches asynchronously for later retrieval.

## Main Features and Functionality

### Local Search Tool

The core functionality of this application is encapsulated in the `search_local` function, which allows users to perform detailed and customizable local searches on Google. The function is designed to accommodate a wide range of parameters, providing flexibility in how searches are conducted.

### Customizable Search Parameters

- **Query (`q`)**: The main search term or query string.
- **Location (`location`)**: Specifies the geographical location from which the search should be simulated.
- **Encoded Location (`uule`)**: An alternative to `location`, using Google's encoded location format.
- **Google Domain (`google_domain`)**: The specific Google domain to use for the search (e.g., google.com).
- **Country Code (`gl`)**: Two-letter code representing the country for the search.
- **Language Code (`hl`)**: Two-letter code representing the language for the search.
- **Result Offset (`start`)**: Used for pagination to skip a certain number of results.
- **Device Type (`device`)**: Specifies the device type (desktop, tablet, mobile) for the search.
- **Cache Control (`no_cache`)**: Determines whether to use cached results or fetch new data.
- **Asynchronous Search (`aasync`)**: Allows the search to be submitted asynchronously, retrieving results later.

## Main Functions Description

### `search_local`

This function is the primary tool for executing local search queries. It constructs a payload with the specified parameters and sends a request to the SerpAPI endpoint. The function returns the search results in JSON format, allowing for easy integration and processing.

**Parameters:**

- **`q`**: The search query string.
- **`location`**: Optional. The location from which the search is simulated.
- **`uule`**: Optional. Google encoded location for the search.
- **`google_domain`**: Optional. The Google domain to use.
- **`gl`**: Optional. Country code for the search.
- **`hl`**: Optional. Language code for the search.
- **`start`**: Optional. Result offset for pagination.
- **`device`**: Optional. Device type for the search.
- **`no_cache`**: Optional. Boolean to control cache usage.
- **`aasync`**: Optional. Boolean for asynchronous search submission.

This function is designed to be flexible and powerful, providing users with the ability to tailor their search queries to meet specific needs and requirements.