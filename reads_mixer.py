"""
Created on June 20, 2014

@author: Joseph Korpela
"""

import random
import sys
import os

class reads_mixer(genome_id, nbr_chromosomes):
    def __init__(self, args=None):
        self._genome_id = genome_id
        self._nbr_chromosome = nbr_chromosomes

        self._reads_file = "reads_" + str(self._genome_id) + ".txt"
        self._chromosome_reads_files = []
        for i in range(1, self._nbr_chromosome+1):
            self._chromosome_reads_files.append("reads_" + str(self._genome_id) + "_chr_" + str(i) + ".txt")

    def consolidate(self):
        """
        Generates a random reference genome with the specified number of chromosomes,
        each of length length_chromosome
        """
        with open(self._reads_file,'w') as reads_file:
            while len(self._chromosome_reads_files) > 0:
                next_file = random.randint(0, len(self._chromosome_reads_files)-1)
                count = 0
                limit = random.randint(10000,100000)
                limit_reached = False
                for line in self._chromosome_reads_files[next_file]:
                    reads_file.write(line)
                    count += 1
                    if count == limit:
                        limit_reached = True
                        break
                if not limit_reached:
                    self._chromosome_reads_files[next_file].close()
                    del self._chromosome_reads_files[next_file]
            for chromosome_file in self._chromosome_reads_files:
                chromosome_file.close()
                os.remove(chromosome_file)