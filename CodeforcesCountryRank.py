import urllib.request,json

#change the three variables below
contestId = "1107"
country = "India"
userhandle=	"anjn98"

link = "http://codeforces.com/api/contest.standings?contestId=" + contestId+ "&showUnofficial=false"
a = []
p = {}
print ("Getting data from the contest")
with urllib.request.urlopen(link) as url:
	print ("Fetching data from the contest")
	data = json.loads(url.read().decode())
	print ("Processing data from the contest")
	w = url.read()
	for x in data["result"]["rows"]:
		for i in x["party"]["members"]:
			a.append(i["handle"])
			p[i["handle"]] = x["rank"]
r = []
q = []
s = 0
step = 500
e = min(len(a),step)
while s < len(a):
	link2 = "http://codeforces.com/api/user.info?handles="+";".join(a[s:e])
	with urllib.request.urlopen(link2) as url:
		data = json.loads(url.read().decode())
		for x in data["result"]:
			if "country" in x:
				if x["country"] == country:
					r.append(x["handle"])
				if x["handle"] == userhandle:
					break

	print("Done " + str(e))
	s += step
	e += step
	e = min(len(a),e)

cot=1

for t in r:
	if t==userhandle	:
		print("------------------------------------------")
		print("Your country rank is=  " + str(cot))
		print("Your user handle=	  " + t )
		print("Overall rank=          " + str(p[t]) )
		print("------------------------------------------")
		break
	cot=cot+1
	
