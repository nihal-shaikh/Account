# Account
1. class account
2. class account is extended in currentaccount class and savingsaccount class. thus making the variables and funtions of the parent class(account)  accessible to the sub classes(currentaccount and savingsaccount).
3. define a constructor or initiator function __init__ with and object self and to additional parameters account number and balance. which will store the account number and balance corresponding to that object.
4. define deposit() and passing the amount parameter which will add the amount in the balance variable and will update the balance of the corresponding object.
5. define __str__() which represents a string in an informal manner. and here it is used to display the accountno and the balance of the corresponding object.

1. class currentaccount
2. the class current account is passing a class argument which is account
3. where we create an instance of class account by defining __init__() and and passing accountno argument which is fetched from the parent class.
4. define withdraw with arguments amount to perform withdrawal of money form currentaccount
5. if the amount is entered is greater than available balance or the balance goes below the minimum balance i.e 15000 then display insufficient balance
6. else deduct the amount from the balance along with 0.1 extra charge of the amount and display the update balance.

1. class savingsaccount
2. in class savings it is the same process as in the currentaccount on difference is that there is no extra charge levied and the minimum balance requirement is set to 1000.

