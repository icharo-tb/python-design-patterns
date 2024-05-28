from mrjob.job import MRJob
import statistics, re

class sample_mr(MRJob):

    def mapper(self,line,*args):
        split_line = line.split(",")
        found = re.search('^[0-9]',split_line[5])
        if found != None:
            value = split_line[6]
            value = float(value.replace("$",""))
            key = split_line[4]
            yield key, value

    def reducer(self, key, values):
        values_lst = []
        for value in values:
            values_lst.append(value)
        yield key, statistics.mean(values_lst)

if __name__ == '__main__':
    sample_mr.run()