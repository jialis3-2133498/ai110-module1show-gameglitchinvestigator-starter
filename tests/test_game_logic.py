import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
    get_attempt_limit,
)


class TestGetRangeForDifficulty:
    def test_easy_difficulty(self):
        low, high = get_range_for_difficulty("Easy")
        assert low == 1
        assert high == 20

    def test_normal_difficulty(self):
        low, high = get_range_for_difficulty("Normal")
        assert low == 1
        assert high == 100

    def test_hard_difficulty(self):
        low, high = get_range_for_difficulty("Hard")
        assert low == 1
        assert high == 50

    def test_unknown_difficulty(self):
        low, high = get_range_for_difficulty("Unknown")
        assert low == 1
        assert high == 100


class TestParseGuess:
    def test_valid_integer(self):
        ok, guess, error = parse_guess("42")
        assert ok is True
        assert guess == 42
        assert error is None

    def test_valid_float_as_int(self):
        ok, guess, error = parse_guess("42.0")
        assert ok is True
        assert guess == 42
        assert error is None

    def test_none_input(self):
        ok, guess, error = parse_guess(None)
        assert ok is False
        assert guess is None
        assert error == "Enter a guess."

    def test_empty_string(self):
        ok, guess, error = parse_guess("")
        assert ok is False
        assert guess is None
        assert error == "Enter a guess."

    def test_non_numeric(self):
        ok, guess, error = parse_guess("abc")
        assert ok is False
        assert guess is None
        assert error == "That is not a number."


class TestCheckGuess:
    def test_win(self):
        outcome, message = check_guess(50, 50)
        assert outcome == "Win"
        assert message == "🎉 Correct!"

    def test_too_high(self):
        outcome, message = check_guess(60, 50)
        assert outcome == "Too High"
        assert "LOWER" in message  # Hint should indicate to go lower

    def test_too_low(self):
        outcome, message = check_guess(40, 50)
        assert outcome == "Too Low"
        assert "HIGHER" in message  # Hint should indicate to go higher

    def test_type_error_handling(self):
        # Test the TypeError case where secret is string
        outcome, message = check_guess(60, "50")
        assert outcome == "Too High"
        assert "LOWER" in message

        outcome, message = check_guess(40, "50")
        assert outcome == "Too Low"
        assert "HIGHER" in message


class TestUpdateScore:
    def test_win_score(self):
        new_score = update_score(0, "Win", 1)
        assert new_score == 80  # 100 - 10 * (1 + 1) = 80

        new_score = update_score(0, "Win", 10)
        assert new_score == 10  # Minimum 10

    def test_too_high_score(self):
        # Even attempt number
        new_score = update_score(100, "Too High", 1)  # attempt_number % 2 == 1, so -5
        assert new_score == 95

        # Odd attempt number
        new_score = update_score(100, "Too High", 2)  # attempt_number % 2 == 0, so +5
        assert new_score == 105

    def test_too_low_score(self):
        new_score = update_score(100, "Too Low", 1)
        assert new_score == 95

    def test_unknown_outcome(self):
        new_score = update_score(100, "Unknown", 1)
        assert new_score == 100


class TestGetAttemptLimit:
    def test_easy_limit(self):
        limit = get_attempt_limit("Easy")
        assert limit == 6

    def test_normal_limit(self):
        limit = get_attempt_limit("Normal")
        assert limit == 8

    def test_hard_limit(self):
        limit = get_attempt_limit("Hard")
        assert limit == 5

    def test_unknown_difficulty_limit(self):
        limit = get_attempt_limit("Unknown")
        assert limit == 8


# Note: Testing the "new game" functionality requires testing the Streamlit app's session state,
# which is not directly testable from logic_utils.py. The functions above ensure that
# the game logic works correctly, and resetting the game state (secret, attempts, etc.)
# relies on the app.py code. To test new game, you would need integration tests with Streamlit.