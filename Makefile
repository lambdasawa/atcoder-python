.PHONY: login
login:
	oj login -u lambdasawa -p "${ATCODER_PASSWORD}" https://beta.atcoder.jp/
	acc login
