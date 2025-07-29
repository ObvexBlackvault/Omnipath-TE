import pytest
from backend.core import ForkAlpha, ForkBeta

def test_forkalpha_status():
    status = ForkAlpha.status()
    assert isinstance(status, dict)
    assert "state" in status

def test_forkbeta_status():
    status = ForkBeta.status()
    assert isinstance(status, dict)
    assert "state" in status
