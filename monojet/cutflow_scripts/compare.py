import sys

fi1N,fi2N = sys.argv[1],sys.argv[2]

fi1 = open(fi1N)
fi2 = open(fi2N)

events1 = [line.split() for line in fi1.readlines()]
events2 = [line.split() for line in fi2.readlines()]
events1 = filter(lambda x: len(x), events1)
events2 = filter(lambda x: len(x), events2)

events_1_in_2 = filter(lambda x: x not in events2,events1)
#events_1_in_2 = filter(lambda x: x in events2,events1)
totalevents = events1+events2
totalevents = filter(lambda x: x in events_1_in_2,totalevents)
#totalevents = filter(lambda x: x not in events_1_in_2,totalevents)
totalevents += events_1_in_2

numoverlaps = len(events_1_in_2)
numtotal    = len(totalevents)

for ev in events_1_in_2: print ev
print " Total events = ", numtotal
print " Found %d overlapping events between %s and %s (%g %%)"%(numoverlaps, fi1N, fi2N,100*float(numoverlaps)/numtotal)
