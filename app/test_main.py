import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, cat_expected_human_age, dog_expected_human_age",
    [
        (0, 0, 0, 0),
        (14, 14, 0, 0),
        (15, 15, 1, 1),
        (28, 28, 3, 2),
        (100, 100, 21, 17)
    ]
)
def test_get_human_age(
        cat_age,
        dog_age,
        cat_expected_human_age,
        dog_expected_human_age
):
    assert get_human_age(cat_age, dog_age) == [cat_expected_human_age, dog_expected_human_age]


@pytest.mark.parametrize(
    "bad_input",
    [
        "twenty",
        5.5,
        None,
        [10, 20],
        {"five": 5},
        (3, 3),
        False
    ]
)
def test_bad_input(bad_input):
    with pytest.raises(TypeError):
        get_human_age(bad_input, bad_input)
