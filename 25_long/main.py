import os
import benczutils.bio as bio
import numpy as np

def calculateOverlaps(segments):
    segmentsToRemove = []
    for firstId in range(len(segments)):
        for secondId in range(len(segments)):
            if firstId == secondId:
                continue
            if segments[firstId] in segments[secondId]:
                segmentsToRemove.append(firstId)
    for i in reversed(segmentsToRemove):
        segments.pop(i)

    overlapMatrix = np.zeros((len(segments), len(segments)), np.int32)
    for leftId in range(len(segments)):
        for rightId in range(len(segments)):
            if leftId == rightId:
                continue
            left = segments[leftId]
            right = segments[rightId]

            for i in reversed(range(min(len(left), len(right)))):
                if left[-i:] == right[:i]:
                    overlapMatrix[leftId, rightId] = i
                    break
    return (overlapMatrix, segments)

def assembly(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        fasta = bio.readFasta(f.read())
        segments = []
        for key in fasta:
            segments.append(fasta[key])
       
        (overlapMatrix, segments) = calculateOverlaps(segments)

        while len(segments) > 1:
            bestOverlap = -1
            bestOverlapLocation = (-1, -1)
            for row in range(len(segments)):
                for col in range(len(segments)):
                    if overlapMatrix[row, col] > bestOverlap:
                        bestOverlap = overlapMatrix[row, col]
                        bestOverlapLocation = (row, col)

            segments[bestOverlapLocation[0]] = segments[bestOverlapLocation[0]] + segments[bestOverlapLocation[1]][bestOverlap:]
            segments.pop(bestOverlapLocation[1])

            (overlapMatrix, segments) = calculateOverlaps(segments)

            #break
        print(len(segments))
        print(all(s in segments[0] for s in segments))
        return segments[0]

print(assembly("sample.txt"))
print(assembly("rosalind_long.txt"))