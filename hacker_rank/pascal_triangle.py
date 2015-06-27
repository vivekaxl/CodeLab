def pascal_traingle(rw):
    result = []
    for r in xrange(rw+1):
        row = [1]
        if r:
            last_row = result[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
            result.append(row)
        else:
            result.append([1])
    return result[-1]

if __name__ == "__main__":
    print pascal_traingle(6)

