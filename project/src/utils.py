import json

def get_proxies_names(file_name) -> list:
    """
    Retrieves proxy names from a JSON file.

    Args:
        file_name (str, optional): The name of the JSON file. Defaults to "project/astro_links.json".

    Returns:
        list: A list of proxy names.
    """
    try:
        with open(file_name, "r") as f:
            data = json.load(f)
            proxies = [i for i in data]
            return proxies
    except:
      return []
