import pytest
from antlr4 import *
from MySQLLexer import MySQLLexer
from MySQLParser import MySQLParser
from evaluator import Evaluator


def get_evaluator_result(sql_text: str) -> int:
    """
    从 SQL 文本获取评估器结果的辅助函数
    """
    # 创建词法分析器
    input_stream = InputStream(sql_text)
    lexer = MySQLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # 创建语法分析器
    parser = MySQLParser(token_stream)

    # 解析SQL语句
    tree = parser.query()

    # 使用访问者计算表达式的值
    evaluator = Evaluator()
    result = evaluator.visit(tree)

    return result


def test_int64_literal():
    """测试简单数字"""
    sql_text = "select 42;"
    result = get_evaluator_result(sql_text)
    assert result == 42


def test_simple_expr_unary():
    """测试简单负数（不涉及运算）"""
    sql_text = "select -5;"
    result = get_evaluator_result(sql_text)
    assert result == -5


def test_bit_expr_addition():
    """测试加法运算"""
    sql_text = "select 1 + 1;"
    result = get_evaluator_result(sql_text)
    assert result == 2


def test_bit_expr_subtraction():
    """测试减法运算"""
    sql_text = "select 5 - 3;"
    result = get_evaluator_result(sql_text)
    assert result == 2


def test_bit_expr_multiplication():
    """测试乘法运算"""
    sql_text = "select 4 * 3;"
    result = get_evaluator_result(sql_text)
    assert result == 12


def test_bit_expr_division():
    """测试除法运算"""
    sql_text = "select 10 / 2;"
    result = get_evaluator_result(sql_text)
    assert result == 5


def test_bit_expr_modulo():
    """测试取模运算"""
    sql_text = "select 10 % 3;"
    result = get_evaluator_result(sql_text)
    assert result == 1


def test_division_by_zero():
    """测试除零异常"""
    sql_text = "select 10 / 0;"
    with pytest.raises(Exception, match="除零错误"):
        get_evaluator_result(sql_text)


if __name__ == "__main__":
    # 可以直接运行此文件来执行测试
    pytest.main([__file__])