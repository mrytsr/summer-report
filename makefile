all:
	python2 ./download.py > download.md
	python2 ./order.py > order.md
	cat report-head.md download.md order.md > report.md
	git add -A ;git commit -m"add -A";git push origin master
