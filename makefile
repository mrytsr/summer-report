all:
	cat report-head.md > report.md
	python2 ./report.py >> report.md
	git add -A ;git commit -m"add -A";git push origin master
