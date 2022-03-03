from django.db import models


class Card(models.Model):

    """
    Create card model for
    """

    name = models.CharField(max_length=100, verbose_name='Название')
    info = models.TextField(null=True, blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to=None)
    user = models.ForeignKey('UserCustom', null=False, on_delete=models.PROTECT, related_name='User',
                             verbose_name='Добавил пользователь')
    status = models.ForeignKey('Status', null=False, on_delete=models.PROTECT, related_name='Status',
                             verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Карточка'
        verbose_name = 'Карточка'
        ordering = ['name']


class Status(models.Model):

    NOT_STARTED = 'NOT_S'
    DONE = 'DONE'
    IN_DEVELOPMENT = 'IN_DEV'
    STATUS_CHOICES = [
        (NOT_STARTED, 'Not started'),
        (DONE, 'Done'),
        (IN_DEVELOPMENT, 'In development: '),
    ]

    status = models.CharField(
        max_length=6,
        choices=STATUS_CHOICES,
        default=NOT_STARTED,
    )
    dev = models.ManyToManyField('UserCustom', null=che, related_name='Пользователи',
                                                         verbose_name='Пользователи')

    @classmethod
    def create(cls, stat):
        status = cls(status=stat, dev=models.ManyToManyField(null=checkStat(stat)))
        return status

    def __str__(self):
        return self.status + ' '.join([str(elem) for elem in self.dev])

    #def addedDevelopers(status: String) -> list:
    #    if (status != 'NOT_S'):
    #        return {'dev1','dev2'}
    #    else:
    #        return {}


    def checkStat(status:String) -> Boolean:
        return True if status != 'NOT_S' else False



    class Meta:
        verbose_name_plural = 'Статус'
        verbose_name = 'Статус'
        ordering = ['status']