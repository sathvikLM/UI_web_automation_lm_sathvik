import logging
import os
from datetime import datetime
from pathlib import Path

class LogGen:
    """
    Returns a module‑level logger that writes to
    Logs/run_<YYYY‑MM‑DD_HH‑MM‑SS>.log
    """
    @staticmethod
    def loggen() -> logging.Logger:
        # ── make sure Logs/ exists ───────────────────────────────────────────
        log_dir = Path("Logs")
        log_dir.mkdir(exist_ok=True)

        # one file per test‑run
        log_file = log_dir / f"run_{datetime.now():%Y-%m-%d_%H-%M-%S}.log"

        # configure root logger only once
        if not logging.getLogger().handlers:
            fmt = "%(asctime)s  [%(levelname)s]  %(name)s: %(message)s"
            logging.basicConfig(
                level=logging.INFO,
                format=fmt,
                handlers=[
                    logging.FileHandler(log_file, encoding="utf‑8"),
                    logging.StreamHandler()                 # still prints to console
                ],
            )

        return logging.getLogger(__name__)
