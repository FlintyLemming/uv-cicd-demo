"""Simple CLI entrypoint for the calculator module.

This script provides a minimal command-line interface so the project
can be bundled into a standalone executable by the CI workflow.
"""

from __future__ import annotations

import argparse
from typing import Iterable

from src.calculator import add, divide, factorial, multiply, power, subtract


OPERATIONS = ("add", "subtract", "multiply", "divide", "power", "factorial")


def _coerce_operands(operation: str, operands: Iterable[str]) -> tuple[float | int, ...]:
    values = tuple(operands)
    if operation == "factorial":
        if len(values) != 1:
            raise ValueError("factorial requires exactly one operand")
        try:
            return (int(values[0]),)
        except ValueError as exc:  # pragma: no cover - defensive
            raise ValueError("factorial operand must be an integer") from exc

    if len(values) != 2:
        raise ValueError(f"{operation} requires exactly two operands")

    try:
        first, second = (float(values[0]), float(values[1]))
    except ValueError as exc:  # pragma: no cover - defensive
        raise ValueError("operands must be numeric") from exc
    return first, second


def _perform(operation: str, operands: tuple[float | int, ...]) -> float | int:
    if operation == "add":
        return add(*operands)
    if operation == "subtract":
        return subtract(*operands)
    if operation == "multiply":
        return multiply(*operands)
    if operation == "divide":
        return divide(*operands)
    if operation == "power":
        return power(*operands)
    if operation == "factorial":
        return factorial(int(operands[0]))
    raise ValueError(f"Unsupported operation: {operation}")  # pragma: no cover - defensive


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Perform calculator operations.")
    parser.add_argument("operation", choices=OPERATIONS, help="Operation to execute")
    parser.add_argument("operands", nargs="+", help="Operands required for the operation")
    args = parser.parse_args(argv)

    try:
        coerced = _coerce_operands(args.operation, args.operands)
        result = _perform(args.operation, coerced)
    except ValueError as exc:
        parser.error(str(exc))
        return

    if isinstance(result, float) and result.is_integer():
        # Avoid printing trailing .0 for whole numbers produced by float operations
        print(int(result))
    else:
        print(result)


if __name__ == "__main__":  # pragma: no cover - manual exec
    main()
