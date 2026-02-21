import re
from urllib.parse import urlparse

SUSPICIOUS_KEYWORDS = [
    "login", "verify", "update", "secure", "account",
    "banking", "confirm", "password", "paypal", "security"
]

def extract_features(url: str):
    """
    Extract simple numeric features from a URL.
    Returns a list of feature values in a fixed order.
    """
    parsed = urlparse(url)

    url_length = len(url)
    hostname = parsed.hostname or ""
    path = parsed.path or ""
    query = parsed.query or ""

    num_dots = url.count(".")
    num_hyphens = url.count("-")
    num_subdirs = path.count("/")
    num_query_params = query.count("&") + (1 if query else 0)
    has_at_symbol = 1 if "@" in url else 0
    has_ip_address = 1 if re.search(r"\b\d{1,3}(\.\d{1,3}){3}\b", hostname) else 0
    uses_https = 1 if parsed.scheme == "https" else 0

    keyword_count = sum(1 for kw in SUSPICIOUS_KEYWORDS if kw in url.lower())

    return [
        url_length,
        num_dots,
        num_hyphens,
        num_subdirs,
        num_query_params,
        has_at_symbol,
        has_ip_address,
        uses_https,
        keyword_count,
    ]

def get_feature_names():
    return [
        "url_length",
        "num_dots",
        "num_hyphens",
        "num_subdirs",
        "num_query_params",
        "has_at_symbol",
        "has_ip_address",
        "uses_https",
        "keyword_count",
    ]
