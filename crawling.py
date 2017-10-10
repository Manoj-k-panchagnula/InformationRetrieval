from collections import deque
from bs4 import BeautifulSoup
from urlparse import urljoin
import sys
import urllib2
import time

url = " http://www.unt.edu"

print "pages to be crawled"

# Create queues
queue = deque([])
queue2 = []
queue3 = []
# Maintains list of visited pages
visited_list = []



# Crawl the page and populate the queue with newly found URLs
def crawl(url):
	visited_list.append(url)
	if len(queue) > 20000:
		return
	try:	
		urlf = urllib2.urlopen(url)
		soup = BeautifulSoup(urlf.read())
		urls = soup.findAll("a", href = True)
		
		# If not found in queue	
		for i in urls:
			flag = 0
			complete_url = urljoin(url, i["href"])
			queue.append(complete_url)
			
		# Pop one URL from the queue from the left side so that it can be crawled
		current = queue.popleft()
		# Recursive call to crawl until the queue is populated with 20000 URLs
		crawl(current)
	except:
		print ""

crawl(url)


def crawl_queue(url2):
	# Check if the URL already exists in the visited_list do not append
	if url2 not in visited_list:
		visited_list.append(url2)
		if len(queue2) > 20000:
			return
		try:	
			urlf = urllib2.urlopen(url2)
			soup = BeautifulSoup(urlf.read())
			urls = soup.findAll("a", href = True)
			for i in urls:
				flag = 0
				complete_url = urljoin(url2, i["href"])
				
				queue2.append(complete_url)
				
		except:
			print ""
#crawl(url)


def crawl_queue2(url3):
	if url3  not in visited_list:
		visited_list.append(url3)
		if len(queue3) > 20000:
			return
		try:	
			urlf = urllib2.urlopen(url3)
			soup = BeautifulSoup(urlf.read())
			urls = soup.findAll("a", href = True)
			for i in urls:
				flag = 0
				complete_url = urljoin(url3, i["href"])
				
				queue3.append(complete_url)
				
		except:
			print ""

	
for j in queue:
	crawl_queue(j)

	
for j in queue2:
	crawl_queue2(j)

print "------------Level 1-----------------"
for i in queue:
	print i
print len(queue)

print "------------pages crawled-----------"
for i in queue2:
	print i
print len(queue2)

counter=0
f = open("urls1.txt","w")
for i in visited_list:
	
	try:
		urlf = urllib2.urlopen(i, timeout=4)
		counter  = counter +1
		filename = str(counter)+".txt"
		target = open(filename, "w")			
		target.write(urlf.read())		
		target.close()
		f.write(i)
		f.write("\n")
	except:
		visited_list.remove(i)
f.close()
		

	
print len(queue)
print len(queue2)
print len(visited_list)

