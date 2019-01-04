class StepData(object):
    def __init__(self, **kwargs):
        for field in ('id', 'date', 'type_name', 'value'):
            setattr(self, field, kwargs.get(field, None))
