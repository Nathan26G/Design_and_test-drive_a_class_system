from lib.tyre import *

def test_default_values_in_dict_correct_when_initated():
    new_tyre = Tyre('front left')
    tyre_dict = new_tyre.tyres
    assert tyre_dict['position'] == 'front left'