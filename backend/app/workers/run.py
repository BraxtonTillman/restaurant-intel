"""
Worker entrypoint.

Run inside docker:
    python -m app.workers.run
"""

from __future__ import annotations

import os
import time


def main() -> None:
    # Optional "kill switch" via env var
    enabled = os.getenv("WORKER_ENABLED", "true").lower() in {
        "1", "true", "yes", "y"}
    if not enabled:
        print("Worker disabled (WORKER_ENABLED=false). Exiting.")
        return

    print("Worker starting...")

    # TODO: replace this with real work (ingestion, metrics, scheduled tasks)
    while True:
        print("Worker tick...")
        time.sleep(10)


if __name__ == "__main__":
    main()
