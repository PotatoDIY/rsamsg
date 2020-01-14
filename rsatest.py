#!/usr/bin/python3
# -*- coding: utf-8 -*-
from rsamsg import *
#alice and bob




#alice_pubkey, alice_privkey=gen()
#bob_pubkey, bob_privkey=gen()

alice_pubkey = loadfile("keys/alice_pubkey")
alice_prikey = loadfile("keys/alice_prikey")
bob_pubkey = loadfile("keys/bob_pubkey")
bob_prikey = loadfile("keys/bob_prikey")


#from alice
message = "你好"

#to bob
crypto,signature=alice_to_bob(message,bob_pubkey,alice_prikey)

# bob verify
verifyed,msg=bob_get_msg_from_alice(crypto,signature,bob_prikey,alice_pubkey)
if(verifyed):
    print(msg)
else:
    print("err:{}".format(msg))