class Solution:
    def dfs(self, airport):
        if airport in self.adjList:
            tickets = self.adjList[airport]
            while len(tickets) > 0:
                ticket = tickets.pop()
                self.dfs(ticket)
        self.route.append(airport)
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.route = []
        self.adjList = defaultdict(list)

        for i, j in tickets:
            self.adjList[i].append(j)
        print(self.adjList)
        for key in self.adjList: 
            self.adjList[key] = sorted(self.adjList[key], reverse=True)
        print(self.adjList)
        
        self.dfs("JFK")
        return self.route[::-1]