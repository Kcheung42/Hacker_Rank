# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    myfirst.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/14 18:17:18 by kcheung           #+#    #+#              #
#    Updated: 2018/01/15 11:09:20 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class TrieNode:
	def __init__(self):
		self.children = [None] * 26
		self.isEndOfWord = False

class Trie:
	def __init__(self):
		self.root = self.getNode()

	def getNode(self):
		return TrieNode()

	def charToIndex(self, ch):
		return ord(ch) - ord('a')

	def insert(self, key):
		pCrawl = self.root
		length = len(key)
		for level in range(length):
			index = self.charToIndex(key[level])
			if not pCrawl.children[index]:
				pCrawl.children[index] = self.getNode()
			pCrawl = pCrawl.children[index]
		pCrawl.isEndOfWord = True

	def search(self, key):
		length = len(key)
		pCrawl = self.root
		for level in range(length):
			index = self.charToIndex(key[level])
			if not pCrawl.children[index]:
				return False
			pCrawl = pCrawl.children[index]
		return pCrawl != None and pCrawl.isEndOfWord

def main():

	# Input keys (use only 'a' through 'z' and lower case)
	keys = ["the","a","there","anaswe","any",
			"by","their", "bambi"]
	output = ["Not present in trie",
			"Present in tire"]

	# Trie object
	t = Trie()

	# Construct trie
	for key in keys:
		t.insert(key)

	# Search for different keys
	print("{} ---- {}".format("the",output[t.search("the")]))
	print("{} ---- {}".format("these",output[t.search("these")]))
	print("{} ---- {}".format("their",output[t.search("their")]))
	print("{} ---- {}".format("thaw",output[t.search("thaw")]))
	print("{} ---- {}".format("bambi",output[t.search("bambi")]))

if __name__ == '__main__':
	main()
