cell_ind=0
cells=[0]*100000
i=0
j=0
YOUR_NAME=""

# positions of  '[' and ']' 
loop_pos = {}

# stack of open brackets
stack = []

bf_code=">+++++++[<++++++++++>u-]<+.>>+++++++++[<+++++++++>-]<+.>>+++dgdfgada++++++++++++++++++[<++++>-]<.>>+++++++++++[<++++++++>-]<+.>++++++++++++++++++++++++++++++++.>>+++++++[<++++++++++>-]<+.>>++++++++[<+++++++++>-]<.>>+++++++++++++[<+++++>-]<.>>+++++++++++++++++++++[<++++>-]<-.>>+++++++++++++++++++++++[<+++>-]<.>>+++++++++++[<++++dasdasfdsg+++>-]<.>>++++++++[<+++++++++>-]<+."

while j<len(bf_code):
	# push the location of open brackets onto the stack
    if bf_code[j]=="[":
        stack.append(j)
        
	# when a closing bracket is found, get the starting position and store the start/end pair
    if bf_code[j]== "]":
        if len(stack)==0:
            raise Exception('Loop end when no loops open at location %i' % j)
        start = stack.pop()
        loop_pos[start]=j
        loop_pos[j]=start
    j+=1

	# adding pointer
def addpointer(): 
        global cell_ind,i
        cell_ind=cell_ind+1
        if cell_ind>len(cells):
            raise Exception('error:overflow pointer')
        
     
	#reduce pointer	 
def reducepointer(): 
        global cell_ind,i
        cell_ind=cell_ind-1
        if cell_ind < 0:
            raise Exception('error:underflow pointer- tried to move to cell -1')
        
    
    #increasing cell
def increascell(): 
        global cells,cell_ind,i
        cells[cell_ind]=cells[cell_ind]+1
        if cells[cell_ind] > 255:
            raise Exception('Memory overflow at location %i' % cell_ind)
        
		
		
    #decreasing cell    
def decreascell():   
        global cells,cell_ind,i
        cells[cell_ind]=cells[cell_ind]-1
        if cells[cell_ind] < 0:     
            raise Exception('Memory underflow at location %i' % cell_ind)
        
        
	#begining loop		
def firstloop():
    global cells,cell_ind,i
         
    if cells[cell_ind] == 0:
        i = loop_pos[i] 
    
	
	
	#end of loop
def endloop():      
    global cells,cell_ind,i
    if cells[cell_ind] != 0:
        i = loop_pos[i]
       

    #output
def endofchar():      
    global YOUR_NAME,i,cells,cell_ind
    YOUR_NAME+=(chr(cells[cell_ind]))
    #print(cells[cell_ind]) 
    
    
   
while i<len(bf_code):

    d=bf_code[i]
    
    
# map the inputs to the function blocks
    switcher = {'+' : increascell,
           '-' :decreascell,
           '>' : addpointer,
           '<' : reducepointer,
           '.' : endofchar,
           '[' : firstloop,
           ']' : endloop,
           
    }
    
    try:
        switcher[d]()
        i=i+1
    except KeyError:
        i=i+1

#print output of bf code
print(YOUR_NAME) 






       

            
            
