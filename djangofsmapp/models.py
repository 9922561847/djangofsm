'''
purpose: creating workflow using django_fsm
author: Pratiksha Mali
Date  : 04 April 2021

'''
from django.db import models
from django_fsm import FSMField,transition

STATES = ['Open','In Progress','Resolved','Re Opened','Closed']

class Task(models.Model):
    '''
    this class defined to understand workflow
    FSMState is defined here.
    '''
    title = models.CharField(max_length=100, null=False)
    description = models.TextField()
    state = FSMField(default=STATES[0],choices=STATES)


    #source: source parameter accepts a list of states or individual state.
    #field : this parameter accepts both the string attribute name or the actual firld instance.

    @transition(field=state,source=['Open','Re Opened'],target='In Progress')
    def start(self):
        '''
        This method contain the action needs to take once state is changed.
        it will notify users.
        '''
        task = Task.objects.get(pk=task_id)
        task.start()
        task.save()

    @transition(field=state,source='In Progress',target='Resolved')
    def resolve(self):
        '''
        This method contain the action needs to take once state is changed to Inprogress to Resolved

        '''
        pass

    #Adding conditions on Transitions
    @transition(field=state,source='Resolved',target='Closed',conditions['can_close'])
    def close(self):
        """
        This method will contain the action that needs to be taken once the state is changed
        """
        pass