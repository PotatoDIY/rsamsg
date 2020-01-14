from rsamsg import gen,savefile

alice_pubkey, alice_privkey=gen()
bob_pubkey, bob_privkey=gen()


savefile("keys/alice_prikey",alice_privkey)
savefile("keys/alice_pubkey",alice_pubkey)

savefile("keys/bob_prikey",bob_privkey)
savefile("keys/bob_pubkey",bob_pubkey)