import asyncio
from core import run

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run())
    except KeyboardInterrupt:
        pass