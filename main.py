from antlr4 import *
from MySQLLexer import MySQLLexer
from MySQLParser import MySQLParser
from MySQLParserVisitor import MySQLParserVisitor

class ExpressionEvaluator(MySQLParserVisitor):
    """
    表达式求值器，继承自MySQLParserVisitor
    用于解析和计算SQL表达式，如 select 1 + 1
    """
    
    def visitQuery(self, ctx):
        if ctx.simpleStatement():
            return self.visit(ctx.simpleStatement())
        return self.visitChildren(ctx)
    
    def visitSimpleStatement(self, ctx):
        if ctx.selectStatement():
            return self.visit(ctx.selectStatement())
        return self.visitChildren(ctx)
    
    def visitSelectStatement(self, ctx):
        if ctx.queryExpression():
            return self.visit(ctx.queryExpression())
        return self.visitChildren(ctx)
    
    def visitQueryExpression(self, ctx):
        if ctx.queryExpressionBody():
            return self.visit(ctx.queryExpressionBody())
        return self.visitChildren(ctx)
    
    def visitQueryExpressionBody(self, ctx):
        if ctx.queryPrimary():
            return self.visit(ctx.queryPrimary())
        return self.visitChildren(ctx)
    
    def visitQueryPrimary(self, ctx):
        if ctx.querySpecification():
            return self.visit(ctx.querySpecification())
        return self.visitChildren(ctx)
    
    def visitQuerySpecification(self, ctx):
        if ctx.selectItemList():
            return self.visit(ctx.selectItemList())
        return self.visitChildren(ctx)
    
    def visitSelectItemList(self, ctx):
        if ctx.selectItem(0):
            return self.visit(ctx.selectItem(0))
        return self.visitChildren(ctx)
    
    def visitSelectItem(self, ctx):
        if ctx.expr():
            return self.visit(ctx.expr())
        return self.visitChildren(ctx)
    
    def visitExprIs(self, ctx):
        # 访问第一个子节点
        if ctx.getChildCount() > 0:
            return self.visit(ctx.getChild(0))
        return self.visitChildren(ctx)
    
    def visitPrimaryExprPredicate(self, ctx):
        if ctx.getChildCount() > 0:
            return self.visit(ctx.getChild(0))
        return self.visitChildren(ctx)
    
    def visitBoolPri(self, ctx):
        if ctx.getChildCount() > 0:
            return self.visit(ctx.getChild(0))
        return self.visitChildren(ctx)
    
    def visitPredicate(self, ctx):
        if ctx.getChildCount() > 0:
            return self.visit(ctx.getChild(0))
        return self.visitChildren(ctx)
    
    def visitBitExpr(self, ctx):
        # 检查是否为二元运算表达式 (expr op expr)
        if ctx.getChildCount() == 3:
            left_ctx = ctx.getChild(0)
            op_token = ctx.getChild(1)
            right_ctx = ctx.getChild(2)
            
            left_val = self.visit(left_ctx)
            op = op_token.getText()
            right_val = self.visit(right_ctx)
            
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '*':
                return left_val * right_val
            elif op == '/':
                if right_val != 0:
                    return left_val / right_val
                else:
                    raise Exception("除零错误")
            elif op == '%':
                return left_val % right_val
        else:
            # 单个表达式或继续访问子节点
            return self.visitChildren(ctx)
    
    def visitSimpleExprLiteral(self, ctx):
        if ctx.getChildCount() > 0:
            return self.visit(ctx.getChild(0))
        return self.visitChildren(ctx)
    
    def visitLiteralOrNull(self, ctx):
        if ctx.getChildCount() > 0:
            return self.visit(ctx.getChild(0))
        return self.visitChildren(ctx)
    
    def visitLiteral(self, ctx):
        if ctx.getChildCount() > 0:
            return self.visit(ctx.getChild(0))
        return self.visitChildren(ctx)
    
    def visitNumLiteral(self, ctx):
        if ctx.getChildCount() > 0:
            first_child = ctx.getChild(0)
            if hasattr(first_child, 'getText'):
                text = first_child.getText()
                if text.isdigit() or (text.startswith('-') and text[1:].isdigit()):
                    return int(text)
                else:
                    try:
                        return float(text)
                    except:
                        return self.visitChildren(ctx)
        return self.visitChildren(ctx)

def evaluate_sql(sql_text):
    """
    解析并计算SQL表达式的值
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
    evaluator = ExpressionEvaluator()
    result = evaluator.visit(tree)
    
    print(f"SQL语句: {sql_text}")
    print(f"计算结果: {result}")
    
    return result

def main():
    print("MySQL SQL表达式求值器")
    print("="*40)
    print("使用访问者模式解析和计算SQL表达式")
    print()
    
    # 主要测试：select 1 + 1
    sql = "select 1 + 1;"
    print("目标SQL: ", sql)
    result = evaluate_sql(sql)
    print(f"eval结果: {result}")
    print()
    
    print("其他示例:")
    examples = [
        "select 2 + 3;",
        "select 10 - 4;",
        "select 5 * 6;",
        "select 20 / 4;"
    ]
    
    for example in examples:
        result = evaluate_sql(example)
        print(f"eval结果: {result}")
        print()

if __name__ == '__main__':
    main()