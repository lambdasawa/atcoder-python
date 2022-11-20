.PHONY: setup
setup:
	which oj || make setup-oj
	oj login -u lambdasawa -p "$(shell op read op://Personal/AtCoder/newPassword)" https://beta.atcoder.jp/

	which acc || make setup-acc
	acc session | grep OK || acc login
	ln -sf ${PWD}/__template__/py $(shell acc config-dir)/
	ln -sf ${PWD}/config.json $(shell acc config-dir)/

.PHONY: setup-oj
setup-oj:
	pip3 install online-judge-tools && asdf reshim && oj --version

.PHONY: setup-acc
setup-acc:
	npm install -g atcoder-cli && asdf reshim && acc --version
