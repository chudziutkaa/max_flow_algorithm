import pprint

class Matrix(object):
    def __init__(self, row, column):
        self.row=row
        self.column=column
        self.matrix=[[0 for i in range(column)] for j in range(row)]
        for i in range(self.row):
            self.matrix[0][i]=i
        for j in range(self.column):
            self.matrix[j][0]=j

    def add(self, vertex1, vertex2, weight):
        self.matrix[vertex1][vertex2]=weight

    def display(self):
        pprint.pprint(self.matrix)

    def browsePath(self, start, end):
        stack=[]
        stack.append([start, [start]])
        while len(stack)!=0:
            [v, path] = stack.pop()
            for i in range(1, len(self.matrix[v])):
                if self.matrix[v][i]!=0:
                    if i in path:
                        continue
                    elif i==end:
                        path=path+[i]
                        pass
                        return path
                    else:
                        stack.append([i, path+[i]])

    def flow(self, start, end):
        path=self.browsePath(start, end)
        flows=[]
        max_flow=0
        while path!=None:
            for i in range(len(path)-1):
                flows.append(self.matrix[path[i]][path[i+1]])
            minimum=min(flows)
            self.matrix[path[i]][path[i+1]]=self.matrix[path[i]][path[i+1]]-minimum
            max_flow=max_flow+minimum
            path=self.browsePath(start, end)
        else:
            print "Maximum flow for this path from vertex %s to vertex %s equals: %s" %(start, end, max_flow)

