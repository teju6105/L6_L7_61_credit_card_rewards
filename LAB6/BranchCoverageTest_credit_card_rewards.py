import pytest
from credit_card_rewards import reward_points, late_payment_fee, card_status


# Reward Points - Branch Tests

def test_invalid_card():
    with pytest.raises(ValueError):
        reward_points("diamond", 1000, "grocery", False)

def test_invalid_amount():
    with pytest.raises(ValueError):
        reward_points("classic", 0, "grocery", False)

def test_valid_amount():
    assert reward_points("classic", 1000, "grocery", False) == 10

def test_fuel():
    assert reward_points("gold", 1000, "fuel", False) == 0

def test_grocery():
    assert reward_points("gold", 1000, "grocery", False) == 20

def test_dining():
    assert reward_points("gold", 1000, "dining", False) == 40

def test_travel():
    assert reward_points("platinum", 1000, "travel", False) == 80

def test_weekend_non_classic():
    assert reward_points("gold", 1000, "grocery", True) == 70

def test_weekend_classic():
    assert reward_points("classic", 1000, "grocery", True) == 10


# Late Payment Fee - Branch Tests

def test_days_late_zero():
    assert late_payment_fee(5000, 0) == 0

def test_outstanding_zero():
    assert late_payment_fee(0, 5) == 0

def test_outstanding_below_1000():
    assert late_payment_fee(500, 5) == 100

def test_outstanding_equal_1000():
    assert late_payment_fee(1000, 5) == 100

def test_outstanding_between_1000_and_10000():
    assert late_payment_fee(5000, 5) == 500

def test_outstanding_equal_10000():
    assert late_payment_fee(10000, 5) == 500

def test_outstanding_above_10000():
    assert late_payment_fee(15000, 5) == 1000

def test_more_than_30_days_late():
    assert late_payment_fee(15000, 31) == 1750


# Card Status - Branch Tests

def test_frozen():
    assert card_status(95, 3, True) == "frozen"

def test_blocked():
    assert card_status(50, 3, False) == "blocked"

def test_not_blocked():
    assert card_status(50, 0, False) == "watch"

def test_over_limit():
    assert card_status(95, 0, False) == "over limit risk"

def test_watch_utilisation():
    assert card_status(50, 0, False) == "watch"

def test_watch_missed_payment():
    assert card_status(20, 1, False) == "watch"

def test_good_status():
    assert card_status(20, 0, False) == "good"