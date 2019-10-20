import converter
from Bio import AlignIO
from sklearn import svm
from combinatorics import m_way_unordered_combinations as choose_n



"""
makes a svm where 0 is hydroxylase and 1 is halogenase


"""


hydro_name = "WP_107105619HWD"
ancestor_name = "hand_pickedHWG"


dic = converter.dic

alignment_files = [
    "/Applications/Chang_Lab/biopy/SVM/sequence_files/clustal.txt",
    "/Applications/Chang_Lab/biopy/SVM/sequence_files/mafft2.txt",
    "/Applications/Chang_Lab/biopy/SVM/sequence_files/muscle.txt"
]





# hydroxylase = AlignIO.read("", 'fasta') # TODO: insert file name
# halogenase = AlignIO.read("", 'fasta') # TODO: insert file name

def encode(seq):
    return [dic[aa] for aa in seq]



def fit_model(halogenase, hydroxylase):
    x = [encode(halo) for halo in halogenase]
    y = [encode(hydro) for hydro in hydroxylase]

    # for halo in halogenase:
    #     halo = halo.seq
    #     x.append(encode(halo))
    #     y.append(1)
    #
    # for hydro in hydroxylase:
    #     hydro = hydro.seq
    #     x.append(encdoe(hydro))
    #     y.append(0)

    clf = svm.SVC(degree = 21, gamma='scale')
    clf.fit(x, y)
    return clf




def test_combinations(differences, num_options, close_hydro, model):
    options = choose_n(differences, [num_options])
    output = []

    for option in options:
        mutant = ""
        prev = 0
        for mutation in option[0]:
            mutant += close_hydro[prev: mutation[2]] + mutation[0]
            prev = mutation[2] + 1
        mutant += close_hydro[prev:]

        if model.predict(encode(mutant)):
            output.append(option)

    return output

for file_name in alignment_files:
    alignment = AlignIO.read(file_name, "fasta")
    hydro = []
    halo = []
    ancestor = ""
    close_hydro  = ""
    for align in alignment:
        if align.id == ancestor_name:
            ancestor = align.seq
        elif align.id == hydro_name:
            close_hydro = align.seq
        if align.id[-3:] == "HWD":
            hydro.append(align.seq)
        else:
            halo.append(align.seq)

    differences = []
    for a, b, c in zip(ancestor, close_hydro, range(len(ancestor))):
        if a != b:
            differences.append([a, b, c])

    model = fit_model(halo, hydro)

    switches = []
    for i in range(1, 5):
        temp = test_combinations(differences, i, model)
        switches.append(temp)

    print(file_name, len(switches))

    more = int(input("would you like to display all switching mutations(input int 1-5):"))
    for i in range(more):
        print(switches[i])










#
