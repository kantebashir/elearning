from .models import Lesson


def get_Lessons():
    return Lesson.objects.all()

def get_Lesson():
    return Lesson.objects.get()    