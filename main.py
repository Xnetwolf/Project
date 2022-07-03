import mnemonic
import bip32utils
import os
from xkcdpass import xkcd_password as xp

r = open("rules.txt", "r")
r1 = r.read()
t = open("english.txt", "r")
t1 = t.readlines()
#print(t1[0].split("\n"))
z = open("test2.txt", "w")
os.system("xkcdpass --count=100 --delimiter=' ' -n=18 -w='english.txt' > hello.txt")
def bip39(mnemonic_words):
	mobj = mnemonic.Mnemonic("english")
	seed = mobj.to_seed(mnemonic_words)

	bip32_root_key_obj = bip32utils.BIP32Key.fromEntropy(seed)
	bip32_child_key_obj = bip32_root_key_obj.ChildKey(44 + bip32utils.BIP32_HARDEN).ChildKey(0 + bip32utils.BIP32_HARDEN).ChildKey(0+ bip32utils.BIP32_HARDEN).ChildKey(0).ChildKey(0)

	return bip32_child_key_obj.Address()


def check():
	b = 0
	a = 1
	while a == 1:
		addy = bip39(mnemonic_words)
		balance = getBalance(addy)
		if balance > 0:
			print(mnemonic_words)
			open("logs.txt", "w").write(mnemonic_words)
			a = 2
		else:
			print(f"{b+1}")
			b = b+1
