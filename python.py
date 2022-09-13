#importing puLP modeller
from pulp import *  
# Creates a list of all the charging stn.
CS = ["a", "b", "c"]
cpcost = {  "a":[20, 70000],
            "b" :[20, 70000],
            "c" :[20, 65000]
         }
               }

zones = ["3", "5", "6", "7", "8", "12", "13"]
demand = {"3" :18,"5" : 10,"6" :10 ,"7" : 2,"8" : 10,"12" :10 ,"13" : 10,}
costs = 
        #3    #5    #6  #7
        [
        [82, 75, 5, 20, 37, 16, 112], #a
        [4119, 112, 37, 17, 5, 24, 149],#b   Plants
        [30, 25, 112, 132, 149, 128, 5], #c
        ]
Routes = [(p, s) for p in Plants for s in zones]
(supply, fixedCost) = splitDict(cpcost)
costs = makeDict([Plants, zones], costs, 0)
flow = LpVariable.dicts("Route",(Plants,ones),0,None,LpInteger)
build = LpVariable.dicts("Build  charging station ",Plants,0,1,LpInteger)

prob = LpProblem("Charging station Problem",LpMinimize)
prob += lpSum([flow[p][s]*costs[p][s] for (p,s) in Routes])+lpSum([fixedCost[p]*build[p] for p in Plants]),"Total Costs"
for p in Plants:
    prob += lpSum([flow[p][s] for s in zones]) <= supply[p]*build[p], ("Sum of chargers  out of Plant %s"%p)
for s in Nodes:
    prob += lpSum([flow[p][s] for p in Plants]) >= demand[s], ("Sum of chargers  into zones %s" %s)
# The problem is solved using PuLP's choice of Solver
prob.solve()
# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])
# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name,"=",v.varValue)
# The optimised objective function value 
print("Total Costs = ", value(prob.objective))
