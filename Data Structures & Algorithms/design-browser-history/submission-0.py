class BrowserHistory:

    def __init__(self, homepage: str):
        # must store history # of steps
        # self.curr = None
        self.history = [homepage]
        self.ptr = 0
        

    def visit(self, url: str) -> None:
        # visit url
        # clear up forward history
        self.history = self.history[:self.ptr + 1]
        self.history.append(url)
        self.ptr += 1
        

    def back(self, steps: int) -> str:
        # if can't go back x steps, go back as much as possible
        # return curr url

        if self.ptr - steps < 0:
            self.ptr = 0
        else:
            self.ptr -= steps
        
        return self.history[self.ptr]

# forward =  [5, 6, 7]
# curr = 4
# backwards = [1, 2, 3]

    def forward(self, steps: int) -> str:
        # go forward, return url
        # if you can't go forward x steps then go as much as possible 

        l = len(self.history)
        if self.ptr + steps + 1 > l:
            self.ptr = l - 1
        else:
            self.ptr += steps

        return self.history[self.ptr] 



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)