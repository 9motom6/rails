import pytest

from rails.rails import Rails

@pytest.mark.parametrize(
    "length, expected",
    [
        pytest.param(-1, 0, id="negative_length"),
        pytest.param(0, 1, id="zero_length"),
        pytest.param(1, 1, id="length_1"),
        pytest.param(2, 2, id="length_2"),
        pytest.param(3, 4, id="length_3"),
        pytest.param(4, 7, id="length_4"),
        pytest.param(5, 13, id="length_5"),
        pytest.param(10, 274, id="length_10"),
        pytest.param(100, 180396380815100901214157639, id="length_100"),
    ],
)
def test_count_rails(length, expected):
    Rails.cache.clear()
    rails = Rails()

    assert rails.count_rails_recursive(length) == expected


@pytest.mark.parametrize(
    "length, expected",
    [
        pytest.param(-1, 0, id="negative_length"),
        pytest.param(0, 1, id="zero_length"),
        pytest.param(1, 1, id="length_1"),
        pytest.param(2, 2, id="length_2"),
        pytest.param(3, 4, id="length_3"),
        pytest.param(4, 7, id="length_4"),
        pytest.param(5, 13, id="length_5"),
        pytest.param(10, 274, id="length_10"),
        pytest.param(100, 180396380815100901214157639, id="length_100"),
        pytest.param(1000, 2758842807766486252615892411656158645133100149652696210351601845036392978912293462801016485671033253921841350537004356434253826361707295202024537559785200706502368152965047761644352316799391470273906561574500883480570560512982435681502330814068718832813973880527601, id="length_1000"),
    ],
)
def test_count_rails_iterative(length, expected):
    Rails.cache.clear()
    rails = Rails()
    print(rails.count_rails_iterative(length))
    assert rails.count_rails_iterative(length) == expected