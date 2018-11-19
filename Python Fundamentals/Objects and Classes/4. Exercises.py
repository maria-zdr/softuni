class Exercise:
    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems = problems


list_exercises = []

while True:
    data = input()
    if data == 'go go go':
        break

    list_data = data.split(' -> ')
    exercise = Exercise(list_data[0], list_data[1], list_data[2], list_data[3].split(', '))
    list_exercises.append(exercise)

for item in list_exercises:
    print('Exercises: {}'.format(item.topic))
    print('Problems for exercises and homework for the "{}" course @ SoftUni.'.format(item.course_name))
    print('Check your solutions here: {}'.format(item.judge_contest_link))
    for i in range(0, len(item.problems)):
        print('{}. {}'.format(i + 1, item.problems[i]))