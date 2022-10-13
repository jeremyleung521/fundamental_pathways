#!/usr/bin/env python
import numpy
import pickle


def sort_through_similarity(file_name='02_similarities.txt', threshold=0.6, output=False):
    """
    Given the output of pylcs, sort through it and only report values greater than threshold. 

    """

    # Loading in the similarities and listing everything greater than a percentage into "full"
    data = numpy.loadtxt(file_name)
    similar = []

    for pair in data:
        if pair[4] > threshold:
            similar.append([int(pair[2]), int(pair[3])])

    if output:
        numpy.savetxt('03_discarded.txt', similar)

    return similar


def pair_down_to_unique(input_array, output=True, output_path='.'):
    """
    Given an input array, pair down that list to only unique elements

    """ 
    # Finding the unique iter/seg pairs in 'similar'
    paired_down = []
    [paired_down.append(x) for x in input_array if x not in paired_down]
    
    if output:
        reduced_set = numpy.asarray(paired_down)
        numpy.savetxt(f'{output_path}/03_discarded_uniq.txt', reduced_set, fmt='%i')

    return paired_down


def sort_through_pickle_trace(paired_down, file_name='../output.pickle', print_output=True, output_path='.'):
    """
    Sort through a pickle file (from extract success) and pair it down to a list with only 
    traces that are not part of paired_down (i.e. the fundamental pathway).
    """
    # Now sorting through the output.pickle and find the traces...
    with open(file_name, 'rb') as fo:
        succ_trajs = pickle.load(fo)
    
    final_traces = [trace for trace in succ_trajs if trace[0] not in paired_down]
    
    with open(f'{output_path}/output_reduced.pickle', 'wb') as fo:
        pickle.dump(final_traces, fo)
     
    if print_output:
        print('fundamental pathways:')
        for trace in final_traces:
            print(trace[0])


if __name__ == "__main__":
    similar = sort_through_similarity(file_name='output/02_similarities.txt', threshold=0.6, output=False)
    paired_down = pair_down_to_unique(similar, output=True, output_path='output')
    sort_through_pickle_trace(paired_down, file_name='../output.pickle', print_output=True, output_path='output')
