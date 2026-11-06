def format_price(value):
    """Format a number as $1,234.56."""
    return f"${value:,.2f}"


def parse_config(text):
    """Return {} for empty input instead of crashing."""
    if not text:
        return {}
    return {"raw": text}
