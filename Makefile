PKG_MAN_PROG = $(shell if[ `lsb_release -is` = "CentOS" ]; then echo yum; else echo apt-get; fi)
NOW = $(shell date -d now +"%F")
DB_HOST = localhost
DB_USER = root
DB_PASSWD = sasa
DB = blog
mysql_dumps = mysqldump -u$(DB_USER) -p$(DB_PASSWD) $(DB)
mysql = mysql -u$(DB_USER) -p$(DB_PASSWD) $(DB)

runtime-dep:
	sudo easy_install pip
	sudo pip install -r requirements.txt

run:
	@echo "run server at http://localhost:8080\nyou could use curl tools test server\nexample:\n\tcurl 'http://localhost:8080/article/1'"
	@python app.py

init-db:
	${mysql} < mysql/blog.sql

dumps-table:
	${mysql_dumps} --no-data > mysql/blog.sql

dumps-data:
	${mysql_dumps} --no-create-info > mysql/data.sql
