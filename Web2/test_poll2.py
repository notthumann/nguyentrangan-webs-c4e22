from poll import Poll
import mlab
#1.Connect

mlab.connect()

#2.Read all
poll_list = Poll.objects() #page, lazy loading
for p in poll_list:
    print(p.question)
    print(p.options)
    print(p.code)

# p = poll_list[2]
# print(p.question)
# print(p.options)
# print(p.code)


