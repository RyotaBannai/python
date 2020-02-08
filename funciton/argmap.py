def cheeseshop(kind, phrase='this is the test', *arguments, **keywords):
	"""Do nothing, but document it.

  No, really, it doesn't do anything.
    """
	print("-- Do you have any", kind, "?")
	print("-- I'm sorry, we're all out of", kind)

	#mapした引数を全て呼び出す.
	for arg in arguments:
		print(arg)
	print("-" * 40)
	for kw in keywords:
		print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


print(cheeseshop.__doc__)