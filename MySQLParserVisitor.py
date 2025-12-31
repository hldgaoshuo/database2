# Generated from MySQLParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MySQLParser import MySQLParser
else:
    from MySQLParser import MySQLParser

# This class defines a complete generic visitor for a parse tree produced by MySQLParser.

class MySQLParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MySQLParser#queries.
    def visitQueries(self, ctx:MySQLParser.QueriesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#query.
    def visitQuery(self, ctx:MySQLParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleStatement.
    def visitSimpleStatement(self, ctx:MySQLParser.SimpleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterStatement.
    def visitAlterStatement(self, ctx:MySQLParser.AlterStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterDatabase.
    def visitAlterDatabase(self, ctx:MySQLParser.AlterDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterDatabaseOption.
    def visitAlterDatabaseOption(self, ctx:MySQLParser.AlterDatabaseOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterEvent.
    def visitAlterEvent(self, ctx:MySQLParser.AlterEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterLogfileGroup.
    def visitAlterLogfileGroup(self, ctx:MySQLParser.AlterLogfileGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterLogfileGroupOptions.
    def visitAlterLogfileGroupOptions(self, ctx:MySQLParser.AlterLogfileGroupOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterLogfileGroupOption.
    def visitAlterLogfileGroupOption(self, ctx:MySQLParser.AlterLogfileGroupOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterServer.
    def visitAlterServer(self, ctx:MySQLParser.AlterServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterTable.
    def visitAlterTable(self, ctx:MySQLParser.AlterTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterTableActions.
    def visitAlterTableActions(self, ctx:MySQLParser.AlterTableActionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterCommandList.
    def visitAlterCommandList(self, ctx:MySQLParser.AlterCommandListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterCommandsModifierList.
    def visitAlterCommandsModifierList(self, ctx:MySQLParser.AlterCommandsModifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#standaloneAlterCommands.
    def visitStandaloneAlterCommands(self, ctx:MySQLParser.StandaloneAlterCommandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterPartition.
    def visitAlterPartition(self, ctx:MySQLParser.AlterPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterList.
    def visitAlterList(self, ctx:MySQLParser.AlterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterCommandsModifier.
    def visitAlterCommandsModifier(self, ctx:MySQLParser.AlterCommandsModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterListItem.
    def visitAlterListItem(self, ctx:MySQLParser.AlterListItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#place.
    def visitPlace(self, ctx:MySQLParser.PlaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#restrict.
    def visitRestrict(self, ctx:MySQLParser.RestrictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterOrderList.
    def visitAlterOrderList(self, ctx:MySQLParser.AlterOrderListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterAlgorithmOption.
    def visitAlterAlgorithmOption(self, ctx:MySQLParser.AlterAlgorithmOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterLockOption.
    def visitAlterLockOption(self, ctx:MySQLParser.AlterLockOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#indexLockAndAlgorithm.
    def visitIndexLockAndAlgorithm(self, ctx:MySQLParser.IndexLockAndAlgorithmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#withValidation.
    def visitWithValidation(self, ctx:MySQLParser.WithValidationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#removePartitioning.
    def visitRemovePartitioning(self, ctx:MySQLParser.RemovePartitioningContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#allOrPartitionNameList.
    def visitAllOrPartitionNameList(self, ctx:MySQLParser.AllOrPartitionNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterTablespace.
    def visitAlterTablespace(self, ctx:MySQLParser.AlterTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterUndoTablespace.
    def visitAlterUndoTablespace(self, ctx:MySQLParser.AlterUndoTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#undoTableSpaceOptions.
    def visitUndoTableSpaceOptions(self, ctx:MySQLParser.UndoTableSpaceOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#undoTableSpaceOption.
    def visitUndoTableSpaceOption(self, ctx:MySQLParser.UndoTableSpaceOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterTablespaceOptions.
    def visitAlterTablespaceOptions(self, ctx:MySQLParser.AlterTablespaceOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterTablespaceOption.
    def visitAlterTablespaceOption(self, ctx:MySQLParser.AlterTablespaceOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeTablespaceOption.
    def visitChangeTablespaceOption(self, ctx:MySQLParser.ChangeTablespaceOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterView.
    def visitAlterView(self, ctx:MySQLParser.AlterViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#viewTail.
    def visitViewTail(self, ctx:MySQLParser.ViewTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#viewQueryBlock.
    def visitViewQueryBlock(self, ctx:MySQLParser.ViewQueryBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#viewCheckOption.
    def visitViewCheckOption(self, ctx:MySQLParser.ViewCheckOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterInstanceStatement.
    def visitAlterInstanceStatement(self, ctx:MySQLParser.AlterInstanceStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createStatement.
    def visitCreateStatement(self, ctx:MySQLParser.CreateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createDatabase.
    def visitCreateDatabase(self, ctx:MySQLParser.CreateDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createDatabaseOption.
    def visitCreateDatabaseOption(self, ctx:MySQLParser.CreateDatabaseOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createTable.
    def visitCreateTable(self, ctx:MySQLParser.CreateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tableElementList.
    def visitTableElementList(self, ctx:MySQLParser.TableElementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tableElement.
    def visitTableElement(self, ctx:MySQLParser.TableElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#duplicateAsQe.
    def visitDuplicateAsQe(self, ctx:MySQLParser.DuplicateAsQeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#asCreateQueryExpression.
    def visitAsCreateQueryExpression(self, ctx:MySQLParser.AsCreateQueryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#queryExpressionOrParens.
    def visitQueryExpressionOrParens(self, ctx:MySQLParser.QueryExpressionOrParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#queryExpressionWithOptLockingClauses.
    def visitQueryExpressionWithOptLockingClauses(self, ctx:MySQLParser.QueryExpressionWithOptLockingClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createRoutine.
    def visitCreateRoutine(self, ctx:MySQLParser.CreateRoutineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createProcedure.
    def visitCreateProcedure(self, ctx:MySQLParser.CreateProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#routineString.
    def visitRoutineString(self, ctx:MySQLParser.RoutineStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#storedRoutineBody.
    def visitStoredRoutineBody(self, ctx:MySQLParser.StoredRoutineBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createFunction.
    def visitCreateFunction(self, ctx:MySQLParser.CreateFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createUdf.
    def visitCreateUdf(self, ctx:MySQLParser.CreateUdfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#routineCreateOption.
    def visitRoutineCreateOption(self, ctx:MySQLParser.RoutineCreateOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#routineAlterOptions.
    def visitRoutineAlterOptions(self, ctx:MySQLParser.RoutineAlterOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#routineOption.
    def visitRoutineOption(self, ctx:MySQLParser.RoutineOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createIndex.
    def visitCreateIndex(self, ctx:MySQLParser.CreateIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#indexNameAndType.
    def visitIndexNameAndType(self, ctx:MySQLParser.IndexNameAndTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createIndexTarget.
    def visitCreateIndexTarget(self, ctx:MySQLParser.CreateIndexTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createLogfileGroup.
    def visitCreateLogfileGroup(self, ctx:MySQLParser.CreateLogfileGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#logfileGroupOptions.
    def visitLogfileGroupOptions(self, ctx:MySQLParser.LogfileGroupOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#logfileGroupOption.
    def visitLogfileGroupOption(self, ctx:MySQLParser.LogfileGroupOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createServer.
    def visitCreateServer(self, ctx:MySQLParser.CreateServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#serverOptions.
    def visitServerOptions(self, ctx:MySQLParser.ServerOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#serverOption.
    def visitServerOption(self, ctx:MySQLParser.ServerOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createTablespace.
    def visitCreateTablespace(self, ctx:MySQLParser.CreateTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createUndoTablespace.
    def visitCreateUndoTablespace(self, ctx:MySQLParser.CreateUndoTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tsDataFileName.
    def visitTsDataFileName(self, ctx:MySQLParser.TsDataFileNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tsDataFile.
    def visitTsDataFile(self, ctx:MySQLParser.TsDataFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tablespaceOptions.
    def visitTablespaceOptions(self, ctx:MySQLParser.TablespaceOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tablespaceOption.
    def visitTablespaceOption(self, ctx:MySQLParser.TablespaceOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tsOptionInitialSize.
    def visitTsOptionInitialSize(self, ctx:MySQLParser.TsOptionInitialSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tsOptionUndoRedoBufferSize.
    def visitTsOptionUndoRedoBufferSize(self, ctx:MySQLParser.TsOptionUndoRedoBufferSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tsOptionAutoextendSize.
    def visitTsOptionAutoextendSize(self, ctx:MySQLParser.TsOptionAutoextendSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tsOptionMaxSize.
    def visitTsOptionMaxSize(self, ctx:MySQLParser.TsOptionMaxSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tsOptionExtentSize.
    def visitTsOptionExtentSize(self, ctx:MySQLParser.TsOptionExtentSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tsOptionNodegroup.
    def visitTsOptionNodegroup(self, ctx:MySQLParser.TsOptionNodegroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tsOptionEngine.
    def visitTsOptionEngine(self, ctx:MySQLParser.TsOptionEngineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tsOptionWait.
    def visitTsOptionWait(self, ctx:MySQLParser.TsOptionWaitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tsOptionComment.
    def visitTsOptionComment(self, ctx:MySQLParser.TsOptionCommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tsOptionFileblockSize.
    def visitTsOptionFileblockSize(self, ctx:MySQLParser.TsOptionFileblockSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tsOptionEncryption.
    def visitTsOptionEncryption(self, ctx:MySQLParser.TsOptionEncryptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tsOptionEngineAttribute.
    def visitTsOptionEngineAttribute(self, ctx:MySQLParser.TsOptionEngineAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createView.
    def visitCreateView(self, ctx:MySQLParser.CreateViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#viewReplaceOrAlgorithm.
    def visitViewReplaceOrAlgorithm(self, ctx:MySQLParser.ViewReplaceOrAlgorithmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#viewAlgorithm.
    def visitViewAlgorithm(self, ctx:MySQLParser.ViewAlgorithmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#viewSuid.
    def visitViewSuid(self, ctx:MySQLParser.ViewSuidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createTrigger.
    def visitCreateTrigger(self, ctx:MySQLParser.CreateTriggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#triggerFollowsPrecedesClause.
    def visitTriggerFollowsPrecedesClause(self, ctx:MySQLParser.TriggerFollowsPrecedesClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createEvent.
    def visitCreateEvent(self, ctx:MySQLParser.CreateEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createRole.
    def visitCreateRole(self, ctx:MySQLParser.CreateRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createSpatialReference.
    def visitCreateSpatialReference(self, ctx:MySQLParser.CreateSpatialReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#srsAttribute.
    def visitSrsAttribute(self, ctx:MySQLParser.SrsAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dropStatement.
    def visitDropStatement(self, ctx:MySQLParser.DropStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dropDatabase.
    def visitDropDatabase(self, ctx:MySQLParser.DropDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dropEvent.
    def visitDropEvent(self, ctx:MySQLParser.DropEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dropFunction.
    def visitDropFunction(self, ctx:MySQLParser.DropFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dropProcedure.
    def visitDropProcedure(self, ctx:MySQLParser.DropProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dropIndex.
    def visitDropIndex(self, ctx:MySQLParser.DropIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dropLogfileGroup.
    def visitDropLogfileGroup(self, ctx:MySQLParser.DropLogfileGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dropLogfileGroupOption.
    def visitDropLogfileGroupOption(self, ctx:MySQLParser.DropLogfileGroupOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dropServer.
    def visitDropServer(self, ctx:MySQLParser.DropServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dropTable.
    def visitDropTable(self, ctx:MySQLParser.DropTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dropTableSpace.
    def visitDropTableSpace(self, ctx:MySQLParser.DropTableSpaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dropTrigger.
    def visitDropTrigger(self, ctx:MySQLParser.DropTriggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dropView.
    def visitDropView(self, ctx:MySQLParser.DropViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dropRole.
    def visitDropRole(self, ctx:MySQLParser.DropRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dropSpatialReference.
    def visitDropSpatialReference(self, ctx:MySQLParser.DropSpatialReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dropUndoTablespace.
    def visitDropUndoTablespace(self, ctx:MySQLParser.DropUndoTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#renameTableStatement.
    def visitRenameTableStatement(self, ctx:MySQLParser.RenameTableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#renamePair.
    def visitRenamePair(self, ctx:MySQLParser.RenamePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#truncateTableStatement.
    def visitTruncateTableStatement(self, ctx:MySQLParser.TruncateTableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#importStatement.
    def visitImportStatement(self, ctx:MySQLParser.ImportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#callStatement.
    def visitCallStatement(self, ctx:MySQLParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#deleteStatement.
    def visitDeleteStatement(self, ctx:MySQLParser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#partitionDelete.
    def visitPartitionDelete(self, ctx:MySQLParser.PartitionDeleteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#deleteStatementOption.
    def visitDeleteStatementOption(self, ctx:MySQLParser.DeleteStatementOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#doStatement.
    def visitDoStatement(self, ctx:MySQLParser.DoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#handlerStatement.
    def visitHandlerStatement(self, ctx:MySQLParser.HandlerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#handlerReadOrScan.
    def visitHandlerReadOrScan(self, ctx:MySQLParser.HandlerReadOrScanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#insertStatement.
    def visitInsertStatement(self, ctx:MySQLParser.InsertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#insertLockOption.
    def visitInsertLockOption(self, ctx:MySQLParser.InsertLockOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#insertFromConstructor.
    def visitInsertFromConstructor(self, ctx:MySQLParser.InsertFromConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#fields.
    def visitFields(self, ctx:MySQLParser.FieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#insertValues.
    def visitInsertValues(self, ctx:MySQLParser.InsertValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#insertQueryExpression.
    def visitInsertQueryExpression(self, ctx:MySQLParser.InsertQueryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#valueList.
    def visitValueList(self, ctx:MySQLParser.ValueListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#values.
    def visitValues(self, ctx:MySQLParser.ValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#valuesReference.
    def visitValuesReference(self, ctx:MySQLParser.ValuesReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#insertUpdateList.
    def visitInsertUpdateList(self, ctx:MySQLParser.InsertUpdateListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#loadStatement.
    def visitLoadStatement(self, ctx:MySQLParser.LoadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dataOrXml.
    def visitDataOrXml(self, ctx:MySQLParser.DataOrXmlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#loadDataLock.
    def visitLoadDataLock(self, ctx:MySQLParser.LoadDataLockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#loadFrom.
    def visitLoadFrom(self, ctx:MySQLParser.LoadFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#loadSourceType.
    def visitLoadSourceType(self, ctx:MySQLParser.LoadSourceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#sourceCount.
    def visitSourceCount(self, ctx:MySQLParser.SourceCountContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#sourceOrder.
    def visitSourceOrder(self, ctx:MySQLParser.SourceOrderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#xmlRowsIdentifiedBy.
    def visitXmlRowsIdentifiedBy(self, ctx:MySQLParser.XmlRowsIdentifiedByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#loadDataFileTail.
    def visitLoadDataFileTail(self, ctx:MySQLParser.LoadDataFileTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#loadDataFileTargetList.
    def visitLoadDataFileTargetList(self, ctx:MySQLParser.LoadDataFileTargetListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#fieldOrVariableList.
    def visitFieldOrVariableList(self, ctx:MySQLParser.FieldOrVariableListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#loadAlgorithm.
    def visitLoadAlgorithm(self, ctx:MySQLParser.LoadAlgorithmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#loadParallel.
    def visitLoadParallel(self, ctx:MySQLParser.LoadParallelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#loadMemory.
    def visitLoadMemory(self, ctx:MySQLParser.LoadMemoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#replaceStatement.
    def visitReplaceStatement(self, ctx:MySQLParser.ReplaceStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#selectStatement.
    def visitSelectStatement(self, ctx:MySQLParser.SelectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#selectStatementWithInto.
    def visitSelectStatementWithInto(self, ctx:MySQLParser.SelectStatementWithIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#queryExpression.
    def visitQueryExpression(self, ctx:MySQLParser.QueryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#queryExpressionBody.
    def visitQueryExpressionBody(self, ctx:MySQLParser.QueryExpressionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#queryExpressionParens.
    def visitQueryExpressionParens(self, ctx:MySQLParser.QueryExpressionParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#queryPrimary.
    def visitQueryPrimary(self, ctx:MySQLParser.QueryPrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#querySpecification.
    def visitQuerySpecification(self, ctx:MySQLParser.QuerySpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#subquery.
    def visitSubquery(self, ctx:MySQLParser.SubqueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#querySpecOption.
    def visitQuerySpecOption(self, ctx:MySQLParser.QuerySpecOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#limitClause.
    def visitLimitClause(self, ctx:MySQLParser.LimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleLimitClause.
    def visitSimpleLimitClause(self, ctx:MySQLParser.SimpleLimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#limitOptions.
    def visitLimitOptions(self, ctx:MySQLParser.LimitOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#limitOption.
    def visitLimitOption(self, ctx:MySQLParser.LimitOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#intoClause.
    def visitIntoClause(self, ctx:MySQLParser.IntoClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#procedureAnalyseClause.
    def visitProcedureAnalyseClause(self, ctx:MySQLParser.ProcedureAnalyseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#havingClause.
    def visitHavingClause(self, ctx:MySQLParser.HavingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#qualifyClause.
    def visitQualifyClause(self, ctx:MySQLParser.QualifyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#windowClause.
    def visitWindowClause(self, ctx:MySQLParser.WindowClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#windowDefinition.
    def visitWindowDefinition(self, ctx:MySQLParser.WindowDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#windowSpec.
    def visitWindowSpec(self, ctx:MySQLParser.WindowSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#windowSpecDetails.
    def visitWindowSpecDetails(self, ctx:MySQLParser.WindowSpecDetailsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#windowFrameClause.
    def visitWindowFrameClause(self, ctx:MySQLParser.WindowFrameClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#windowFrameUnits.
    def visitWindowFrameUnits(self, ctx:MySQLParser.WindowFrameUnitsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#windowFrameExtent.
    def visitWindowFrameExtent(self, ctx:MySQLParser.WindowFrameExtentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#windowFrameStart.
    def visitWindowFrameStart(self, ctx:MySQLParser.WindowFrameStartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#windowFrameBetween.
    def visitWindowFrameBetween(self, ctx:MySQLParser.WindowFrameBetweenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#windowFrameBound.
    def visitWindowFrameBound(self, ctx:MySQLParser.WindowFrameBoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#windowFrameExclusion.
    def visitWindowFrameExclusion(self, ctx:MySQLParser.WindowFrameExclusionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#withClause.
    def visitWithClause(self, ctx:MySQLParser.WithClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#commonTableExpression.
    def visitCommonTableExpression(self, ctx:MySQLParser.CommonTableExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#groupByClause.
    def visitGroupByClause(self, ctx:MySQLParser.GroupByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#olapOption.
    def visitOlapOption(self, ctx:MySQLParser.OlapOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#orderClause.
    def visitOrderClause(self, ctx:MySQLParser.OrderClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#direction.
    def visitDirection(self, ctx:MySQLParser.DirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#fromClause.
    def visitFromClause(self, ctx:MySQLParser.FromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tableReferenceList.
    def visitTableReferenceList(self, ctx:MySQLParser.TableReferenceListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tableValueConstructor.
    def visitTableValueConstructor(self, ctx:MySQLParser.TableValueConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#explicitTable.
    def visitExplicitTable(self, ctx:MySQLParser.ExplicitTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#rowValueExplicit.
    def visitRowValueExplicit(self, ctx:MySQLParser.RowValueExplicitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#selectOption.
    def visitSelectOption(self, ctx:MySQLParser.SelectOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#lockingClauseList.
    def visitLockingClauseList(self, ctx:MySQLParser.LockingClauseListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#lockingClause.
    def visitLockingClause(self, ctx:MySQLParser.LockingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#lockStrengh.
    def visitLockStrengh(self, ctx:MySQLParser.LockStrenghContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#lockedRowAction.
    def visitLockedRowAction(self, ctx:MySQLParser.LockedRowActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#selectItemList.
    def visitSelectItemList(self, ctx:MySQLParser.SelectItemListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#selectItem.
    def visitSelectItem(self, ctx:MySQLParser.SelectItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#selectAlias.
    def visitSelectAlias(self, ctx:MySQLParser.SelectAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#whereClause.
    def visitWhereClause(self, ctx:MySQLParser.WhereClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tableReference.
    def visitTableReference(self, ctx:MySQLParser.TableReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#escapedTableReference.
    def visitEscapedTableReference(self, ctx:MySQLParser.EscapedTableReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#joinedTable.
    def visitJoinedTable(self, ctx:MySQLParser.JoinedTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#naturalJoinType.
    def visitNaturalJoinType(self, ctx:MySQLParser.NaturalJoinTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#innerJoinType.
    def visitInnerJoinType(self, ctx:MySQLParser.InnerJoinTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#outerJoinType.
    def visitOuterJoinType(self, ctx:MySQLParser.OuterJoinTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tableFactor.
    def visitTableFactor(self, ctx:MySQLParser.TableFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#singleTable.
    def visitSingleTable(self, ctx:MySQLParser.SingleTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#singleTableParens.
    def visitSingleTableParens(self, ctx:MySQLParser.SingleTableParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#derivedTable.
    def visitDerivedTable(self, ctx:MySQLParser.DerivedTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tableReferenceListParens.
    def visitTableReferenceListParens(self, ctx:MySQLParser.TableReferenceListParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tableFunction.
    def visitTableFunction(self, ctx:MySQLParser.TableFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#columnsClause.
    def visitColumnsClause(self, ctx:MySQLParser.ColumnsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#jtColumn.
    def visitJtColumn(self, ctx:MySQLParser.JtColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#onEmptyOrError.
    def visitOnEmptyOrError(self, ctx:MySQLParser.OnEmptyOrErrorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#onEmptyOrErrorJsonTable.
    def visitOnEmptyOrErrorJsonTable(self, ctx:MySQLParser.OnEmptyOrErrorJsonTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#onEmpty.
    def visitOnEmpty(self, ctx:MySQLParser.OnEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#onError.
    def visitOnError(self, ctx:MySQLParser.OnErrorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#jsonOnResponse.
    def visitJsonOnResponse(self, ctx:MySQLParser.JsonOnResponseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#unionOption.
    def visitUnionOption(self, ctx:MySQLParser.UnionOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tableAlias.
    def visitTableAlias(self, ctx:MySQLParser.TableAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#indexHintList.
    def visitIndexHintList(self, ctx:MySQLParser.IndexHintListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#indexHint.
    def visitIndexHint(self, ctx:MySQLParser.IndexHintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#indexHintType.
    def visitIndexHintType(self, ctx:MySQLParser.IndexHintTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#keyOrIndex.
    def visitKeyOrIndex(self, ctx:MySQLParser.KeyOrIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#constraintKeyType.
    def visitConstraintKeyType(self, ctx:MySQLParser.ConstraintKeyTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#indexHintClause.
    def visitIndexHintClause(self, ctx:MySQLParser.IndexHintClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#indexList.
    def visitIndexList(self, ctx:MySQLParser.IndexListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#indexListElement.
    def visitIndexListElement(self, ctx:MySQLParser.IndexListElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#updateStatement.
    def visitUpdateStatement(self, ctx:MySQLParser.UpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#transactionOrLockingStatement.
    def visitTransactionOrLockingStatement(self, ctx:MySQLParser.TransactionOrLockingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#transactionStatement.
    def visitTransactionStatement(self, ctx:MySQLParser.TransactionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#beginWork.
    def visitBeginWork(self, ctx:MySQLParser.BeginWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#startTransactionOptionList.
    def visitStartTransactionOptionList(self, ctx:MySQLParser.StartTransactionOptionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#savepointStatement.
    def visitSavepointStatement(self, ctx:MySQLParser.SavepointStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#lockStatement.
    def visitLockStatement(self, ctx:MySQLParser.LockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#lockItem.
    def visitLockItem(self, ctx:MySQLParser.LockItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#lockOption.
    def visitLockOption(self, ctx:MySQLParser.LockOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#xaStatement.
    def visitXaStatement(self, ctx:MySQLParser.XaStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#xaConvert.
    def visitXaConvert(self, ctx:MySQLParser.XaConvertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#xid.
    def visitXid(self, ctx:MySQLParser.XidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#replicationStatement.
    def visitReplicationStatement(self, ctx:MySQLParser.ReplicationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#purgeOptions.
    def visitPurgeOptions(self, ctx:MySQLParser.PurgeOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#resetOption.
    def visitResetOption(self, ctx:MySQLParser.ResetOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#masterOrBinaryLogsAndGtids.
    def visitMasterOrBinaryLogsAndGtids(self, ctx:MySQLParser.MasterOrBinaryLogsAndGtidsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#sourceResetOptions.
    def visitSourceResetOptions(self, ctx:MySQLParser.SourceResetOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#replicationLoad.
    def visitReplicationLoad(self, ctx:MySQLParser.ReplicationLoadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSource.
    def visitChangeReplicationSource(self, ctx:MySQLParser.ChangeReplicationSourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeSource.
    def visitChangeSource(self, ctx:MySQLParser.ChangeSourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#sourceDefinitions.
    def visitSourceDefinitions(self, ctx:MySQLParser.SourceDefinitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#sourceDefinition.
    def visitSourceDefinition(self, ctx:MySQLParser.SourceDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceAutoPosition.
    def visitChangeReplicationSourceAutoPosition(self, ctx:MySQLParser.ChangeReplicationSourceAutoPositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceHost.
    def visitChangeReplicationSourceHost(self, ctx:MySQLParser.ChangeReplicationSourceHostContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceBind.
    def visitChangeReplicationSourceBind(self, ctx:MySQLParser.ChangeReplicationSourceBindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceUser.
    def visitChangeReplicationSourceUser(self, ctx:MySQLParser.ChangeReplicationSourceUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourcePassword.
    def visitChangeReplicationSourcePassword(self, ctx:MySQLParser.ChangeReplicationSourcePasswordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourcePort.
    def visitChangeReplicationSourcePort(self, ctx:MySQLParser.ChangeReplicationSourcePortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceConnectRetry.
    def visitChangeReplicationSourceConnectRetry(self, ctx:MySQLParser.ChangeReplicationSourceConnectRetryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceRetryCount.
    def visitChangeReplicationSourceRetryCount(self, ctx:MySQLParser.ChangeReplicationSourceRetryCountContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceDelay.
    def visitChangeReplicationSourceDelay(self, ctx:MySQLParser.ChangeReplicationSourceDelayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceSSL.
    def visitChangeReplicationSourceSSL(self, ctx:MySQLParser.ChangeReplicationSourceSSLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceSSLCA.
    def visitChangeReplicationSourceSSLCA(self, ctx:MySQLParser.ChangeReplicationSourceSSLCAContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceSSLCApath.
    def visitChangeReplicationSourceSSLCApath(self, ctx:MySQLParser.ChangeReplicationSourceSSLCApathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceSSLCipher.
    def visitChangeReplicationSourceSSLCipher(self, ctx:MySQLParser.ChangeReplicationSourceSSLCipherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceSSLCLR.
    def visitChangeReplicationSourceSSLCLR(self, ctx:MySQLParser.ChangeReplicationSourceSSLCLRContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceSSLCLRpath.
    def visitChangeReplicationSourceSSLCLRpath(self, ctx:MySQLParser.ChangeReplicationSourceSSLCLRpathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceSSLKey.
    def visitChangeReplicationSourceSSLKey(self, ctx:MySQLParser.ChangeReplicationSourceSSLKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceSSLVerifyServerCert.
    def visitChangeReplicationSourceSSLVerifyServerCert(self, ctx:MySQLParser.ChangeReplicationSourceSSLVerifyServerCertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceTLSVersion.
    def visitChangeReplicationSourceTLSVersion(self, ctx:MySQLParser.ChangeReplicationSourceTLSVersionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceTLSCiphersuites.
    def visitChangeReplicationSourceTLSCiphersuites(self, ctx:MySQLParser.ChangeReplicationSourceTLSCiphersuitesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceSSLCert.
    def visitChangeReplicationSourceSSLCert(self, ctx:MySQLParser.ChangeReplicationSourceSSLCertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourcePublicKey.
    def visitChangeReplicationSourcePublicKey(self, ctx:MySQLParser.ChangeReplicationSourcePublicKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceGetSourcePublicKey.
    def visitChangeReplicationSourceGetSourcePublicKey(self, ctx:MySQLParser.ChangeReplicationSourceGetSourcePublicKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceHeartbeatPeriod.
    def visitChangeReplicationSourceHeartbeatPeriod(self, ctx:MySQLParser.ChangeReplicationSourceHeartbeatPeriodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceCompressionAlgorithm.
    def visitChangeReplicationSourceCompressionAlgorithm(self, ctx:MySQLParser.ChangeReplicationSourceCompressionAlgorithmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplicationSourceZstdCompressionLevel.
    def visitChangeReplicationSourceZstdCompressionLevel(self, ctx:MySQLParser.ChangeReplicationSourceZstdCompressionLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#privilegeCheckDef.
    def visitPrivilegeCheckDef(self, ctx:MySQLParser.PrivilegeCheckDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tablePrimaryKeyCheckDef.
    def visitTablePrimaryKeyCheckDef(self, ctx:MySQLParser.TablePrimaryKeyCheckDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#assignGtidsToAnonymousTransactionsDefinition.
    def visitAssignGtidsToAnonymousTransactionsDefinition(self, ctx:MySQLParser.AssignGtidsToAnonymousTransactionsDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#sourceTlsCiphersuitesDef.
    def visitSourceTlsCiphersuitesDef(self, ctx:MySQLParser.SourceTlsCiphersuitesDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#sourceFileDef.
    def visitSourceFileDef(self, ctx:MySQLParser.SourceFileDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#sourceLogFile.
    def visitSourceLogFile(self, ctx:MySQLParser.SourceLogFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#sourceLogPos.
    def visitSourceLogPos(self, ctx:MySQLParser.SourceLogPosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#serverIdList.
    def visitServerIdList(self, ctx:MySQLParser.ServerIdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#changeReplication.
    def visitChangeReplication(self, ctx:MySQLParser.ChangeReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#filterDefinition.
    def visitFilterDefinition(self, ctx:MySQLParser.FilterDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#filterDbList.
    def visitFilterDbList(self, ctx:MySQLParser.FilterDbListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#filterTableList.
    def visitFilterTableList(self, ctx:MySQLParser.FilterTableListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#filterStringList.
    def visitFilterStringList(self, ctx:MySQLParser.FilterStringListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#filterWildDbTableString.
    def visitFilterWildDbTableString(self, ctx:MySQLParser.FilterWildDbTableStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#filterDbPairList.
    def visitFilterDbPairList(self, ctx:MySQLParser.FilterDbPairListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#startReplicaStatement.
    def visitStartReplicaStatement(self, ctx:MySQLParser.StartReplicaStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#stopReplicaStatement.
    def visitStopReplicaStatement(self, ctx:MySQLParser.StopReplicaStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#replicaUntil.
    def visitReplicaUntil(self, ctx:MySQLParser.ReplicaUntilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#userOption.
    def visitUserOption(self, ctx:MySQLParser.UserOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#passwordOption.
    def visitPasswordOption(self, ctx:MySQLParser.PasswordOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#defaultAuthOption.
    def visitDefaultAuthOption(self, ctx:MySQLParser.DefaultAuthOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#pluginDirOption.
    def visitPluginDirOption(self, ctx:MySQLParser.PluginDirOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#replicaThreadOptions.
    def visitReplicaThreadOptions(self, ctx:MySQLParser.ReplicaThreadOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#replicaThreadOption.
    def visitReplicaThreadOption(self, ctx:MySQLParser.ReplicaThreadOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#groupReplication.
    def visitGroupReplication(self, ctx:MySQLParser.GroupReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#groupReplicationStartOptions.
    def visitGroupReplicationStartOptions(self, ctx:MySQLParser.GroupReplicationStartOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#groupReplicationStartOption.
    def visitGroupReplicationStartOption(self, ctx:MySQLParser.GroupReplicationStartOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#groupReplicationUser.
    def visitGroupReplicationUser(self, ctx:MySQLParser.GroupReplicationUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#groupReplicationPassword.
    def visitGroupReplicationPassword(self, ctx:MySQLParser.GroupReplicationPasswordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#groupReplicationPluginAuth.
    def visitGroupReplicationPluginAuth(self, ctx:MySQLParser.GroupReplicationPluginAuthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#replica.
    def visitReplica(self, ctx:MySQLParser.ReplicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#preparedStatement.
    def visitPreparedStatement(self, ctx:MySQLParser.PreparedStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#executeStatement.
    def visitExecuteStatement(self, ctx:MySQLParser.ExecuteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#executeVarList.
    def visitExecuteVarList(self, ctx:MySQLParser.ExecuteVarListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#cloneStatement.
    def visitCloneStatement(self, ctx:MySQLParser.CloneStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dataDirSSL.
    def visitDataDirSSL(self, ctx:MySQLParser.DataDirSSLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#ssl.
    def visitSsl(self, ctx:MySQLParser.SslContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#accountManagementStatement.
    def visitAccountManagementStatement(self, ctx:MySQLParser.AccountManagementStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterUserStatement.
    def visitAlterUserStatement(self, ctx:MySQLParser.AlterUserStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterUserList.
    def visitAlterUserList(self, ctx:MySQLParser.AlterUserListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterUser.
    def visitAlterUser(self, ctx:MySQLParser.AlterUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#oldAlterUser.
    def visitOldAlterUser(self, ctx:MySQLParser.OldAlterUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#userFunction.
    def visitUserFunction(self, ctx:MySQLParser.UserFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createUserStatement.
    def visitCreateUserStatement(self, ctx:MySQLParser.CreateUserStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createUserTail.
    def visitCreateUserTail(self, ctx:MySQLParser.CreateUserTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#userAttributes.
    def visitUserAttributes(self, ctx:MySQLParser.UserAttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#defaultRoleClause.
    def visitDefaultRoleClause(self, ctx:MySQLParser.DefaultRoleClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#requireClause.
    def visitRequireClause(self, ctx:MySQLParser.RequireClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#connectOptions.
    def visitConnectOptions(self, ctx:MySQLParser.ConnectOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#accountLockPasswordExpireOptions.
    def visitAccountLockPasswordExpireOptions(self, ctx:MySQLParser.AccountLockPasswordExpireOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#userAttribute.
    def visitUserAttribute(self, ctx:MySQLParser.UserAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dropUserStatement.
    def visitDropUserStatement(self, ctx:MySQLParser.DropUserStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#grantStatement.
    def visitGrantStatement(self, ctx:MySQLParser.GrantStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#grantTargetList.
    def visitGrantTargetList(self, ctx:MySQLParser.GrantTargetListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#grantOptions.
    def visitGrantOptions(self, ctx:MySQLParser.GrantOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#exceptRoleList.
    def visitExceptRoleList(self, ctx:MySQLParser.ExceptRoleListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#withRoles.
    def visitWithRoles(self, ctx:MySQLParser.WithRolesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#grantAs.
    def visitGrantAs(self, ctx:MySQLParser.GrantAsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#versionedRequireClause.
    def visitVersionedRequireClause(self, ctx:MySQLParser.VersionedRequireClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#renameUserStatement.
    def visitRenameUserStatement(self, ctx:MySQLParser.RenameUserStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#revokeStatement.
    def visitRevokeStatement(self, ctx:MySQLParser.RevokeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#aclType.
    def visitAclType(self, ctx:MySQLParser.AclTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#roleOrPrivilegesList.
    def visitRoleOrPrivilegesList(self, ctx:MySQLParser.RoleOrPrivilegesListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#roleOrPrivilege.
    def visitRoleOrPrivilege(self, ctx:MySQLParser.RoleOrPrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#grantIdentifier.
    def visitGrantIdentifier(self, ctx:MySQLParser.GrantIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#requireList.
    def visitRequireList(self, ctx:MySQLParser.RequireListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#requireListElement.
    def visitRequireListElement(self, ctx:MySQLParser.RequireListElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#grantOption.
    def visitGrantOption(self, ctx:MySQLParser.GrantOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#setRoleStatement.
    def visitSetRoleStatement(self, ctx:MySQLParser.SetRoleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#roleList.
    def visitRoleList(self, ctx:MySQLParser.RoleListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#role.
    def visitRole(self, ctx:MySQLParser.RoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tableAdministrationStatement.
    def visitTableAdministrationStatement(self, ctx:MySQLParser.TableAdministrationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#histogramAutoUpdate.
    def visitHistogramAutoUpdate(self, ctx:MySQLParser.HistogramAutoUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#histogramUpdateParam.
    def visitHistogramUpdateParam(self, ctx:MySQLParser.HistogramUpdateParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#histogramNumBuckets.
    def visitHistogramNumBuckets(self, ctx:MySQLParser.HistogramNumBucketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#histogram.
    def visitHistogram(self, ctx:MySQLParser.HistogramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#checkOption.
    def visitCheckOption(self, ctx:MySQLParser.CheckOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#repairType.
    def visitRepairType(self, ctx:MySQLParser.RepairTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#uninstallStatement.
    def visitUninstallStatement(self, ctx:MySQLParser.UninstallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#installStatement.
    def visitInstallStatement(self, ctx:MySQLParser.InstallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#installOptionType.
    def visitInstallOptionType(self, ctx:MySQLParser.InstallOptionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#installSetRvalue.
    def visitInstallSetRvalue(self, ctx:MySQLParser.InstallSetRvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#installSetValue.
    def visitInstallSetValue(self, ctx:MySQLParser.InstallSetValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#installSetValueList.
    def visitInstallSetValueList(self, ctx:MySQLParser.InstallSetValueListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#setStatement.
    def visitSetStatement(self, ctx:MySQLParser.SetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#startOptionValueList.
    def visitStartOptionValueList(self, ctx:MySQLParser.StartOptionValueListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#transactionCharacteristics.
    def visitTransactionCharacteristics(self, ctx:MySQLParser.TransactionCharacteristicsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#transactionAccessMode.
    def visitTransactionAccessMode(self, ctx:MySQLParser.TransactionAccessModeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#isolationLevel.
    def visitIsolationLevel(self, ctx:MySQLParser.IsolationLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#optionValueListContinued.
    def visitOptionValueListContinued(self, ctx:MySQLParser.OptionValueListContinuedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#optionValueNoOptionType.
    def visitOptionValueNoOptionType(self, ctx:MySQLParser.OptionValueNoOptionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#optionValue.
    def visitOptionValue(self, ctx:MySQLParser.OptionValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#setSystemVariable.
    def visitSetSystemVariable(self, ctx:MySQLParser.SetSystemVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#startOptionValueListFollowingOptionType.
    def visitStartOptionValueListFollowingOptionType(self, ctx:MySQLParser.StartOptionValueListFollowingOptionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#optionValueFollowingOptionType.
    def visitOptionValueFollowingOptionType(self, ctx:MySQLParser.OptionValueFollowingOptionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#setExprOrDefault.
    def visitSetExprOrDefault(self, ctx:MySQLParser.SetExprOrDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showDatabasesStatement.
    def visitShowDatabasesStatement(self, ctx:MySQLParser.ShowDatabasesStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showTablesStatement.
    def visitShowTablesStatement(self, ctx:MySQLParser.ShowTablesStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showTriggersStatement.
    def visitShowTriggersStatement(self, ctx:MySQLParser.ShowTriggersStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showEventsStatement.
    def visitShowEventsStatement(self, ctx:MySQLParser.ShowEventsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showTableStatusStatement.
    def visitShowTableStatusStatement(self, ctx:MySQLParser.ShowTableStatusStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showOpenTablesStatement.
    def visitShowOpenTablesStatement(self, ctx:MySQLParser.ShowOpenTablesStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showParseTreeStatement.
    def visitShowParseTreeStatement(self, ctx:MySQLParser.ShowParseTreeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showPluginsStatement.
    def visitShowPluginsStatement(self, ctx:MySQLParser.ShowPluginsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showEngineLogsStatement.
    def visitShowEngineLogsStatement(self, ctx:MySQLParser.ShowEngineLogsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showEngineMutexStatement.
    def visitShowEngineMutexStatement(self, ctx:MySQLParser.ShowEngineMutexStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showEngineStatusStatement.
    def visitShowEngineStatusStatement(self, ctx:MySQLParser.ShowEngineStatusStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showColumnsStatement.
    def visitShowColumnsStatement(self, ctx:MySQLParser.ShowColumnsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showBinaryLogsStatement.
    def visitShowBinaryLogsStatement(self, ctx:MySQLParser.ShowBinaryLogsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showBinaryLogStatusStatement.
    def visitShowBinaryLogStatusStatement(self, ctx:MySQLParser.ShowBinaryLogStatusStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showReplicasStatement.
    def visitShowReplicasStatement(self, ctx:MySQLParser.ShowReplicasStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showBinlogEventsStatement.
    def visitShowBinlogEventsStatement(self, ctx:MySQLParser.ShowBinlogEventsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showRelaylogEventsStatement.
    def visitShowRelaylogEventsStatement(self, ctx:MySQLParser.ShowRelaylogEventsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showKeysStatement.
    def visitShowKeysStatement(self, ctx:MySQLParser.ShowKeysStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showEnginesStatement.
    def visitShowEnginesStatement(self, ctx:MySQLParser.ShowEnginesStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showCountWarningsStatement.
    def visitShowCountWarningsStatement(self, ctx:MySQLParser.ShowCountWarningsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showCountErrorsStatement.
    def visitShowCountErrorsStatement(self, ctx:MySQLParser.ShowCountErrorsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showWarningsStatement.
    def visitShowWarningsStatement(self, ctx:MySQLParser.ShowWarningsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showErrorsStatement.
    def visitShowErrorsStatement(self, ctx:MySQLParser.ShowErrorsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showProfilesStatement.
    def visitShowProfilesStatement(self, ctx:MySQLParser.ShowProfilesStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showProfileStatement.
    def visitShowProfileStatement(self, ctx:MySQLParser.ShowProfileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showStatusStatement.
    def visitShowStatusStatement(self, ctx:MySQLParser.ShowStatusStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showProcessListStatement.
    def visitShowProcessListStatement(self, ctx:MySQLParser.ShowProcessListStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showVariablesStatement.
    def visitShowVariablesStatement(self, ctx:MySQLParser.ShowVariablesStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showCharacterSetStatement.
    def visitShowCharacterSetStatement(self, ctx:MySQLParser.ShowCharacterSetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showCollationStatement.
    def visitShowCollationStatement(self, ctx:MySQLParser.ShowCollationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showPrivilegesStatement.
    def visitShowPrivilegesStatement(self, ctx:MySQLParser.ShowPrivilegesStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showGrantsStatement.
    def visitShowGrantsStatement(self, ctx:MySQLParser.ShowGrantsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showCreateDatabaseStatement.
    def visitShowCreateDatabaseStatement(self, ctx:MySQLParser.ShowCreateDatabaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showCreateTableStatement.
    def visitShowCreateTableStatement(self, ctx:MySQLParser.ShowCreateTableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showCreateViewStatement.
    def visitShowCreateViewStatement(self, ctx:MySQLParser.ShowCreateViewStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showMasterStatusStatement.
    def visitShowMasterStatusStatement(self, ctx:MySQLParser.ShowMasterStatusStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showReplicaStatusStatement.
    def visitShowReplicaStatusStatement(self, ctx:MySQLParser.ShowReplicaStatusStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showCreateProcedureStatement.
    def visitShowCreateProcedureStatement(self, ctx:MySQLParser.ShowCreateProcedureStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showCreateFunctionStatement.
    def visitShowCreateFunctionStatement(self, ctx:MySQLParser.ShowCreateFunctionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showCreateTriggerStatement.
    def visitShowCreateTriggerStatement(self, ctx:MySQLParser.ShowCreateTriggerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showCreateProcedureStatusStatement.
    def visitShowCreateProcedureStatusStatement(self, ctx:MySQLParser.ShowCreateProcedureStatusStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showCreateFunctionStatusStatement.
    def visitShowCreateFunctionStatusStatement(self, ctx:MySQLParser.ShowCreateFunctionStatusStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showCreateProcedureCodeStatement.
    def visitShowCreateProcedureCodeStatement(self, ctx:MySQLParser.ShowCreateProcedureCodeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showCreateFunctionCodeStatement.
    def visitShowCreateFunctionCodeStatement(self, ctx:MySQLParser.ShowCreateFunctionCodeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showCreateEventStatement.
    def visitShowCreateEventStatement(self, ctx:MySQLParser.ShowCreateEventStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showCreateUserStatement.
    def visitShowCreateUserStatement(self, ctx:MySQLParser.ShowCreateUserStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#showCommandType.
    def visitShowCommandType(self, ctx:MySQLParser.ShowCommandTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#engineOrAll.
    def visitEngineOrAll(self, ctx:MySQLParser.EngineOrAllContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#fromOrIn.
    def visitFromOrIn(self, ctx:MySQLParser.FromOrInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#inDb.
    def visitInDb(self, ctx:MySQLParser.InDbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#profileDefinitions.
    def visitProfileDefinitions(self, ctx:MySQLParser.ProfileDefinitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#profileDefinition.
    def visitProfileDefinition(self, ctx:MySQLParser.ProfileDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#otherAdministrativeStatement.
    def visitOtherAdministrativeStatement(self, ctx:MySQLParser.OtherAdministrativeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#keyCacheListOrParts.
    def visitKeyCacheListOrParts(self, ctx:MySQLParser.KeyCacheListOrPartsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#keyCacheList.
    def visitKeyCacheList(self, ctx:MySQLParser.KeyCacheListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#assignToKeycache.
    def visitAssignToKeycache(self, ctx:MySQLParser.AssignToKeycacheContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#assignToKeycachePartition.
    def visitAssignToKeycachePartition(self, ctx:MySQLParser.AssignToKeycachePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#cacheKeyList.
    def visitCacheKeyList(self, ctx:MySQLParser.CacheKeyListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#keyUsageElement.
    def visitKeyUsageElement(self, ctx:MySQLParser.KeyUsageElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#keyUsageList.
    def visitKeyUsageList(self, ctx:MySQLParser.KeyUsageListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#flushOption.
    def visitFlushOption(self, ctx:MySQLParser.FlushOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#logType.
    def visitLogType(self, ctx:MySQLParser.LogTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#flushTables.
    def visitFlushTables(self, ctx:MySQLParser.FlushTablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#flushTablesOptions.
    def visitFlushTablesOptions(self, ctx:MySQLParser.FlushTablesOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#preloadTail.
    def visitPreloadTail(self, ctx:MySQLParser.PreloadTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#preloadList.
    def visitPreloadList(self, ctx:MySQLParser.PreloadListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#preloadKeys.
    def visitPreloadKeys(self, ctx:MySQLParser.PreloadKeysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#adminPartition.
    def visitAdminPartition(self, ctx:MySQLParser.AdminPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#resourceGroupManagement.
    def visitResourceGroupManagement(self, ctx:MySQLParser.ResourceGroupManagementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createResourceGroup.
    def visitCreateResourceGroup(self, ctx:MySQLParser.CreateResourceGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#resourceGroupVcpuList.
    def visitResourceGroupVcpuList(self, ctx:MySQLParser.ResourceGroupVcpuListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#vcpuNumOrRange.
    def visitVcpuNumOrRange(self, ctx:MySQLParser.VcpuNumOrRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#resourceGroupPriority.
    def visitResourceGroupPriority(self, ctx:MySQLParser.ResourceGroupPriorityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#resourceGroupEnableDisable.
    def visitResourceGroupEnableDisable(self, ctx:MySQLParser.ResourceGroupEnableDisableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#alterResourceGroup.
    def visitAlterResourceGroup(self, ctx:MySQLParser.AlterResourceGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#setResourceGroup.
    def visitSetResourceGroup(self, ctx:MySQLParser.SetResourceGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#threadIdList.
    def visitThreadIdList(self, ctx:MySQLParser.ThreadIdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dropResourceGroup.
    def visitDropResourceGroup(self, ctx:MySQLParser.DropResourceGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#utilityStatement.
    def visitUtilityStatement(self, ctx:MySQLParser.UtilityStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#describeStatement.
    def visitDescribeStatement(self, ctx:MySQLParser.DescribeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#explainStatement.
    def visitExplainStatement(self, ctx:MySQLParser.ExplainStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#explainOptions.
    def visitExplainOptions(self, ctx:MySQLParser.ExplainOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#explainableStatement.
    def visitExplainableStatement(self, ctx:MySQLParser.ExplainableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#explainInto.
    def visitExplainInto(self, ctx:MySQLParser.ExplainIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#helpCommand.
    def visitHelpCommand(self, ctx:MySQLParser.HelpCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#useCommand.
    def visitUseCommand(self, ctx:MySQLParser.UseCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#restartServer.
    def visitRestartServer(self, ctx:MySQLParser.RestartServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#exprOr.
    def visitExprOr(self, ctx:MySQLParser.ExprOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#exprNot.
    def visitExprNot(self, ctx:MySQLParser.ExprNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#exprIs.
    def visitExprIs(self, ctx:MySQLParser.ExprIsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#exprAnd.
    def visitExprAnd(self, ctx:MySQLParser.ExprAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#exprXor.
    def visitExprXor(self, ctx:MySQLParser.ExprXorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#primaryExprPredicate.
    def visitPrimaryExprPredicate(self, ctx:MySQLParser.PrimaryExprPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#primaryExprCompare.
    def visitPrimaryExprCompare(self, ctx:MySQLParser.PrimaryExprCompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#primaryExprAllAny.
    def visitPrimaryExprAllAny(self, ctx:MySQLParser.PrimaryExprAllAnyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#primaryExprIsNull.
    def visitPrimaryExprIsNull(self, ctx:MySQLParser.PrimaryExprIsNullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#compOp.
    def visitCompOp(self, ctx:MySQLParser.CompOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#predicate.
    def visitPredicate(self, ctx:MySQLParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#predicateExprIn.
    def visitPredicateExprIn(self, ctx:MySQLParser.PredicateExprInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#predicateExprBetween.
    def visitPredicateExprBetween(self, ctx:MySQLParser.PredicateExprBetweenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#predicateExprLike.
    def visitPredicateExprLike(self, ctx:MySQLParser.PredicateExprLikeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#predicateExprRegex.
    def visitPredicateExprRegex(self, ctx:MySQLParser.PredicateExprRegexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#bitExpr.
    def visitBitExpr(self, ctx:MySQLParser.BitExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprConvert.
    def visitSimpleExprConvert(self, ctx:MySQLParser.SimpleExprConvertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprCast.
    def visitSimpleExprCast(self, ctx:MySQLParser.SimpleExprCastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprUnary.
    def visitSimpleExprUnary(self, ctx:MySQLParser.SimpleExprUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExpressionRValue.
    def visitSimpleExpressionRValue(self, ctx:MySQLParser.SimpleExpressionRValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprOdbc.
    def visitSimpleExprOdbc(self, ctx:MySQLParser.SimpleExprOdbcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprRuntimeFunction.
    def visitSimpleExprRuntimeFunction(self, ctx:MySQLParser.SimpleExprRuntimeFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprFunction.
    def visitSimpleExprFunction(self, ctx:MySQLParser.SimpleExprFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprCollate.
    def visitSimpleExprCollate(self, ctx:MySQLParser.SimpleExprCollateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprMatch.
    def visitSimpleExprMatch(self, ctx:MySQLParser.SimpleExprMatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprWindowingFunction.
    def visitSimpleExprWindowingFunction(self, ctx:MySQLParser.SimpleExprWindowingFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprBinary.
    def visitSimpleExprBinary(self, ctx:MySQLParser.SimpleExprBinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprColumnRef.
    def visitSimpleExprColumnRef(self, ctx:MySQLParser.SimpleExprColumnRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprParamMarker.
    def visitSimpleExprParamMarker(self, ctx:MySQLParser.SimpleExprParamMarkerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprSum.
    def visitSimpleExprSum(self, ctx:MySQLParser.SimpleExprSumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprCastTime.
    def visitSimpleExprCastTime(self, ctx:MySQLParser.SimpleExprCastTimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprConvertUsing.
    def visitSimpleExprConvertUsing(self, ctx:MySQLParser.SimpleExprConvertUsingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprSubQuery.
    def visitSimpleExprSubQuery(self, ctx:MySQLParser.SimpleExprSubQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprGroupingOperation.
    def visitSimpleExprGroupingOperation(self, ctx:MySQLParser.SimpleExprGroupingOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprNot.
    def visitSimpleExprNot(self, ctx:MySQLParser.SimpleExprNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprValues.
    def visitSimpleExprValues(self, ctx:MySQLParser.SimpleExprValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprUserVariableAssignment.
    def visitSimpleExprUserVariableAssignment(self, ctx:MySQLParser.SimpleExprUserVariableAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprDefault.
    def visitSimpleExprDefault(self, ctx:MySQLParser.SimpleExprDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprList.
    def visitSimpleExprList(self, ctx:MySQLParser.SimpleExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprInterval.
    def visitSimpleExprInterval(self, ctx:MySQLParser.SimpleExprIntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprCase.
    def visitSimpleExprCase(self, ctx:MySQLParser.SimpleExprCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprConcat.
    def visitSimpleExprConcat(self, ctx:MySQLParser.SimpleExprConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprLiteral.
    def visitSimpleExprLiteral(self, ctx:MySQLParser.SimpleExprLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#arrayCast.
    def visitArrayCast(self, ctx:MySQLParser.ArrayCastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#jsonOperator.
    def visitJsonOperator(self, ctx:MySQLParser.JsonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#sumExpr.
    def visitSumExpr(self, ctx:MySQLParser.SumExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#groupingOperation.
    def visitGroupingOperation(self, ctx:MySQLParser.GroupingOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#windowFunctionCall.
    def visitWindowFunctionCall(self, ctx:MySQLParser.WindowFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#samplingMethod.
    def visitSamplingMethod(self, ctx:MySQLParser.SamplingMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#samplingPercentage.
    def visitSamplingPercentage(self, ctx:MySQLParser.SamplingPercentageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tablesampleClause.
    def visitTablesampleClause(self, ctx:MySQLParser.TablesampleClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#windowingClause.
    def visitWindowingClause(self, ctx:MySQLParser.WindowingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#leadLagInfo.
    def visitLeadLagInfo(self, ctx:MySQLParser.LeadLagInfoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#stableInteger.
    def visitStableInteger(self, ctx:MySQLParser.StableIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#paramOrVar.
    def visitParamOrVar(self, ctx:MySQLParser.ParamOrVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#nullTreatment.
    def visitNullTreatment(self, ctx:MySQLParser.NullTreatmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#jsonFunction.
    def visitJsonFunction(self, ctx:MySQLParser.JsonFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#inSumExpr.
    def visitInSumExpr(self, ctx:MySQLParser.InSumExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#identListArg.
    def visitIdentListArg(self, ctx:MySQLParser.IdentListArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#identList.
    def visitIdentList(self, ctx:MySQLParser.IdentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#fulltextOptions.
    def visitFulltextOptions(self, ctx:MySQLParser.FulltextOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#runtimeFunctionCall.
    def visitRuntimeFunctionCall(self, ctx:MySQLParser.RuntimeFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#returningType.
    def visitReturningType(self, ctx:MySQLParser.ReturningTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#geometryFunction.
    def visitGeometryFunction(self, ctx:MySQLParser.GeometryFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#timeFunctionParameters.
    def visitTimeFunctionParameters(self, ctx:MySQLParser.TimeFunctionParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#fractionalPrecision.
    def visitFractionalPrecision(self, ctx:MySQLParser.FractionalPrecisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#weightStringLevels.
    def visitWeightStringLevels(self, ctx:MySQLParser.WeightStringLevelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#weightStringLevelListItem.
    def visitWeightStringLevelListItem(self, ctx:MySQLParser.WeightStringLevelListItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dateTimeTtype.
    def visitDateTimeTtype(self, ctx:MySQLParser.DateTimeTtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#trimFunction.
    def visitTrimFunction(self, ctx:MySQLParser.TrimFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#substringFunction.
    def visitSubstringFunction(self, ctx:MySQLParser.SubstringFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#functionCall.
    def visitFunctionCall(self, ctx:MySQLParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#udfExprList.
    def visitUdfExprList(self, ctx:MySQLParser.UdfExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#udfExpr.
    def visitUdfExpr(self, ctx:MySQLParser.UdfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#userVariable.
    def visitUserVariable(self, ctx:MySQLParser.UserVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#inExpressionUserVariableAssignment.
    def visitInExpressionUserVariableAssignment(self, ctx:MySQLParser.InExpressionUserVariableAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#rvalueSystemOrUserVariable.
    def visitRvalueSystemOrUserVariable(self, ctx:MySQLParser.RvalueSystemOrUserVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#lvalueVariable.
    def visitLvalueVariable(self, ctx:MySQLParser.LvalueVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#rvalueSystemVariable.
    def visitRvalueSystemVariable(self, ctx:MySQLParser.RvalueSystemVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#whenExpression.
    def visitWhenExpression(self, ctx:MySQLParser.WhenExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#thenExpression.
    def visitThenExpression(self, ctx:MySQLParser.ThenExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#elseExpression.
    def visitElseExpression(self, ctx:MySQLParser.ElseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#castType.
    def visitCastType(self, ctx:MySQLParser.CastTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#exprList.
    def visitExprList(self, ctx:MySQLParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#charset.
    def visitCharset(self, ctx:MySQLParser.CharsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#notRule.
    def visitNotRule(self, ctx:MySQLParser.NotRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#not2Rule.
    def visitNot2Rule(self, ctx:MySQLParser.Not2RuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#interval.
    def visitInterval(self, ctx:MySQLParser.IntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#intervalTimeStamp.
    def visitIntervalTimeStamp(self, ctx:MySQLParser.IntervalTimeStampContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#exprListWithParentheses.
    def visitExprListWithParentheses(self, ctx:MySQLParser.ExprListWithParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#exprWithParentheses.
    def visitExprWithParentheses(self, ctx:MySQLParser.ExprWithParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleExprWithParentheses.
    def visitSimpleExprWithParentheses(self, ctx:MySQLParser.SimpleExprWithParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#orderList.
    def visitOrderList(self, ctx:MySQLParser.OrderListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#orderExpression.
    def visitOrderExpression(self, ctx:MySQLParser.OrderExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#groupList.
    def visitGroupList(self, ctx:MySQLParser.GroupListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#groupingExpression.
    def visitGroupingExpression(self, ctx:MySQLParser.GroupingExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#channel.
    def visitChannel(self, ctx:MySQLParser.ChannelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#compoundStatement.
    def visitCompoundStatement(self, ctx:MySQLParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#returnStatement.
    def visitReturnStatement(self, ctx:MySQLParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#ifStatement.
    def visitIfStatement(self, ctx:MySQLParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#ifBody.
    def visitIfBody(self, ctx:MySQLParser.IfBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#thenStatement.
    def visitThenStatement(self, ctx:MySQLParser.ThenStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#compoundStatementList.
    def visitCompoundStatementList(self, ctx:MySQLParser.CompoundStatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#caseStatement.
    def visitCaseStatement(self, ctx:MySQLParser.CaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#elseStatement.
    def visitElseStatement(self, ctx:MySQLParser.ElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#labeledBlock.
    def visitLabeledBlock(self, ctx:MySQLParser.LabeledBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#unlabeledBlock.
    def visitUnlabeledBlock(self, ctx:MySQLParser.UnlabeledBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#label.
    def visitLabel(self, ctx:MySQLParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#beginEndBlock.
    def visitBeginEndBlock(self, ctx:MySQLParser.BeginEndBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#labeledControl.
    def visitLabeledControl(self, ctx:MySQLParser.LabeledControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#unlabeledControl.
    def visitUnlabeledControl(self, ctx:MySQLParser.UnlabeledControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#loopBlock.
    def visitLoopBlock(self, ctx:MySQLParser.LoopBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#whileDoBlock.
    def visitWhileDoBlock(self, ctx:MySQLParser.WhileDoBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#repeatUntilBlock.
    def visitRepeatUntilBlock(self, ctx:MySQLParser.RepeatUntilBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#spDeclarations.
    def visitSpDeclarations(self, ctx:MySQLParser.SpDeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#spDeclaration.
    def visitSpDeclaration(self, ctx:MySQLParser.SpDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:MySQLParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#conditionDeclaration.
    def visitConditionDeclaration(self, ctx:MySQLParser.ConditionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#spCondition.
    def visitSpCondition(self, ctx:MySQLParser.SpConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#sqlstate.
    def visitSqlstate(self, ctx:MySQLParser.SqlstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#handlerDeclaration.
    def visitHandlerDeclaration(self, ctx:MySQLParser.HandlerDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#handlerCondition.
    def visitHandlerCondition(self, ctx:MySQLParser.HandlerConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#cursorDeclaration.
    def visitCursorDeclaration(self, ctx:MySQLParser.CursorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#iterateStatement.
    def visitIterateStatement(self, ctx:MySQLParser.IterateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#leaveStatement.
    def visitLeaveStatement(self, ctx:MySQLParser.LeaveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#getDiagnosticsStatement.
    def visitGetDiagnosticsStatement(self, ctx:MySQLParser.GetDiagnosticsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#signalAllowedExpr.
    def visitSignalAllowedExpr(self, ctx:MySQLParser.SignalAllowedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#statementInformationItem.
    def visitStatementInformationItem(self, ctx:MySQLParser.StatementInformationItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#conditionInformationItem.
    def visitConditionInformationItem(self, ctx:MySQLParser.ConditionInformationItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#signalInformationItemName.
    def visitSignalInformationItemName(self, ctx:MySQLParser.SignalInformationItemNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#signalStatement.
    def visitSignalStatement(self, ctx:MySQLParser.SignalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#resignalStatement.
    def visitResignalStatement(self, ctx:MySQLParser.ResignalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#signalInformationItem.
    def visitSignalInformationItem(self, ctx:MySQLParser.SignalInformationItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#cursorOpen.
    def visitCursorOpen(self, ctx:MySQLParser.CursorOpenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#cursorClose.
    def visitCursorClose(self, ctx:MySQLParser.CursorCloseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#cursorFetch.
    def visitCursorFetch(self, ctx:MySQLParser.CursorFetchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#schedule.
    def visitSchedule(self, ctx:MySQLParser.ScheduleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#columnDefinition.
    def visitColumnDefinition(self, ctx:MySQLParser.ColumnDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#checkOrReferences.
    def visitCheckOrReferences(self, ctx:MySQLParser.CheckOrReferencesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#checkConstraint.
    def visitCheckConstraint(self, ctx:MySQLParser.CheckConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#constraintEnforcement.
    def visitConstraintEnforcement(self, ctx:MySQLParser.ConstraintEnforcementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tableConstraintDef.
    def visitTableConstraintDef(self, ctx:MySQLParser.TableConstraintDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#constraintName.
    def visitConstraintName(self, ctx:MySQLParser.ConstraintNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#fieldDefinition.
    def visitFieldDefinition(self, ctx:MySQLParser.FieldDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#columnAttribute.
    def visitColumnAttribute(self, ctx:MySQLParser.ColumnAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#columnFormat.
    def visitColumnFormat(self, ctx:MySQLParser.ColumnFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#storageMedia.
    def visitStorageMedia(self, ctx:MySQLParser.StorageMediaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#now.
    def visitNow(self, ctx:MySQLParser.NowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#nowOrSignedLiteral.
    def visitNowOrSignedLiteral(self, ctx:MySQLParser.NowOrSignedLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#gcolAttribute.
    def visitGcolAttribute(self, ctx:MySQLParser.GcolAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#references.
    def visitReferences(self, ctx:MySQLParser.ReferencesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#deleteOption.
    def visitDeleteOption(self, ctx:MySQLParser.DeleteOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#keyList.
    def visitKeyList(self, ctx:MySQLParser.KeyListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#keyPart.
    def visitKeyPart(self, ctx:MySQLParser.KeyPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#keyListWithExpression.
    def visitKeyListWithExpression(self, ctx:MySQLParser.KeyListWithExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#keyPartOrExpression.
    def visitKeyPartOrExpression(self, ctx:MySQLParser.KeyPartOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#indexType.
    def visitIndexType(self, ctx:MySQLParser.IndexTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#indexOption.
    def visitIndexOption(self, ctx:MySQLParser.IndexOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#commonIndexOption.
    def visitCommonIndexOption(self, ctx:MySQLParser.CommonIndexOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#visibility.
    def visitVisibility(self, ctx:MySQLParser.VisibilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#indexTypeClause.
    def visitIndexTypeClause(self, ctx:MySQLParser.IndexTypeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#fulltextIndexOption.
    def visitFulltextIndexOption(self, ctx:MySQLParser.FulltextIndexOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#spatialIndexOption.
    def visitSpatialIndexOption(self, ctx:MySQLParser.SpatialIndexOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dataTypeDefinition.
    def visitDataTypeDefinition(self, ctx:MySQLParser.DataTypeDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dataType.
    def visitDataType(self, ctx:MySQLParser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#nchar.
    def visitNchar(self, ctx:MySQLParser.NcharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#realType.
    def visitRealType(self, ctx:MySQLParser.RealTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#fieldLength.
    def visitFieldLength(self, ctx:MySQLParser.FieldLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#fieldOptions.
    def visitFieldOptions(self, ctx:MySQLParser.FieldOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#charsetWithOptBinary.
    def visitCharsetWithOptBinary(self, ctx:MySQLParser.CharsetWithOptBinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#ascii.
    def visitAscii(self, ctx:MySQLParser.AsciiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#unicode.
    def visitUnicode(self, ctx:MySQLParser.UnicodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#wsNumCodepoints.
    def visitWsNumCodepoints(self, ctx:MySQLParser.WsNumCodepointsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#typeDatetimePrecision.
    def visitTypeDatetimePrecision(self, ctx:MySQLParser.TypeDatetimePrecisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#functionDatetimePrecision.
    def visitFunctionDatetimePrecision(self, ctx:MySQLParser.FunctionDatetimePrecisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#charsetName.
    def visitCharsetName(self, ctx:MySQLParser.CharsetNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#collationName.
    def visitCollationName(self, ctx:MySQLParser.CollationNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createTableOptions.
    def visitCreateTableOptions(self, ctx:MySQLParser.CreateTableOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createTableOptionsEtc.
    def visitCreateTableOptionsEtc(self, ctx:MySQLParser.CreateTableOptionsEtcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createPartitioningEtc.
    def visitCreatePartitioningEtc(self, ctx:MySQLParser.CreatePartitioningEtcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createTableOptionsSpaceSeparated.
    def visitCreateTableOptionsSpaceSeparated(self, ctx:MySQLParser.CreateTableOptionsSpaceSeparatedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createTableOption.
    def visitCreateTableOption(self, ctx:MySQLParser.CreateTableOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#ternaryOption.
    def visitTernaryOption(self, ctx:MySQLParser.TernaryOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#defaultCollation.
    def visitDefaultCollation(self, ctx:MySQLParser.DefaultCollationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#defaultEncryption.
    def visitDefaultEncryption(self, ctx:MySQLParser.DefaultEncryptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#defaultCharset.
    def visitDefaultCharset(self, ctx:MySQLParser.DefaultCharsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#partitionClause.
    def visitPartitionClause(self, ctx:MySQLParser.PartitionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#partitionDefKey.
    def visitPartitionDefKey(self, ctx:MySQLParser.PartitionDefKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#partitionDefHash.
    def visitPartitionDefHash(self, ctx:MySQLParser.PartitionDefHashContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#partitionDefRangeList.
    def visitPartitionDefRangeList(self, ctx:MySQLParser.PartitionDefRangeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#subPartitions.
    def visitSubPartitions(self, ctx:MySQLParser.SubPartitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#partitionKeyAlgorithm.
    def visitPartitionKeyAlgorithm(self, ctx:MySQLParser.PartitionKeyAlgorithmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#partitionDefinitions.
    def visitPartitionDefinitions(self, ctx:MySQLParser.PartitionDefinitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#partitionDefinition.
    def visitPartitionDefinition(self, ctx:MySQLParser.PartitionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#partitionValuesIn.
    def visitPartitionValuesIn(self, ctx:MySQLParser.PartitionValuesInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#partitionOption.
    def visitPartitionOption(self, ctx:MySQLParser.PartitionOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#subpartitionDefinition.
    def visitSubpartitionDefinition(self, ctx:MySQLParser.SubpartitionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#partitionValueItemListParen.
    def visitPartitionValueItemListParen(self, ctx:MySQLParser.PartitionValueItemListParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#partitionValueItem.
    def visitPartitionValueItem(self, ctx:MySQLParser.PartitionValueItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#definerClause.
    def visitDefinerClause(self, ctx:MySQLParser.DefinerClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#ifExists.
    def visitIfExists(self, ctx:MySQLParser.IfExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#ifExistsIdentifier.
    def visitIfExistsIdentifier(self, ctx:MySQLParser.IfExistsIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#persistedVariableIdentifier.
    def visitPersistedVariableIdentifier(self, ctx:MySQLParser.PersistedVariableIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#ifNotExists.
    def visitIfNotExists(self, ctx:MySQLParser.IfNotExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#ignoreUnknownUser.
    def visitIgnoreUnknownUser(self, ctx:MySQLParser.IgnoreUnknownUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#procedureParameter.
    def visitProcedureParameter(self, ctx:MySQLParser.ProcedureParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#functionParameter.
    def visitFunctionParameter(self, ctx:MySQLParser.FunctionParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#collate.
    def visitCollate(self, ctx:MySQLParser.CollateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#typeWithOptCollate.
    def visitTypeWithOptCollate(self, ctx:MySQLParser.TypeWithOptCollateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#schemaIdentifierPair.
    def visitSchemaIdentifierPair(self, ctx:MySQLParser.SchemaIdentifierPairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#viewRefList.
    def visitViewRefList(self, ctx:MySQLParser.ViewRefListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#updateList.
    def visitUpdateList(self, ctx:MySQLParser.UpdateListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#updateElement.
    def visitUpdateElement(self, ctx:MySQLParser.UpdateElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#charsetClause.
    def visitCharsetClause(self, ctx:MySQLParser.CharsetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#fieldsClause.
    def visitFieldsClause(self, ctx:MySQLParser.FieldsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#fieldTerm.
    def visitFieldTerm(self, ctx:MySQLParser.FieldTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#linesClause.
    def visitLinesClause(self, ctx:MySQLParser.LinesClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#lineTerm.
    def visitLineTerm(self, ctx:MySQLParser.LineTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#userList.
    def visitUserList(self, ctx:MySQLParser.UserListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createUserList.
    def visitCreateUserList(self, ctx:MySQLParser.CreateUserListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createUser.
    def visitCreateUser(self, ctx:MySQLParser.CreateUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#createUserWithMfa.
    def visitCreateUserWithMfa(self, ctx:MySQLParser.CreateUserWithMfaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#identification.
    def visitIdentification(self, ctx:MySQLParser.IdentificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#identifiedByPassword.
    def visitIdentifiedByPassword(self, ctx:MySQLParser.IdentifiedByPasswordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#identifiedByRandomPassword.
    def visitIdentifiedByRandomPassword(self, ctx:MySQLParser.IdentifiedByRandomPasswordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#identifiedWithPlugin.
    def visitIdentifiedWithPlugin(self, ctx:MySQLParser.IdentifiedWithPluginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#identifiedWithPluginAsAuth.
    def visitIdentifiedWithPluginAsAuth(self, ctx:MySQLParser.IdentifiedWithPluginAsAuthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#identifiedWithPluginByPassword.
    def visitIdentifiedWithPluginByPassword(self, ctx:MySQLParser.IdentifiedWithPluginByPasswordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#identifiedWithPluginByRandomPassword.
    def visitIdentifiedWithPluginByRandomPassword(self, ctx:MySQLParser.IdentifiedWithPluginByRandomPasswordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#initialAuth.
    def visitInitialAuth(self, ctx:MySQLParser.InitialAuthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#retainCurrentPassword.
    def visitRetainCurrentPassword(self, ctx:MySQLParser.RetainCurrentPasswordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#discardOldPassword.
    def visitDiscardOldPassword(self, ctx:MySQLParser.DiscardOldPasswordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#userRegistration.
    def visitUserRegistration(self, ctx:MySQLParser.UserRegistrationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#factor.
    def visitFactor(self, ctx:MySQLParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#replacePassword.
    def visitReplacePassword(self, ctx:MySQLParser.ReplacePasswordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#userIdentifierOrText.
    def visitUserIdentifierOrText(self, ctx:MySQLParser.UserIdentifierOrTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#user.
    def visitUser(self, ctx:MySQLParser.UserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#likeClause.
    def visitLikeClause(self, ctx:MySQLParser.LikeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#likeOrWhere.
    def visitLikeOrWhere(self, ctx:MySQLParser.LikeOrWhereContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#onlineOption.
    def visitOnlineOption(self, ctx:MySQLParser.OnlineOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#noWriteToBinLog.
    def visitNoWriteToBinLog(self, ctx:MySQLParser.NoWriteToBinLogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#usePartition.
    def visitUsePartition(self, ctx:MySQLParser.UsePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#fieldIdentifier.
    def visitFieldIdentifier(self, ctx:MySQLParser.FieldIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#columnName.
    def visitColumnName(self, ctx:MySQLParser.ColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#columnInternalRef.
    def visitColumnInternalRef(self, ctx:MySQLParser.ColumnInternalRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#columnInternalRefList.
    def visitColumnInternalRefList(self, ctx:MySQLParser.ColumnInternalRefListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#columnRef.
    def visitColumnRef(self, ctx:MySQLParser.ColumnRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#insertIdentifier.
    def visitInsertIdentifier(self, ctx:MySQLParser.InsertIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#indexName.
    def visitIndexName(self, ctx:MySQLParser.IndexNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#indexRef.
    def visitIndexRef(self, ctx:MySQLParser.IndexRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tableWild.
    def visitTableWild(self, ctx:MySQLParser.TableWildContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#schemaName.
    def visitSchemaName(self, ctx:MySQLParser.SchemaNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#schemaRef.
    def visitSchemaRef(self, ctx:MySQLParser.SchemaRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#procedureName.
    def visitProcedureName(self, ctx:MySQLParser.ProcedureNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#procedureRef.
    def visitProcedureRef(self, ctx:MySQLParser.ProcedureRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#functionName.
    def visitFunctionName(self, ctx:MySQLParser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#functionRef.
    def visitFunctionRef(self, ctx:MySQLParser.FunctionRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#triggerName.
    def visitTriggerName(self, ctx:MySQLParser.TriggerNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#triggerRef.
    def visitTriggerRef(self, ctx:MySQLParser.TriggerRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#viewName.
    def visitViewName(self, ctx:MySQLParser.ViewNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#viewRef.
    def visitViewRef(self, ctx:MySQLParser.ViewRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tablespaceName.
    def visitTablespaceName(self, ctx:MySQLParser.TablespaceNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tablespaceRef.
    def visitTablespaceRef(self, ctx:MySQLParser.TablespaceRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#logfileGroupName.
    def visitLogfileGroupName(self, ctx:MySQLParser.LogfileGroupNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#logfileGroupRef.
    def visitLogfileGroupRef(self, ctx:MySQLParser.LogfileGroupRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#eventName.
    def visitEventName(self, ctx:MySQLParser.EventNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#eventRef.
    def visitEventRef(self, ctx:MySQLParser.EventRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#udfName.
    def visitUdfName(self, ctx:MySQLParser.UdfNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#serverName.
    def visitServerName(self, ctx:MySQLParser.ServerNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#serverRef.
    def visitServerRef(self, ctx:MySQLParser.ServerRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#engineRef.
    def visitEngineRef(self, ctx:MySQLParser.EngineRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tableName.
    def visitTableName(self, ctx:MySQLParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#filterTableRef.
    def visitFilterTableRef(self, ctx:MySQLParser.FilterTableRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tableRefWithWildcard.
    def visitTableRefWithWildcard(self, ctx:MySQLParser.TableRefWithWildcardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tableRef.
    def visitTableRef(self, ctx:MySQLParser.TableRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tableRefList.
    def visitTableRefList(self, ctx:MySQLParser.TableRefListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tableAliasRefList.
    def visitTableAliasRefList(self, ctx:MySQLParser.TableAliasRefListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#parameterName.
    def visitParameterName(self, ctx:MySQLParser.ParameterNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#labelIdentifier.
    def visitLabelIdentifier(self, ctx:MySQLParser.LabelIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#labelRef.
    def visitLabelRef(self, ctx:MySQLParser.LabelRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#roleIdentifier.
    def visitRoleIdentifier(self, ctx:MySQLParser.RoleIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#pluginRef.
    def visitPluginRef(self, ctx:MySQLParser.PluginRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#componentRef.
    def visitComponentRef(self, ctx:MySQLParser.ComponentRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#resourceGroupRef.
    def visitResourceGroupRef(self, ctx:MySQLParser.ResourceGroupRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#windowName.
    def visitWindowName(self, ctx:MySQLParser.WindowNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#pureIdentifier.
    def visitPureIdentifier(self, ctx:MySQLParser.PureIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#identifier.
    def visitIdentifier(self, ctx:MySQLParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#identifierList.
    def visitIdentifierList(self, ctx:MySQLParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#identifierListWithParentheses.
    def visitIdentifierListWithParentheses(self, ctx:MySQLParser.IdentifierListWithParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#qualifiedIdentifier.
    def visitQualifiedIdentifier(self, ctx:MySQLParser.QualifiedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simpleIdentifier.
    def visitSimpleIdentifier(self, ctx:MySQLParser.SimpleIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#dotIdentifier.
    def visitDotIdentifier(self, ctx:MySQLParser.DotIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#ulong_number.
    def visitUlong_number(self, ctx:MySQLParser.Ulong_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#real_ulong_number.
    def visitReal_ulong_number(self, ctx:MySQLParser.Real_ulong_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#ulonglongNumber.
    def visitUlonglongNumber(self, ctx:MySQLParser.UlonglongNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#real_ulonglong_number.
    def visitReal_ulonglong_number(self, ctx:MySQLParser.Real_ulonglong_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#signedLiteral.
    def visitSignedLiteral(self, ctx:MySQLParser.SignedLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#signedLiteralOrNull.
    def visitSignedLiteralOrNull(self, ctx:MySQLParser.SignedLiteralOrNullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#literal.
    def visitLiteral(self, ctx:MySQLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#literalOrNull.
    def visitLiteralOrNull(self, ctx:MySQLParser.LiteralOrNullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#nullAsLiteral.
    def visitNullAsLiteral(self, ctx:MySQLParser.NullAsLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#stringList.
    def visitStringList(self, ctx:MySQLParser.StringListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#textStringLiteral.
    def visitTextStringLiteral(self, ctx:MySQLParser.TextStringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#textString.
    def visitTextString(self, ctx:MySQLParser.TextStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#textStringHash.
    def visitTextStringHash(self, ctx:MySQLParser.TextStringHashContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#textLiteral.
    def visitTextLiteral(self, ctx:MySQLParser.TextLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#textStringNoLinebreak.
    def visitTextStringNoLinebreak(self, ctx:MySQLParser.TextStringNoLinebreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#textStringLiteralList.
    def visitTextStringLiteralList(self, ctx:MySQLParser.TextStringLiteralListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#numLiteral.
    def visitNumLiteral(self, ctx:MySQLParser.NumLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#boolLiteral.
    def visitBoolLiteral(self, ctx:MySQLParser.BoolLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#nullLiteral.
    def visitNullLiteral(self, ctx:MySQLParser.NullLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#int64Literal.
    def visitInt64Literal(self, ctx:MySQLParser.Int64LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#temporalLiteral.
    def visitTemporalLiteral(self, ctx:MySQLParser.TemporalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#floatOptions.
    def visitFloatOptions(self, ctx:MySQLParser.FloatOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#standardFloatOptions.
    def visitStandardFloatOptions(self, ctx:MySQLParser.StandardFloatOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#precision.
    def visitPrecision(self, ctx:MySQLParser.PrecisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#textOrIdentifier.
    def visitTextOrIdentifier(self, ctx:MySQLParser.TextOrIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#lValueIdentifier.
    def visitLValueIdentifier(self, ctx:MySQLParser.LValueIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#roleIdentifierOrText.
    def visitRoleIdentifierOrText(self, ctx:MySQLParser.RoleIdentifierOrTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#sizeNumber.
    def visitSizeNumber(self, ctx:MySQLParser.SizeNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#parentheses.
    def visitParentheses(self, ctx:MySQLParser.ParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#equal.
    def visitEqual(self, ctx:MySQLParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#optionType.
    def visitOptionType(self, ctx:MySQLParser.OptionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#rvalueSystemVariableType.
    def visitRvalueSystemVariableType(self, ctx:MySQLParser.RvalueSystemVariableTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#setVarIdentType.
    def visitSetVarIdentType(self, ctx:MySQLParser.SetVarIdentTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#jsonAttribute.
    def visitJsonAttribute(self, ctx:MySQLParser.JsonAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#identifierKeyword.
    def visitIdentifierKeyword(self, ctx:MySQLParser.IdentifierKeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#identifierKeywordsAmbiguous1RolesAndLabels.
    def visitIdentifierKeywordsAmbiguous1RolesAndLabels(self, ctx:MySQLParser.IdentifierKeywordsAmbiguous1RolesAndLabelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#identifierKeywordsAmbiguous2Labels.
    def visitIdentifierKeywordsAmbiguous2Labels(self, ctx:MySQLParser.IdentifierKeywordsAmbiguous2LabelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#labelKeyword.
    def visitLabelKeyword(self, ctx:MySQLParser.LabelKeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#identifierKeywordsAmbiguous3Roles.
    def visitIdentifierKeywordsAmbiguous3Roles(self, ctx:MySQLParser.IdentifierKeywordsAmbiguous3RolesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#identifierKeywordsUnambiguous.
    def visitIdentifierKeywordsUnambiguous(self, ctx:MySQLParser.IdentifierKeywordsUnambiguousContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#roleKeyword.
    def visitRoleKeyword(self, ctx:MySQLParser.RoleKeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#lValueKeyword.
    def visitLValueKeyword(self, ctx:MySQLParser.LValueKeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#identifierKeywordsAmbiguous4SystemVariables.
    def visitIdentifierKeywordsAmbiguous4SystemVariables(self, ctx:MySQLParser.IdentifierKeywordsAmbiguous4SystemVariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#roleOrIdentifierKeyword.
    def visitRoleOrIdentifierKeyword(self, ctx:MySQLParser.RoleOrIdentifierKeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#roleOrLabelKeyword.
    def visitRoleOrLabelKeyword(self, ctx:MySQLParser.RoleOrLabelKeywordContext):
        return self.visitChildren(ctx)



del MySQLParser