"""简单的计算器模块，用于 CI/CD 演示。

这个模块包含基本的数学运算函数，同时展示了一些常见的
编程模式和测试场景。
"""

from __future__ import annotations

from typing import Union


Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """两数相加

    Args:
        a: 第一个数字
        b: 第二个数字

    Returns:
        两数之和

    Examples:
        >>> add(2, 3)
        5
        >>> add(1.5, 2.5)
        4.0
    """
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """两数相减

    Args:
        a: 被减数
        b: 减数

    Returns:
        两数之差
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """两数相乘

    Args:
        a: 第一个数字
        b: 第二个数字

    Returns:
        两数之积
    """
    return a * b


def divide(a: Number, b: Number) -> Number:
    """两数相除

    Args:
        a: 被除数
        b: 除数

    Returns:
        两数之商

    Raises:
        ZeroDivisionError: 当除数为 0 时抛出
    """
    if b == 0:
        raise ZeroDivisionError("除数不能为 0")
    return a / b


def power(base: Number, exponent: Number) -> Number:
    """计算幂运算

    Args:
        base: 底数
        exponent: 指数

    Returns:
        base 的 exponent 次方

    Raises:
        ValueError: 当指数为负数且底数为 0 时抛出
    """
    if base == 0 and exponent < 0:
        raise ValueError("0 的负数次幂未定义")
    return base ** exponent


def factorial(n: int) -> int:
    """计算阶乘

    Args:
        n: 非负整数

    Returns:
        n 的阶乘

    Raises:
        ValueError: 当 n 为负数时抛出
    """
    if n < 0:
        raise ValueError("阶乘只对非负整数定义")
    if n in (0, 1):
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result