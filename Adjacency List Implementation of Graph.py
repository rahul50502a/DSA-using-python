class Graph:
    def __init__(self,vno) -> None:
        self.vertex_count = vno
        self.adj_list = {v:[] for v in range(vno)}
        