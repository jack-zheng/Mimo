# Mimo
My mini monitor

### Task1:

1. design sqlite db to log everyday task
	* deal with 'time', use sql insert into .. datetime("now", "localtime");
	* use standard " instead of ', or there maybe a Error: incomplete sql when import db from sql.

2. python client connect to sqlite
	* GUI of mimo, there are two solution. one is pure python, ugly but easy. the other is like web skill, python -> Flask -> electron(page point to web address).

3. finish the basic function of Mimo.

# TODO:

1. once click the Insert button, init all fields
2. need a status bar beside task name to show whether the insert is successfully.
