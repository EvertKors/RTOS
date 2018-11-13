from threading import Thread

def tr(arg):
    i=0
    while True:
       	if i % 100 == 0:
            print(arg, i)
 	i+=1;

if __name__ == "__main__":
    for i in range(1,100):
    	t = Thread(target = tr, args=(i, ))
    	t.start()
