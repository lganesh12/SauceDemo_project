from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TRACE_LOGS = Path.joinpath(PROJECT_ROOT, "trace.zip")
SLOW_MOTION_TIME = 1000
ELEMENT_WAIT_TIME = 5000
