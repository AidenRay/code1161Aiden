# -*- coding: UTF-8 -*-
def test(string1):
	return {"this one": string1}


if __name__ == "__main__":
	while True:
		x = str(raw_input(""))
		y = test(x)
		print y