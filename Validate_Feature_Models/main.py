def validate_apache(filename="./Data/Apache_AllMeasurements.csv"):
    def validate(solution):
        if sum(solution) == 0: return False
        if solution[0] != 1:
            print solution
            return False
        if solution[7] == 1 and solution[8] != 0:
            print solution
            return False
        return True

    f = open(filename, "r")
    for i,line in enumerate(f):
        if i == 0: continue
        soln = [1 if a == "Y" else 0 for a in line.split(",")[:-1]]
        assert(validate(soln) is True), "Something's wrong"


def validate_bdbc(filename="./Data/BDBC_AllMeasurements.csv"):
    def validate(solution):
        if sum(solution) == 0: return False
        page_size_index = 7
        cache_size_index = 13
        pages_indexes = [8, 9, 10, 11, 12]
        caches_indexes = [14, 15, 16, 17]
        if solution[page_size_index] != 1 and solution[cache_size_index] != 1: return False
        if sum([solution[i] for i in pages_indexes]) != 1: return False
        if sum([solution[i] for i in caches_indexes]) != 1: return False
        return True

    f = open(filename, "r")
    for i,line in enumerate(f):
        if i == 0: continue
        soln = [1 if a == "Y" else 0 for a in line.split(",")[:-1]]
        assert(validate(soln) is True), "Something's wrong"


def validate_bdbj(filename="./Data/BDBJ_AllMeasurements.csv"):
    def validate(solution):
        if sum(solution) == 0: return False
        if solution[0] != 1:return False
        if solution[1] != 1:return False
        if solution[2] != 1: return False
        if sum([solution[2], solution[3]]) == 0:return False
        if solution[4] == 1 and solution[5] != 1 and solution[6] != 1:return False
        if solution[6] == 1 and sum([solution[7], solution[8]]) != 1:return False
        if solution[10] != 1:return False
        if solution[10] == 1 and sum([solution[11], solution[12]]) == 0:return False
        if solution[13] != 1:return False
        if solution[14] != 1:return False
        if solution[19] == 1 and solution[17] != 1:return False
        if solution[16] != 1 and solution[17] != 1 and solution[18] != 1:return False
        if solution[20] == 1 and solution[21] != 1 and solution[22] != 1 and sum([solution[23], solution[24]]) != 1:return False
        return True

    f = open(filename, "r")
    for i,line in enumerate(f):
        if i == 0: continue
        soln = [1 if a == "Y" else 0 for a in line.split(",")[:-1]]
        # print soln, soln[2], soln[3]
        assert(validate(soln) is True), "Something's wrong"

def validate_llvm(filename="./Data/LLVM_AllMeasurements.csv"):
    def validate(solution):
        if sum(solution) == 0: return False
        if solution[0] != 1: return False
        return True

    f = open(filename, "r")
    for i,line in enumerate(f):
        if i == 0: continue
        soln = [1 if a == "Y" else 0 for a in line.split(",")[:-1]]
        # print soln, soln[2], soln[3]
        assert(validate(soln) is True), "Something's wrong"


def validate_x264(filename="./Data/X264_AllMeasurements.csv"):
    def validate(solution):
        if sum(solution) == 0: return False
        if solution[0] != 1: return False
        if solution[8] != 1: return False
        if solution[8] == 1 and sum([solution[9], solution[10], solution[11]]) != 1: return False
        if solution[12] != 1: return False
        if solution[12] == 1 and sum([solution[13], solution[14], solution[15]]) != 1: return False
        return True

    f = open(filename, "r")
    for i,line in enumerate(f):
        if i == 0: continue
        soln = [1 if a == "Y" else 0 for a in line.split(",")[:-1]]
        assert(validate(soln) is True), "Something's wrong"


def validate_SQL(filename="./Data/SQL_AllMeasurements.csv"):
    def validate(solution):
        print solution
        # if solution[0] != 1:
        #     print "1"
        #     return False
        indexes1 = [3,4,5,6]
        if solution[2] == 1 and sum([solution[i] for i in indexes1]) != 1:
            print "3"
            return False
        if solution[7] != 1:
            print "4"
            return False
        if solution[10] != 1:
            print "5"
            return False
        if solution[13] != 1:
            print "6"
            return False
        if solution[23] != 1:
            print "7"
            return False
        if solution[24] != 1 or solution[27] != 1 or solution[31] != 1 or solution[34] != 1:
            print "8"
            return False
        return True

    f = open(filename, "r")
    for i,line in enumerate(f):
        if i == 0: continue
        soln = [1 if a == "Y" else 0 for a in line.split(",")[:-1]]
        assert(validate(soln) is True), "Something's wrong"


# validate_apache()
# validate_bdbc()
# validate_bdbj()
# validate_llvm()
# validate_x264()
validate_SQL()