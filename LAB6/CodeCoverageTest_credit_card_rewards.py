
import pytest
from credit_card_rewards import reward_points, late_payment_fee, card_status


# Reward Points Tests

def test_classic_grocery():
    assert reward_points("classic", 1000, "grocery", False) == 10

def test_gold_grocery():
    assert reward_points("gold", 1000, "grocery", False) == 20

def test_platinum_grocery():
    assert reward_points("platinum", 1000, "grocery", False) == 40

def test_unknown_card():
    with pytest.raises(ValueError):
        reward_points("diamond", 1000, "grocery", False)

def test_invalid_amount():
    with pytest.raises(ValueError):
        reward_points("classic", 0, "grocery", False)

def test_fuel_category():
    assert reward_points("gold", 1000, "fuel", False) == 0

def test_dining_category():
    assert reward_points("gold", 1000, "dining", False) == 40

def test_travel_category():
    assert reward_points("platinum", 1000, "travel", False) == 80

def test_weekend_bonus():
    assert reward_points("gold", 1000, "grocery", True) == 70

def test_classic_weekend():
    assert reward_points("classic", 1000, "grocery", True) == 10


# Late Payment Fee Tests

def test_no_late_payment():
    assert late_payment_fee(5000, 0) == 0

def test_negative_outstanding():
    assert late_payment_fee(-500, 5) == 0

def test_fee_below_1000():
    assert late_payment_fee(500, 5) == 100

def test_fee_at_1000():
    assert late_payment_fee(1000, 5) == 100

def test_fee_below_10000():
    assert late_payment_fee(5000, 5) == 500

def test_fee_above_10000():
    assert late_payment_fee(15000, 5) == 1000

def test_late_more_than_30_days():
    assert late_payment_fee(15000, 31) == 1750


# Card Status Tests

def test_frozen_card():
    assert card_status(50, 0, True) == "frozen"

def test_blocked_card():
    assert card_status(50, 3, False) == "blocked"

def test_over_limit_risk():
    assert card_status(95, 0, False) == "over limit risk"

def test_watch_high_utilisation():
    assert card_status(50, 0, False) == "watch"

def test_watch_missed_payment():
    assert card_status(20, 1, False) == "watch"

def test_good_card():
    assert card_status(20, 0, False) == "good"
