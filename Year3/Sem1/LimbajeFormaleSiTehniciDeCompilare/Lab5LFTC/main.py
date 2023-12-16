from Grammar import Grammar

if __name__ == '__main__':
    g = Grammar()
    g.readFromFile("g2.txt")
    print(str(g))
    if g.checkCFG():
        print("The grammar is a Context-Free Grammar")
    else:
        print("The grammar is not a Context-Free Grammar")
