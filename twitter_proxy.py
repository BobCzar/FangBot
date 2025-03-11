# This program is free software and licensed under the GNU Affero General Public License verson 3 (AGPL)
# The AGPL can be found in the LICENSE file within this repository
# Alternatively, the AGPL can be found here: https://www.gnu.org/licenses/agpl-3.0.en.html

import os
import requests
import logging
import random
import asyncio

from urllib.parse import urlparse, urljoin

NITTER_INSTANCES = []

def prepare_nitter_instances():
    """
    Prepares the NITTER_INSTANCES global array so that it can be used
    to substitute Twitter links.

    This function should be called only once when the bot is first started.
    """
    # Make sure to clear the list beforehand.
    NITTER_INSTANCES.clear()

    if not os.path.exists("nitter_instances.txt"):
        logger.info("nitter_instances.txt not found, twitter links will be left as is")
    else:
        with open("nitter_instances.txt") as file:
            NITTER_INSTANCES = file.read().splitlines()
            # The nitter_instances.txt file might contain duplicate links,
            # remove them just to be safe.
            list(set(NITTER_INSTANCES))

        logger.info(f"Loaded {len(NITTER_INSTANCES)} Nitter instances")

def pick_random_nitter_instance():
    """
    Picks a random Nitter instance and returns the string url.
    """
    choice_index = random.randint(0, len(NITTER_INSTANCES) - 1)
    return NITTER_INSTANCES[choice_index]

def test_nitter_instance(url):
    """
    Sends a simple GET request to url and returns true if it's working
    or false if the request returns a status code different from 200 (OK).
    """
    try:
        response = requests.get(f"https://{url}")

        if response.status_code == 200:
            logger.info(f"{url} works, using this one")
            return True
        else:
            logger.error(f"{url} has returned status code {response.status_code}")
            return False
    except:
        logger.error(f"Could not connect to {url}")
        return False

async def convert_twitter_link(original_link):
    """
    Converts the original Twitter link into a link to a Nitter instance and
    returns it as a string.

    If the NITTER_INSTANCES list is empty then the Twitter link is cleaned up
    from all tracking parameters and then returned as a string.
    """

    if not NITTER_INSTANCES:
        original_url = urlparse(original_link)
        cleaned_link = urljoin(f"https://twitter.com", original_url.path)
        logger.info(f'Cleaned up {original_link} into {cleaned_link}')
        return cleaned_link

    # Keep trying until a working instance is found.
    nitter_instance_link = None
    while True:
        nitter_instance_link = pick_random_nitter_instance()
        link_is_valid = test_nitter_instance(nitter_instance_link)
        if link_is_valid == True:
            break
        else:
            seconds = 5
            logger.info(f'Retrying in {seconds} second(s)...')
            await asyncio.sleep(5)

    original_url = urlparse(original_link)
    new_link = urljoin(f"https://{nitter_instance_link}", original_url.path)
    logger.info(f'Converted {original_link} into {new_link}')

    return new_link
