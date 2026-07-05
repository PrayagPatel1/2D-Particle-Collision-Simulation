import pytest
from src.ca_engine import *

def test_correct_init() -> None:
    engine_param = (50, [Cell(), Cell()], RULE_30) 