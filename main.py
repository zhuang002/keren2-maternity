def get_possible_gene(gene1, gene2):
    rt_gene=set()
    for g1 in gene1:
        for g2 in gene2:
            if g1.isupper() or g2.isupper():
                rt_gene.add(g1.upper())
            else:
                rt_gene.add(g1)
    return rt_gene


def get_possible_genes(parent1, parent2):
    list = []
    for i in range(5):
        gene1 = parent1[i*2:i*2+2]
        gene2 = parent2[i*2:i*2+2]
        possible_genes = get_possible_gene(gene1,gene2)
        list.append(possible_genes)
    return list


def is_possible_baby(baby, genes):
    for i in range(5):
        g = baby[i]
        gg = genes[i]
        if g not in gg:
            return False
    return True




alice = input()
bob = input()

possible_genes = get_possible_genes(alice,bob)

babes = int(input())

for i in range(babes):
    baby = input()
    if is_possible_baby(baby, possible_genes):
        print("Possible baby.")
    else:
        print("Not their baby!")


