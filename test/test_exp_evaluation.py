import pytest
from ..src.pyrser import Pyrser


@pytest.fixture
def parser():
    return Pyrser()


def test_sum(parser):
    assert parser.parse('1+2').evaluate() == 3


def test_sub(parser):
    assert parser.parse('1-2').evaluate() == -1


def test_mul(parser):
    assert parser.parse('2*3').evaluate() == 6


def test_div(parser):
    assert parser.parse('9/3').evaluate() == 3


def test_pow(parser):
    assert parser.parse('2^3').evaluate() == 8


def test_parenthesis(parser):
    assert parser.parse('(-(3)*5)+(2*4)').evaluate() == -7


def test_three_sum_terms(parser):
    assert parser.parse('1+2+3').evaluate() == 6


def test_three_sub_terms(parser):
    assert parser.parse('1-2-3').evaluate() == -4


def test_three_mul_terms(parser):
    assert parser.parse('1*2*3').evaluate() == 6


def test_three_pows(parser):
    assert parser.parse('2^2^3').evaluate() == (2 ** 8)


def test_unary_plus_easy(parser):
    assert parser.parse('(+3)').evaluate() == 3


def test_unary_plus(parser):
    assert parser.parse('+3-(+3)++5').evaluate() == 5


def test_unary_minus(parser):
    assert parser.parse('-3-(-3)+-5').evaluate() == -5


def no_prob_with_whitespace(parser):
    assert parser.parse('  1 +  2   ').evaluate() == 3
