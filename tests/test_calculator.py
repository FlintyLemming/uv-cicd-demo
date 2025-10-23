"""计算器模块的测试用例

展示如何使用 pytest 进行单元测试，包含各种测试场景：
- 基本功能测试
- 边界条件测试
- 异常处理测试
- 参数化测试
"""

from __future__ import annotations

import pytest

from src.calculator import add, divide, factorial, multiply, power, subtract


class TestBasicOperations:
    """基本运算功能测试"""

    def test_add(self) -> None:
        """测试加法"""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(1.5, 2.5) == 4.0
        assert add(0, 0) == 0

    def test_subtract(self) -> None:
        """测试减法"""
        assert subtract(5, 3) == 2
        assert subtract(1, 1) == 0
        assert subtract(10.5, 5.5) == 5.0

    def test_multiply(self) -> None:
        """测试乘法"""
        assert multiply(2, 3) == 6
        assert multiply(0, 5) == 0
        assert multiply(-2, 3) == -6
        assert multiply(1.5, 2) == 3.0

    @pytest.mark.parametrize("a,b,expected", [
        (6, 2, 3),
        (10, 5, 2),
        (4, 2, 2),
        (9, 3, 3),
        (1, 1, 1),
    ])
    def test_divide_normal(self, a: int | float, b: int | float, expected: int | float) -> None:
        """参数化测试除法正常情况"""
        assert divide(a, b) == expected

    def test_divide_zero(self) -> None:
        """测试除数为零的情况"""
        with pytest.raises(ZeroDivisionError, match="除数不能为 0"):
            divide(5, 0)


class TestAdvancedOperations:
    """高级运算功能测试"""

    @pytest.mark.parametrize("base,exponent,expected", [
        (2, 3, 8),
        (5, 0, 1),
        (10, 2, 100),
        (-2, 3, -8),
        (4, 0.5, 2),
    ])
    def test_power_normal(self, base: int | float, exponent: int | float, expected: int | float) -> None:
        """参数化测试幂运算正常情况"""
        assert power(base, exponent) == expected

    def test_power_zero_negative_exponent(self) -> None:
        """测试 0 的负数次幂"""
        with pytest.raises(ValueError, match="0 的负数次幂未定义"):
            power(0, -1)


class TestFactorial:
    """阶乘功能测试"""

    @pytest.mark.parametrize("n,expected", [
        (0, 1),
        (1, 1),
        (3, 6),
        (5, 120),
        (6, 720),
    ])
    def test_factorial_normal(self, n: int, expected: int) -> None:
        """参数化测试阶乘正常情况"""
        assert factorial(n) == expected

    def test_factorial_negative(self) -> None:
        """测试负数的阶乘"""
        with pytest.raises(ValueError, match="阶乘只对非负整数定义"):
            factorial(-1)


class TestEdgeCases:
    """边界条件测试"""

    def test_large_numbers(self) -> None:
        """测试大数运算"""
        big_num = 10**6
        assert add(big_num, 1) == big_num + 1
        assert multiply(big_num, 0) == 0

    def test_floating_point_precision(self) -> None:
        """测试浮点数精度"""
        result = add(0.1, 0.2)
        # 浮点数精度问题，使用 approx 进行比较
        assert pytest.approx(result, 0.0001) == 0.3

    def test_mix_int_float(self) -> None:
        """测试整数和浮点数混合运算"""
        assert add(2, 3.5) == 5.5
        assert multiply(4, 2.5) == 10.0