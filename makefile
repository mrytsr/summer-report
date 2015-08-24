all:
	python2 ./download.py > download.md
	python2 ./order.py > order.md
	cat report-head.md download-head.md download.md order-head.md order.md > report.md
	cd tocmd && make; ./replace.sh
	# git add -A ;git commit -m"add -A";git push origin master
