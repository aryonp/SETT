I assume that you already fully installed a linux box.

1. Please install speedtest-cli first on your linux box (I'm using Debian 8)

	apt-get install python-pip
	pip install speedt-cli

2. Choose destination server

	speedtest-cli --list | grep -i munich

3. Add server ID to script sett.py

	speedtest-cli --server XXXX --simple

4. Set the cron scheduler when the script will fire up, I schedule it to test on peak time

	crontab -e

	30 10 * * * python /home/aryonp/sett.py 

	30 15 * * * python /home/aryonp/sett.py 

5. Leave it for a week.

6. After a week read the report on your home folder. for ex: /home/aryonp/data.csv

7. Decide which provider you will use for the institute ;-)
