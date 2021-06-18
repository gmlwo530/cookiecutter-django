from django.utils import timezone
from django.core.cache import cache


def test_redis():
    """
    Test redis set and get
    """
    now = timezone.now().timestamp()
    KEY = f"test_key_{now}"
    VAL = now
    cache.set(KEY, VAL, timeout=60)

    assert VAL == cache.get(KEY)
