from icecream import ic

def add(x,y):
    return x + y

def myfunction(value):
    if value % 2 == 0:
        ic()   #IC returns more information from an execution
        return True
    else:
        ic()   #IC returns more information from an execution
        return False
    
def output_to_file(text):
    with open('debug_log.txt','a') as f:
        f.write(text + '\n')


# change the configuration of icecream loging, in this case, we get the output file log
ic.configureOutput(prefix='Debug| ',outputFunction=output_to_file,
                   includeContext=True)

ic(add(10,20))