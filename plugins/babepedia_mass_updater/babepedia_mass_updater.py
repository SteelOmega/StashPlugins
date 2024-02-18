import config, json, requests, sys
from bs4 import BeautifulSoup

from custom_classes import *

try:
    import stashapi.log as log

    log.LEVEL = config.log_level
    from stashapi.stashapp import StashInterface
    from stashapi.stash_types import OnMultipleMatch
except ModuleNotFoundError:
    print(
        "You need to install stashapp-tools. (https://pypi.org/project/stashapp-tools/)",
        file=sys.stderr,
    )
    print(
        "If you have pip (normally installed with python), run this command in a terminal (cmd): 'pip install stashapp-tools'",
        file=sys.stderr,
    )
    sys.exit()

url = "https://www.babepedia.com/"


def main(stash_in=None, mode_in=None):
    global stash

    if stash_in:
        stash = stash_in
        mode = mode_in
    else:
        fragment = json.loads(sys.stdin.read())
        stash = StashInterface(fragment["server_connection"])
        mode = fragment["args"]["mode"]

    if mode == "run_calculator":
        run_updater()


def run_updater():
    performers = stash.find_performers(fragment=PERFORMER_FRAGMENT)

    log.info("Parsing performers")
    for p in performers:
        if p.get("gender") != 'FEMALE':
            continue

        p_id = f"{p['name']} ({p['id']})"
        try:
            p = StashPerformer(p)
        except DebugException as e:
            log.debug(f"{p_id:>30}: {e}")
        except WarningException as e:
            log.warning(f"{p_id:>30}: {e}")
        except Exception as e:
            log.error(f"{p_id:>30}: {e}")

if __name__ == "__main__":
    main()
