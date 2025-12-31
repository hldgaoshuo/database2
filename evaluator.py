from MySQLParser import MySQLParser
from MySQLParserVisitor import MySQLParserVisitor


class Evaluator(MySQLParserVisitor):

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

    def visitSimpleExprUnary(self, ctx):
        # 处理一元运算符，如负号 (-)
        if ctx.getChildCount() == 2:  # 一元运算符 + 操作数
            op_token = ctx.getChild(0)
            operand_ctx = ctx.getChild(1)

            op = op_token.getText()
            operand_val = self.visit(operand_ctx)

            if op == '-':
                return -operand_val
            elif op == '+':
                return operand_val
            else:
                # 其他一元运算符，返回原值
                return self.visitChildren(ctx)
        else:
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
            return self.visit(ctx.getChild(0))
        return self.visitChildren(ctx)

    def visitInt64Literal(self, ctx:MySQLParser.Int64LiteralContext):
        return int(ctx.getText())
