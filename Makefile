PKG_MAN_PROG = $(shell if[ `lsb_release -is` = "CentOS" ]; then echo yum; else echo apt-get; fi)

init-db:
	mysqldump -uroot -psasa blog < mysql/blog.sql
runtime-dep:
	sudo easy_install pip
	sudo pip install -r requirements.txt

run:
	python app.py
