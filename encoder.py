import converter
from Bio import AlignIO
from sklearn import svm
from combinatorics import m_way_unordered_combinations as choose_n



"""
makes a svm where 0 is hydroxylase and 1 is halogenas


"""


hydro_name = "WP_107105619HWD"
ancestor_name = "hand_pickedHWG"


dic = converter.dic

alignment_files = []

hydroxylase = AlignIO.read("", 'fasta') # TODO: insert file name
halogenase = AlignIO.read("", 'fasta') # TODO: insert file name

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

    clf = svm.SVC(gamma='scale')
    clf.fit(x, y)
    return clf



def test_combinations(options):
    pass










#
