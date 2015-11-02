from model import *
import math
import random
import copy


def lo(curr_candidate_sol,d):
	return curr_candidate_sol.lowerRange[d]


def hi(curr_candidate_sol,d):
	return curr_candidate_sol.upperRange[d]


def decisions(curr_candidate_sol):
	return [_ for _ in xrange(curr_candidate_sol.numOfDec)]


def trim(curr_candidate_sol,x,d):
	# print "curr_candidate_sol:", curr_candidate_sol
	return max(lo(curr_candidate_sol,d), min(x,hi(curr_candidate_sol,d)))

	# max(7.3,min(7.3,8.3))


def n(max):
	return (random.uniform(0,max))

def score(curr_candidate_sol):
	f1,f2 = curr_candidate_sol.getobj()
	square = lambda val: math.pow(val,2)
	sq_root = lambda val: math.sqrt(val)
	dist_from_hell =sq_root(square(f1) + square(f2))
	return dist_from_hell


def get_min_max(model):
	min = 999999
	max = -999999
	for x in xrange(2000):
		temp_candidate_sol = model()
		temp_score = score(temp_candidate_sol)
		if(temp_score > max):
			max = temp_score
		if(temp_score < min):
			min = temp_score
	return (min,max)


class Thing():
	id = 0
	def __init__(self, **entries):
		self.id = Thing.id = Thing.id + 1
		self.__dict__.update(entries)

def candidate(curr_candidate_sol):
	curr_candidate_sol = model()
	curr_candidate_sol.decisionVec = [lo(curr_candidate_sol,d) + n(hi(curr_candidate_sol,d) - lo(curr_candidate_sol,d)) for d in decisions(curr_candidate_sol)]
	
	while (not curr_candidate_sol.check()):
		curr_candidate_sol.decisionVec = [lo(curr_candidate_sol,d) + n(hi(curr_candidate_sol,d) - lo(curr_candidate_sol,d)) for d in decisions(curr_candidate_sol)]

	new = Thing()
	new.have = curr_candidate_sol.decisionVec
	new.score = score(curr_candidate_sol)
	return new


def de(model, baseline_min,baseline_max, max = 100, f = 0.75, cf = 0.3, epsilon = 0.01):
	curr_candidate_sol = model()
	# print "FROM DE-->", curr_candidate_sol
	np = curr_candidate_sol.numOfDec * 10
	frontier = [candidate(curr_candidate_sol) for _ in xrange(np)]

	# for x in frontier:
	# 	print "id:", x.id, " have:", x.have, " score:", x.score

	# print "length of frontier:", len(frontier)

	for each_thing in frontier:
		if(each_thing.score < 0):
			baseline_min = 0
		if(each_thing.score < baseline_min):
			baseline_min = each_thing.score
		if(each_thing.score > baseline_max):
			baseline_max = each_thing.score



	#Normalize the scores of each thing now

	for each_thing in frontier:
		prev_each_thing_score = each_thing.score
		each_thing.score = float(each_thing.score - baseline_min)/(baseline_max - baseline_min)
	

	for k in xrange(max):
		total,n = update(f,cf,frontier,curr_candidate_sol,baseline_min,baseline_max)
		if total/n > (1 - epsilon):
			break
	# for x in frontier:
	# 	print "print --x:",x.id," ",x.have, x.score

	score_have_dict = { obj.score:obj.have for obj in frontier}
	print "==================="
	# for key in sorted(score_have_dict.keys(),reverse = True):
 #  		print "%s: %s" % (key, score_have_dict[key])

  	sorted_keys = sorted(score_have_dict.keys(),reverse = True)
  	print "%s: %s" % (sorted_keys[0], score_have_dict[sorted_keys[0]])
	
	return frontier

def update(f,cf, frontier, curr_candidate_sol,baseline_min,baseline_max,total=0.0, n=0):
	# print "FROM UPDATE -->", curr_candidate_sol
	for x in frontier:
		s = x.score
		curr_candidate_sol.decisionVec = x.have
		new = extrapolate(frontier,x,f,cf,curr_candidate_sol,baseline_min,baseline_max)
		# print "new_score:", new.score
		# print "extrapolated vector:", new.have	
		# print "parent :", s
		if new.score > s:
			# print "+++++++++++++++++++++++++++++++++++++++"
			# print "new.have=", new.have
			# print "x.have=", x.have
			# print "new.score=", new.score
			# print "s=", s
			x.score = new.score
			x.have = new.have
		
		total +=x.score
		# print "x.score:", x.score
		# print "total:", total
		# print "n:", n
		total +=x.score
		n += 1
	return total,n

def extrapolate(frontier, one, f, cf,curr_candidate_sol,baseline_min,baseline_max):
	# print "FROM EXTRAPOLATE -->", curr_candidate_sol
	out = Thing(id = one.id, have = copy.deepcopy(one.have))
	two, three, four = threeOthers(frontier, one)
	changed = False
	numOfDecisions = len(out.have)
	for d in range(numOfDecisions):
		x,y,z = two.have[d], three.have[d], four.have[d]
		# if (d == 3) or (d ==2):
		# 	print "d,x,y,z ",d,"||", x," ",y," ",z
		if random.random() < cf:
			# print "-------------------=======================MANISH MANISH MANISH============------------"
			changed = True
			new = x + f*(y-z)
			# print "new:", new," ",
			# print "d:", d
			# print "trimmed value:", trim(curr_candidate_sol,new,d)
			# print "out.have:", out.have
			out.have[d] = trim(curr_candidate_sol,new,d)
			# print "afterwards out.have:", out.have
			# exit()
	if not changed:
		d = a([d for d in range(numOfDecisions)])
		out.have[d] = two.have[d]
		curr_candidate_sol.decisionVec = out.have

	current_score = score(curr_candidate_sol)	
	if (current_score > baseline_max):
		baseline_max = current_score
	if (current_score < 0):
		baseline_min = 0
	if (current_score < baseline_min):
		baseline_min = current_score

	out.score = (score(curr_candidate_sol) - baseline_min)/(baseline_max - baseline_min)
	return out


def threeOthers(lst, avoid):
	def oneOther():
		x = avoid
		while x.id in seen:
			x=a(lst)
		seen.append(x.id)
		return x

	seen = [ avoid.id ]
	this = oneOther()
	that = oneOther()
	theOtherThing = oneOther()
	return this, that, theOtherThing

def a(lst):
	return lst[int(n(len(lst)))]


if __name__ == "__main__":
	print "Starting Differential Evolution. Hold on tight."
	print "================================================"
	model=Golinski
	baseline_min,baseline_max = get_min_max(model)
	print "baseline_min,baseline_max ", baseline_min," ",baseline_max
	de(model,baseline_min,baseline_max)

# if __name__ == "__main__":
# 	model=Golinski
# 	curr_candidate_sol = model()
# 	# curr_candidate_sol.decisionVec = [lo(curr_candidate_sol,d) + n(hi(curr_candidate_sol,d) - lo(curr_candidate_sol,d)) for d in decisions(curr_candidate_sol)]

# 	for d in decisions(curr_candidate_sol):
# 		print "d:", d, "low value:", lo(curr_candidate_sol,d)
# 		print "d:", d, "high value:", hi(curr_candidate_sol,d)
# 		print "difference:", hi(curr_candidate_sol,d) - lo(curr_candidate_sol,d), " N->", n(hi(curr_candidate_sol,d) - lo(curr_candidate_sol,d))
# 		print "output:", lo(curr_candidate_sol,d) + n(hi(curr_candidate_sol,d) - lo(curr_candidate_sol,d))


# 	# val=n(11.0)
# 	# print val






















