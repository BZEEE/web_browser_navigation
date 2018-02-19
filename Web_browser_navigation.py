# A Stack implementation

class Stack:
    
    def __init__(self):
        self.items = ['www.cs.ualberta.ca']
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def make_empty(self):
        self.items = []
    

def main():
    mainStack = Stack()
    otherStack = Stack()
    otherStack.make_empty()
    endSession = False
    print('[{}]'.format(mainStack.peek()))
    while not endSession:
        validInput = False
        #makes sure its a valid input
        while not validInput:
            action = input()
            if action == '=' or action == '<' or action == '>' or action == 'end':
                validInput = True
        
        if action == '=':
            # enter website and clear all forward history that exists in otherStack
            website = input()
            mainStack.push(website)
            otherStack.make_empty()
            print('[{}]'.format(mainStack.peek()))
            
        elif action == '<':
            # if your stack has more then one element in it, you can still go back
            if not mainStack.size() == 1:
                previousWebsite = mainStack.pop()
                otherStack.push(previousWebsite)
                print('[{}]'.format(mainStack.peek()))
                
            # if your stack has one element (home page) then you cant go back
            else:
                print(action, 'is an invalid action')
                print('[{}]'.format(mainStack.peek()))
            
        elif action == '>':
            #if other stack is not empty then you do have forward history
            if not otherStack.is_empty():
                aheadWebsite = otherStack.pop()
                mainStack.push(aheadWebsite)
                print('[{}]'.format(mainStack.peek()))
                
            #if you dont have any forward history
            else:
                print(action,'is an invalid action ')
                print('[{}]'.format(mainStack.peek()))
        
        #ends session if you want to       
        elif action == 'end':
            endSession = True
        
    
main()