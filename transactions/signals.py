from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

from transactions.models import Transaction


@receiver(pre_delete, sender=Transaction)
def update_account_balance_on_delete(sender, instance: Transaction, **kwargs):
    account = instance.account
    if instance.category.type == 'income':
        account.balance -= instance.amount
    else:
        account.balance += instance.amount
    account.save()


@receiver(pre_save, sender=Transaction)
def update_account_balance_on_save_n_update(sender, instance: Transaction, **kwargs):
    related_account = instance.account

    # for first time creation
    if instance.pk:
        # first adjust the account balance as like previous values deleted
        prevInstance = Transaction.objects.get(pk=instance.pk)
        print(prevInstance)
        if prevInstance.category.type == 'income':
            related_account.balance -= prevInstance.amount
            related_account.balance += instance.amount
        elif prevInstance.category.type == 'expense':
            related_account.balance += prevInstance.amount
            related_account.balance -= instance.amount

        
    # when updating the transaction
    else:
        # adjust account balance with new values
        if instance.category.type == 'income':
            related_account.balance += instance.amount
        elif instance.category.type == 'expense':
            related_account.balance -= instance.amount

    related_account.save()