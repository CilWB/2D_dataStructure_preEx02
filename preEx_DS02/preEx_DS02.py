class node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

class link_list:
    def __init__(self,h=None):
        self.head = h
    def __str__(self):
        #s = 'LL '
        s = ''
        t = self.head
        while t != None :
            s += str(t.data)
            t = t.next
            #if t != None :
            #    s += '->'
        return s
    def at(self,n):
        if n <= 0 :
            return None
        t = self.head
        cnt = 1
        while cnt < n and t != None:
            cnt+=1
            t = t.next
        return t
    def tail(self):
        t = self.head
        while t.next != None:
            t = t.next
        return t
    def append(self,data):
        if self.head == None :
            self.head = node(data)
        else:
            self.tail().next = node(data)

    def size(self):
        cnt = 0 
        t = self.head
        while t!=None:
            cnt+=1
            t = t.next
        return cnt

    def remove(self,n):
        # __n1__->__n2__->__n3__
        #    1      2       3
        if 0<n<=self.size():
            if n == 1 :
                self.head = self.head.next
            else:
                t = self.at(n-1)
                t.next = t.next.next
        else:
            print("ERRORRRR OUT BOUND in remove")
            return None

    def findfromN(self,n,data): # [n,size)
        # if found return n
        # else return -1
        cnt = n
        t = self.at(n)
        ans = -1
        while t != None :
            if t.data == data :
                ans = cnt
                break
            else:
                cnt+=1
                t=t.next
        return ans

def createList(items):
    ll = link_list()
    for i in items :
        ll.append(i)
    return ll

def  delRepeat(LL):
    t = LL.head
    cnt = 1
    while t != None :
        cnt += 1
        cnt2 = cnt
        while LL.findfromN(cnt2,t.data) != -1 :
            LL.remove(LL.findfromN(cnt2,t.data))
        t = t.next
            
############ Question 2 ############    
#print('--no2--')
#l = [c for c in input('input: ').split()]
#print('l= ',l)

#h = createList(l)
#print(h)

#delRepeat(h)
#print(h)
####################################

