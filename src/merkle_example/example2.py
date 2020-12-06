

def example_tree(a, b, c, d):

    hash_a = hash(a)
    hash_b = hash(b)
    hash_c = hash(c)
    hash_d = hash(d)

    hash_ab = hash(hash_a + hash_b)
    hash_cd = hash(hash_c + hash_d)
    hash_ab_cd = hash(hash_ab + hash_cd)

    return hash_ab_cd
