import operations
import pytest



@pytest.mark.parametrize(

    ('returns_input1','returns_input2','returns_output'),
    (
        (60,50,0.2),
        (30,40,-0.25),
        (5,10,-0.5)
    )
)

def test_returns(returns_input1,returns_input2,returns_output):
    assert operations.returns(returns_input1,returns_input2) == returns_output
