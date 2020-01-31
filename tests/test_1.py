"""Performs general tests."""
import amodule
from sampleproject.libs import samplemodule as SM


def test_amodule():
    """Test amodule.hello()."""
    amodule.hello()


def test_true():
    """Just asserts True."""
    assert True


def test_sampleclass():
    """Test samplemodule SampleClass true method."""
    s = SM.SampleClass()
    assert s.true() is True


def test_sampleclass_false():
    """Test samplemodule SampleClass false classmethod."""
    assert SM.SampleClass.false() is False
