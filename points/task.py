from __future__ import absolute_import

from celery import shared_task

from geosolutions import celery_app
from time import sleep

from .models import History, RefernceTable, Result

@celery_app.task()
def calculate_distance(History entry):
    all_points = [[a.x,a.y], for a in RefernceTable.objects.all()]
    origin = [entry.x,entry.y]
    number_of_points = entry.n

    print(len(all_points))
    q = Result()
    q.number_points = number_of_points
    q.points_list = get_nearest_n_points(all_points, origin, number_of_points)
    q.save()
    entry.result_id = q
    return q

def get_nearest_n_points(points, origin, n):
    points.sort(key=lambda x: (x[0]-origin[0])**2 + (x[1] - origin[1])**2)
    return points[:n]

@shared_task
def test(param):
    return 'The test task executed with argument "%s" ' % param


@celery_app.task()
def UploadTask(message):

    # Update the state. The meta data is available in task.info dicttionary
    # The meta data is useful to store relevant information to the task
    # Here we are storing the upload progress in the meta. 

    UploadTask.update_state(state='PROGRESS', meta={'progress': 0})
    sleep(30)
    UploadTask.update_state(state='PROGRESS', meta={'progress': 30})
    sleep(30)
    return message


def get_task_status(task_id):

    # If you have a task_id, this is how you query that task 
    task = UploadTask.AsyncResult(task_id)

    status = task.status
    progress = 0

    if status == u'SUCCESS':
        progress = 100
    elif status == u'FAILURE':
        progress = 0
    elif status == 'PROGRESS':
        progress = task.info['progress']

    return {'status': status, 'progress': progress}