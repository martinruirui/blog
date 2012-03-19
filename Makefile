PKG_MAN_PROG = $(shell if[ `lsb_release -is` = "CentOS" ]; then echo yum; else echo apt-get; fi)
runtime-dep:
	sudo easy_install pip
	sudo pip install -r requirements.txt
