#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run ethernet-ring-dimensioning

# https://py.checkio.org/mission/ethernet-ring-dimensioning/

# A ring topology is a network configuration where the devices are connected to each other in a circular shape.    Optical rings are widely used in mobile networks to transport the traffic from a base station to the backbone, through the mobile backhaul.
# 
# 
# 
# Definition of a ring
# For the sake of simplicity, in this task, we define a ring as a connex graph which vertexes:- have a degree2, which means they have2incident edges.- are connected to two distinct vertexes
# These two conditions ensure that there is a single link between each pair of adjacent nodes.     Ring are represented as a string made of distinct characters,which position in the string reflects the position in the ring.For instance, the ring"AEFCBG"defines the following topology:
# 
# 
# 
# Shortest path asymmetric routing
# Multiple traffic flows will be routed on the ring.
# Each flow is routed on theshortest pathfrom theingress node(starting point of the traffic) to theegress node(exit point of the traffic).
# If there are two shortest paths,the path which order fits the ring definition is kept.
# Let's consider the following situation:
# 
# 
# 
# 
# The path fromAtoB(and fromBtoA) will be"A - G - B", because it uses only two links, while the path going the other way around("A - E - F - C - B")uses five links.
# However, there are two paths of equal length to route a traffic fromAtoC:"A - E - F - C"and"A - G - B - C". The first one,"A - E - F - C", is kept: it is thesame orderas in the ring definition ("AEFCBG").
# The traffic fromCtoAwill use the path"C - B - G - A": the routing is asymmetric in that case.
# 
# 
# Flow aggregation
# A traffic flow is represented as a couple(s, dr)where:-sis a string of length 2, containing theingress nodeand theegress node.-dris the data rate inGbps(gigabit per second).
# The data rate of a traffic flow will be counted for all the links of the shortest path.
# A traffic flow("AB", 5)means that 5 Gbps will be routed on the shortest path fromAtoB.
# We count 5 Gbps on the link"AG"and 5 Gbps on the link"GB". For a traffic flow("CA", 15), we count 15 Gbps on the links"CB","BG", and"GA".
# In order to simplify the model, we consider that the traffic flowsingress -> egressandegress -> ingressare equivalent with regard to dimensioning.
# Two traffic flows("AG", 3)and("GA", 3)induce a 6-Gbps flow on the linkAG, as would("AG", 6)or("GA", 6): links are notdirectional.         Given a list of traffic flows, we consider the resulting bandwidth on each link to dimension the ring.
# 
# 
# Ethernet links dimensioning
# There are five main types of Ethernet links used in mobile networks:-Fast Ethernet(FE): 100 Mbps (or 0.1 Gbps)-Gigabit Ethernet(GE): 1 Gbps.-10 Gigabit Ethernet(10GE): 10 Gbps-40 Gigabit Ethernet(40GE): 40 Gbps.-100 Gigabit Ethernet(100GE): 100 Gbps.
# In order to select a type of link, we look for thesmallest bandwidth allowing to carry the whole traffic with a single link.    Handling a5-Gbps trafficwould require 50 FE links, 5 GE links, or 1 10GE link. Therefore, a10GE Ethernet linkis used.    For a15-Gbps traffic, a40GE Ethernet linkis required. For a traffichigher than 100 Gbps,100GE Ethenet linksare used (2 100GE Ethernet links for a 101-Gbps flow).
# 
# 
# Given a ring and a list of traffic flows, you should return the number of Ethernet links of each type that are required to carry the resulting bandwidth:
# 
# 
# 
# 
# 
# In this example, we have 10 Gbps fromEtoC, 5 Gbps fromAtoCand 60 Gbps fromAtoB.
# These traffic flows induce the following bandwidth: 15 Gbps fromEtoC, 5 Gbps fromAtoEand 60 Gbps fromAtoB.
# The link dimensioning results in 2 100GE, 2 40GE and 1 10GE Ethernet links.
# 
# 
# The result is given as a list containing the number of links for each category, from 100GE to FE.    In our example, the result is[2, 2, 1, 0, 0]
# 
# Input:A variable number of arguments. The first one is a ring, represented as a string where each character is a node.    The remaining arguments are traffic flows, represented as couples(s, dr)wheresis a 2-characters string (ingress node, egress node) anddris a positive value (traffic in Gbps).
# 
# Output:A list with 5 integers, one per type of link, indecreasing order of bandwidth capacity.
# 
# 
# END_DESC

ETHERNET = (100, 40, 10, 1, 0.1) # Ethernet bandwidth capacity in Gbps

def checkio(ring, *flows):
    pass

if __name__ == '__main__':
    # These "asserts" are used only for self-checking and not necessary for auto-testing
    assert checkio("AEFCBG", ("AC", 5), ("EC", 10), ("AB", 60)) == [2, 2, 1, 0, 0]
    assert checkio("ABCDEFGH", ("AD", 4)) == [0, 0, 3, 0, 0]
    assert checkio("ABCDEFGH", ("AD", 4), ("EA", 41)) == [4, 0, 3, 0, 0]