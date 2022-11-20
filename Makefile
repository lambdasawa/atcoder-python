.PHONY: setup
setup:
	direnv allow

	pip3 install online-judge-tools
	asdf reshim
	oj --version
	oj login -u "${ATCODER_USERNAME}" -p "${ATCODER_PASSWORD}" https://beta.atcoder.jp/

	npm install -g atcoder-cli
	asdf reshim
	acc --version
	acc login
