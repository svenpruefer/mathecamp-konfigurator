from mathecamp_konfigurator.mktypes import Expense


################
# Sample Cases #
################

def getExpenseExample():
    return (Expense("Garn", 20, [1, 2], False), {"name": "Garn", "amount": 20, "usage": [1, 2], "payedAlready": False})


#####################
# Constructor tests #
#####################

def test_expenseConstructorAndToDict():
    (expense, expenseDict) = getExpenseExample()
    assert (expense.toDict() == expenseDict)


####################
# Dictionary tests #
####################

def test_expenseToDictAndFromDict():
    expenseDictionary = getExpenseExample()[1]
    assert (Expense.fromDict(expenseDictionary).toDict() == expenseDictionary)


###############
# Print tests #
###############

def test_expensePrint():
    expense = getExpenseExample()[0]
    assert (expense.__str__() == "Expense(Garn,20,[1, 2],False)")
