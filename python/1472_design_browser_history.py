class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.currentPage = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.currentPage + 1]
        self.history.append(url)
        self.currentPage += 1

    def back(self, steps: int) -> str:
        self.currentPage = max(0, self.currentPage - steps)
        return self.history[self.currentPage]

    def forward(self, steps: int) -> str:
        self.currentPage = min(len(self.history) - 1, self.currentPage + steps)
        return self.history[self.currentPage]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)