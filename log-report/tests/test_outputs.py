import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def _load_report():
    return json.loads(REPORT_PATH.read_text())


def test_report_is_valid_json_object():
    """Criterion 1: /app/report.json exists and is a single valid JSON object."""
    assert REPORT_PATH.exists(), "no /app/report.json found"
    report = _load_report()
    assert isinstance(report, dict), "report.json must contain a JSON object"


def test_total_requests():
    """Criterion 2: total_requests equals the number of request lines in the log."""
    report = _load_report()
    assert report["total_requests"] == 6


def test_unique_ips():
    """Criterion 3: unique_ips equals the number of distinct client IPs in the log."""
    report = _load_report()
    assert report["unique_ips"] == 3


def test_top_path():
    """Criterion 4: top_path is the most frequently requested path in the log."""
    report = _load_report()
    assert report["top_path"] == "/index.html"