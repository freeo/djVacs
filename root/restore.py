from django.contrib.sessions.models import Session

sessions = Session.objects.all()
s_dec = []
for session in sessions:
    s_dec.append(session.get_decoded())

file = open("restoresessions.txt", "w")
for s in s_dec:
    file.write(str(s))
    file.write('\n')
file.close()

