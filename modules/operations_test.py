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



@pytest.mark.parametrize(

    ('sharpe_input1','sharpe_input2','sharpe_input3','sharpe_output'),
    (
        (0.02,0.04,0.03,-0.25),
        (0.035,0.1,0.02,0.15),
        (0.05,0.005,0.04,2)
    )
)

def test_sharpe(sharpe_input1,sharpe_input2,sharpe_input3,sharpe_output):
    ratio = operations.sharpe_ratio(sharpe_input1,sharpe_input2,sharpe_input3)
    assert pytest.approx(ratio) == sharpe_output
