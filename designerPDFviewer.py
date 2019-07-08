
h = list(map(int, input().rstrip().split()))

word = input()


def designerPdfViewer(h, word):
    alpha =[]
    for i in range(97, 97 + 26):
        x = chr(i)
        alpha.append(x)
    height = []
    for j in range(len(word)):

        z = alpha.index(word[j])
        height.append(h[z])

    volume = len(word)*max(height)

    print(volume)



result = designerPdfViewer(h, word)
