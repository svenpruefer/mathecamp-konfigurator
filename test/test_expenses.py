from src.mktypes import Expense


################
# Sample Cases #
################

def getExpenseExample():
    return (Expense("Garn", 20, [3, 8], False))


#####################
# Constructor tests #
#####################

def test_expenseConstructorAndToDict():
    expense = getExpenseExample()
    assert (expense.toDict() == {"name": "Garn", "amount": 20, "usage": [3, 8], "payedAlready": False})


####################
# Dictionary tests #
####################

def test_expenseToDictAndFromDict():
    expenseDictionary = {"name": "Garn", "amount": 20, "usage": [3, 8], "payedAlready": False}
    assert (Expense.fromDict(expenseDictionary).toDict() == expenseDictionary)


###############
# Print tests #
###############

def test_expensePrint():
    expense = getExpenseExample()
    assert (expense.__str__() == "Expense(Garn,20,[3, 8],False)")
